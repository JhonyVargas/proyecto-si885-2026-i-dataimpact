"""Tests del contrato de datos y de la seudonimizacion."""

import pytest

from empleabilidad.ingest import ErrorContrato, seudonimizar, validar_contrato


def _fila(**kw):
    base = {"nro": "1", "nombre_completo": "Juan Perez", "fecha_grado": "15/06/2020"}
    base.update(kw)
    return base


def test_contrato_acepta_fila_valida():
    assert validar_contrato([_fila()]) is True


def test_contrato_rechaza_nombre_vacio():
    with pytest.raises(ErrorContrato, match="nombre_completo vacio"):
        validar_contrato([_fila(nombre_completo="  ")])


def test_contrato_rechaza_fecha_invalida():
    with pytest.raises(ErrorContrato, match="fecha_grado invalida"):
        validar_contrato([_fila(fecha_grado="31/31/2020")])


def test_contrato_rechaza_fecha_fuera_de_rango():
    with pytest.raises(ErrorContrato, match="fuera del rango"):
        validar_contrato([_fila(fecha_grado="15/06/1999")])


def test_contrato_rechaza_nro_duplicado():
    with pytest.raises(ErrorContrato, match="duplicado"):
        validar_contrato([_fila(nro="7"), _fila(nro="7")])


def test_seudonimo_es_determinista():
    """La misma persona debe producir el mismo id entre oleadas de encuesta."""
    assert seudonimizar("Juan Perez", "sal") == seudonimizar("Juan Perez", "sal")


def test_seudonimo_ignora_mayusculas_y_espacios():
    assert seudonimizar("  JUAN PEREZ ", "sal") == seudonimizar("juan perez", "sal")


def test_seudonimo_cambia_con_la_sal():
    """Sin sal distinta, un atacante puede romper el hash por fuerza bruta
    sobre el universo conocido de egresados."""
    assert seudonimizar("Juan Perez", "sal-a") != seudonimizar("Juan Perez", "sal-b")


def test_seudonimo_no_contiene_el_nombre():
    sk = seudonimizar("Juan Perez", "sal")
    assert "juan" not in sk.lower() and "perez" not in sk.lower()
