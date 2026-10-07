"""Tests de lo que se publica en el tablero.

El tablero es publico: todo lo que viaja en datos.json queda a la vista de
cualquiera que abra el codigo fuente de la pagina. Estos tests protegen la
politica de publicacion, no solo la interfaz.
"""

import json
import re

import pytest

from empleabilidad import kpis, modelo, tablero
from empleabilidad.kpis import SIN_DETERMINAR, UMBRAL_SUPRESION, agrupar_menores

SEUDONIMO = re.compile(r"EG-[0-9A-F]{10}")
CORTES_POR_PROMOCION = {
    "por_anio": {"anio_grado", "egresados", "con_evidencia", "pct_cobertura"},
    "por_anio_estado": {"anio_grado", "estado_evidencia", "n"},
}
ETIQUETAS_OTROS = {"Otros sectores", "Otras areas"}


# --- Regla de agrupacion ----------------------------------------------------

def test_agrupa_categorias_menores_en_otros():
    filas = [
        {"sector": "TI", "n": 14},
        {"sector": "Educacion", "n": 5},
        {"sector": "Financiero", "n": 3},
        {"sector": "Publico", "n": 2},
        {"sector": "Mineria", "n": 1},
    ]
    r = agrupar_menores(filas, "sector", "Otros sectores", umbral=5)
    assert r == [
        {"sector": "TI", "n": 14},
        {"sector": "Educacion", "n": 5},
        {"sector": "Otros sectores", "n": 6, "agrupa": 3},
    ]


def test_otros_no_revela_que_categorias_suma():
    filas = [{"sector": "TI", "n": 9}, {"sector": "Mineria", "n": 1}]
    otros = agrupar_menores(filas, "sector", "Otros sectores", umbral=5)[-1]
    assert set(otros) == {"sector", "n", "agrupa"}
    assert "Mineria" not in json.dumps(otros)


def test_no_determinado_nunca_se_agrupa():
    """Lo desconocido no es una categoria rara: mezclarlo con 'Otros' haria
    pasar falta de informacion por un sector real."""
    filas = [{"sector": "No determinado", "n": 2}, {"sector": "TI", "n": 7}]
    r = agrupar_menores(filas, "sector", "Otros sectores", umbral=5)
    assert r == [{"sector": "TI", "n": 7}, {"sector": "No determinado", "n": 2}]


def test_sin_categorias_menores_no_crea_otros():
    filas = [{"area": "Desarrollo", "n": 8}, {"area": "Datos", "n": 5}]
    assert agrupar_menores(filas, "area", "Otras areas", umbral=5) == filas


# --- Lo que efectivamente se publica -----------------------------------------

@pytest.fixture(scope="module")
def publicado(tmp_path_factory):
    """Corre modelo -> KPIs -> tablero desde la semilla, en una carpeta temporal."""
    tmp = tmp_path_factory.mktemp("publicado")
    mp = pytest.MonkeyPatch()
    mp.setattr(modelo, "ALMACEN", tmp / "empleabilidad.duckdb")
    mp.setattr(kpis, "ALMACEN", tmp / "empleabilidad.duckdb")
    mp.setattr(kpis, "SALIDA_JSON", tmp / "datos.json")
    mp.setattr(tablero, "DATOS", tmp / "datos.json")
    mp.setattr(tablero, "SALIDA", tmp / "index.html")
    try:
        modelo.construir()
        resultados = kpis.calcular()
        tablero.render()
        yield {
            "r": resultados,
            "json": (tmp / "datos.json").read_text(encoding="utf-8"),
            "html": (tmp / "index.html").read_text(encoding="utf-8"),
        }
    finally:
        mp.undo()


def test_no_publica_registros_individuales(publicado):
    assert "filas" not in publicado["r"]
    for texto in (publicado["json"], publicado["html"]):
        assert "sk_egresado" not in texto
        assert not SEUDONIMO.search(texto), "un seudonimo viajo al tablero"


def test_perfil_laboral_no_se_cruza_con_promocion(publicado):
    """Por promocion solo se publica cobertura. Cruzar el anio con empleador,
    sector o ubicacion aislaria a personas en cohortes de 6 a 32 egresados."""
    for clave, filas in publicado["r"].items():
        if not isinstance(filas, list):
            continue
        for fila in filas:
            if clave in CORTES_POR_PROMOCION:
                assert set(fila) == CORTES_POR_PROMOCION[clave], clave
            else:
                assert "anio_grado" not in fila, f"{clave} se cruza con la promocion"


def test_sector_y_area_sin_categorias_pequenas(publicado):
    for corte, clave in (("por_sector", "sector"), ("por_area", "area")):
        for fila in publicado["r"][corte]:
            if fila[clave] in ETIQUETAS_OTROS | SIN_DETERMINAR:
                continue
            assert fila["n"] >= UMBRAL_SUPRESION, (corte, fila)


def test_los_totales_cuadran(publicado):
    r = publicado["r"]
    cob = r["cobertura_global"][0]
    assert sum(f["n"] for f in r["por_sector"]) == cob["con_evidencia"]
    assert sum(f["n"] for f in r["por_ambito"]) == cob["con_evidencia"]
    assert sum(f["n"] for f in r["por_anio_estado"]) == cob["universo"]
    # Area conocida <=> cargo identificable: mismo denominador que la afinidad.
    assert sum(f["n"] for f in r["por_area"]) == r["afinidad"][0]["cargo_conocido"]
    for anio in r["por_anio"]:
        suma = sum(f["n"] for f in r["por_anio_estado"]
                   if f["anio_grado"] == anio["anio_grado"])
        assert suma == anio["egresados"]
    nom = r["nomina"][0]
    assert nom["registros"] - nom["segundos_grados"] == cob["universo"]


@pytest.mark.parametrize("corte, clave", [
    ("estado_evidencia", "estado_evidencia"),
    ("por_ambito", "ambito"),
    ("top_empleadores", "empleador"),
    ("confianza", "nivel_confianza"),
])
def test_orden_determinista_en_empates(publicado, corte, clave):
    """Sin desempate, dos ejecuciones podian ordenar distinto los empates y el
    tablero cambiaba sin que cambiaran los datos."""
    filas = publicado["r"][corte]
    assert filas == sorted(filas, key=lambda f: (-f["n"], f[clave]))
