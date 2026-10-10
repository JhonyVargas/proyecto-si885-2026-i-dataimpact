"""Verifica indicadores y protección en el paquete público real."""
import json
import duckdb
import pytest
from empleabilidad import modelo, kpis, tablero


@pytest.fixture
def publicacion(tmp_path, monkeypatch):
    monkeypatch.setattr(modelo, 'ALMACEN', tmp_path / 'modelo.duckdb')
    monkeypatch.setattr(kpis, 'ALMACEN', modelo.ALMACEN)
    monkeypatch.setattr(kpis, 'SALIDA_JSON', tmp_path / 'datos.json')
    modelo.construir()
    return kpis.calcular()


def test_cifras_y_denominadores(publicacion):
    r = publicacion
    assert r['resumen']['universo'] == 139
    assert r['resumen']['evidencia']['n'] == 35
    assert r['resumen']['evidencia']['pct'] == 25.2
    assert r['_meta']['registros'] == 141
    assert r['_meta']['excluidos'] == 2
    assert r['calidad']['cargo']['n'] == 11
    assert r['calidad']['empleador']['n'] == 28
    assert r['calidad']['ambito']['n'] == 13
    assert r['calidad']['afinidad']['n'] == 11
    assert r['afinidad']['total'] == 11
    assert r['afinidad']['n'] == 11


def test_cargo_ausente_no_permite_inferir_area(publicacion):
    with duckdb.connect(str(modelo.ALMACEN), read_only=True) as con:
        assert con.execute("SELECT COUNT(*) FROM fact_observacion_laboral "
                           "WHERE NULLIF(cargo, '') IS NULL AND es_afin IS NOT NULL").fetchone()[0] == 0


def test_exportacion_sin_individuos_y_con_celdas_protegidas(publicacion):
    payload = json.dumps(publicacion)
    for secreto in ('sk_egresado', 'EG-', 'filas', 'John von Neumann', 'Banco Falabella'):
        assert secreto not in payload
    for rows in [publicacion['estado'], publicacion['confianza'], *publicacion['perfil'].values()]:
        assert all(r['n'] >= 5 for r in rows)
    for p in publicacion['promociones']:
        e = p['evidencia']
        if e['protegido']:
            assert e['n'] is None and e['pct'] is None
        else:
            assert e['n'] == 0 or e['n'] >= 5
            assert e['total'] - e['n'] == 0 or e['total'] - e['n'] >= 5


def test_agregados_conservan_bases(publicacion):
    assert sum(r['n'] for r in publicacion['estado']) == 139
    assert sum(r['n'] for r in publicacion['confianza']) == 35
    for filas in publicacion['perfil'].values():
        assert sum(r['n'] for r in filas) == 35


def test_agrupacion_protege_etiquetas_y_complementos():
    assert kpis.agrupar({'Empresa pequeña': 1, 'Otra': 7}) == [
        {'categoria': 'Otras categorías agrupadas', 'n': 8}]
    assert kpis.agrupar({'Caso único': 1}) == []
    assert kpis.proteger_par(1, 35)['n'] is None
    assert kpis.proteger_par(34, 35)['n'] is None
    assert kpis.proteger_par(0, 35)['n'] == 0
    assert kpis.proteger_par(0, 0)['pct'] is None


def test_supresion_complementaria_promociones():
    rows = [{'anio_grado': year, 'tiene_evidencia_empleo': 1,
             'estado_evidencia': 'Empleo verificado', 'cargo': 'Developer',
             'es_afin': 1, 'empleador': 'Empresa', 'area': 'Desarrollo',
             'sector': 'TI', 'ambito': 'No determinado', 'nivel_confianza': 'Alta'}
            for year, n in ((2020, 1), (2021, 5)) for _ in range(n)]
    r = kpis.construir_publicacion(rows, 6, 0)
    assert all(p['evidencia']['protegido'] for p in r['promociones'])


def test_render_contiene_solo_exportacion_publica(publicacion, tmp_path, monkeypatch):
    data = tmp_path / 'datos.json'
    data.write_text(json.dumps(publicacion), encoding='utf-8')
    monkeypatch.setattr(tablero, 'DATOS', data)
    monkeypatch.setattr(tablero, 'SALIDA', tmp_path / 'index.html')
    html = tablero.render().read_text(encoding='utf-8')
    assert '/*__DATOS__*/ null' not in html
    assert 'EG-' not in html
    assert '145 registros' not in html
    assert 'data-page="ayuda"' in html
    assert 'Arquitectura del proyecto' in html
