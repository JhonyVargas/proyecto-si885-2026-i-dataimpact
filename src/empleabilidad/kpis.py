"""Indicadores agregados publicables. No exporta observaciones individuales."""
import json
from collections import Counter
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo
import duckdb

RAIZ = Path(__file__).resolve().parents[2]
ALMACEN = RAIZ / 'data' / 'marts' / 'empleabilidad.duckdb'
SALIDA_JSON = RAIZ / 'dashboard' / 'datos.json'
UMBRAL_SUPRESION = 5


def porcentaje(n, d):
    return round(100 * n / d, 1) if d else None


def proteger_par(n, total):
    """No publica ni el valor pequeño ni su complemento deducible."""
    if any(0 < v < UMBRAL_SUPRESION for v in (n, total - n)):
        return {'n': None, 'total': total, 'pct': None, 'protegido': True}
    return {'n': n, 'total': total, 'pct': porcentaje(n, total), 'protegido': False}


def agrupar(contador):
    """Agrupa celdas pequeñas; absorbe otra categoría si el grupo sigue pequeño.

    No exporta las etiquetas ni los valores de las categorías absorbidas.
    """
    grandes = [(k, n) for k, n in contador.items() if n >= UMBRAL_SUPRESION]
    pequenos = [n for n in contador.values() if 0 < n < UMBRAL_SUPRESION]
    agrupado = sum(pequenos)
    while 0 < agrupado < UMBRAL_SUPRESION and grandes:
        k, n = min(grandes, key=lambda x: (x[1], x[0]))
        grandes.remove((k, n))
        agrupado += n
    salida = [{'categoria': k, 'n': n} for k, n in grandes]
    if agrupado >= UMBRAL_SUPRESION:
        salida.append({'categoria': 'Otras categorías agrupadas', 'n': agrupado})
    return sorted(salida, key=lambda x: (-x['n'], x['categoria']))


def construir_publicacion(filas, registros, excluidos):
    evidencia = [f for f in filas if f['tiene_evidencia_empleo'] == 1]
    total, n = len(filas), len(evidencia)
    promociones = []
    for anio in sorted({f['anio_grado'] for f in filas}):
        grupo = [f for f in filas if f['anio_grado'] == anio]
        par = proteger_par(sum(f['tiene_evidencia_empleo'] for f in grupo), len(grupo))
        promociones.append({'anio': anio, 'universo': len(grupo), 'evidencia': par})
    # Una única promoción suprimida sería recuperable restando del total global.
    ocultas = [p for p in promociones if p['evidencia']['protegido']]
    if len(ocultas) == 1:
        candidatas = [p for p in promociones if not p['evidencia']['protegido']]
        if candidatas:
            extra = min(candidatas, key=lambda p: p['universo'])
            extra['evidencia'] = {'n': None, 'total': extra['universo'], 'pct': None, 'protegido': True}
    conocidos = [f for f in evidencia if f['es_afin'] is not None]
    afines = sum(f['es_afin'] == 1 for f in conocidos)
    calidad = {}
    condiciones = {
        'empleador': lambda f: bool(f['empleador']),
        'cargo': lambda f: bool((f['cargo'] or '').strip()),
        'ambito': lambda f: f['ambito'] not in ('', None, 'No determinado'),
        'area': lambda f: f['area'] not in ('', None, 'No determinada'),
        'afinidad': lambda f: f['es_afin'] is not None,
    }
    for nombre, condicion in condiciones.items():
        calidad[nombre] = proteger_par(sum(condicion(f) for f in evidencia), n)
    return {
        'resumen': {'universo': total, 'evidencia': proteger_par(n, total)},
        'promociones': promociones,
        'estado': agrupar(Counter(f['estado_evidencia'] for f in filas)),
        'perfil': {
            'sector': agrupar(Counter(f['sector'] for f in evidencia)),
            'area': agrupar(Counter(f['area'] for f in evidencia)),
            'empleador': agrupar(Counter(f['empleador'] or 'No identificado' for f in evidencia)),
            'ambito': agrupar(Counter(f['ambito'] for f in evidencia)),
        },
        'afinidad': proteger_par(afines, len(conocidos)),
        'calidad': calidad,
        'confianza': agrupar(Counter(f['nivel_confianza'] for f in evidencia)),
        'revision': proteger_par(sum(f['estado_evidencia'] == 'Requiere revision' for f in filas), total),
        '_meta': {
            'registros': registros, 'excluidos': excluidos,
            'umbral_supresion': UMBRAL_SUPRESION,
            'corte': 'Setiembre 2026',
            'generado': datetime.now(ZoneInfo('America/Lima')).isoformat(timespec='seconds'),
            'fuentes': 'Nómina oficial EPIS UPT y fuentes públicas de LinkedIn',
            'politica': 'Agregados marginales globales, sin cruces entre dimensiones. '
                        'Las promociones solo permiten consultar universo y cobertura protegida. '
                        'Categorías pequeñas agrupadas y complementos protegidos.',
        },
    }


def calcular():
    if not ALMACEN.exists():
        raise SystemExit('Falta el almacén. Ejecuta primero empleabilidad.modelo.')
    with duckdb.connect(str(ALMACEN), read_only=True) as con:
        cur = con.execute('''SELECT f.anio_grado, f.estado_evidencia,
            f.tiene_evidencia_empleo, f.es_afin, f.sector, f.ambito,
            f.nivel_confianza, f.cargo, e.nombre AS empleador, a.area
            FROM fact_observacion_laboral f
            LEFT JOIN dim_empleador e USING (sk_empleador)
            LEFT JOIN dim_area a USING (sk_area)''')
        cols = [c[0] for c in cur.description]
        filas = [dict(zip(cols, f)) for f in cur.fetchall()]
        registros = con.execute('SELECT COUNT(*) FROM stg_egresados').fetchone()[0]
        excluidos = con.execute('SELECT COUNT(*) FROM dim_egresado WHERE es_segundo_grado').fetchone()[0]
    resultado = construir_publicacion(filas, registros, excluidos)
    SALIDA_JSON.parent.mkdir(parents=True, exist_ok=True)
    SALIDA_JSON.write_text(json.dumps(resultado, ensure_ascii=False, indent=2), encoding='utf-8')
    return resultado


def imprimir(r):
    s = r['resumen']
    print(f"Universo: {s['universo']} | Evidencia: {s['evidencia']['n']} | "
          f"Cobertura: {s['evidencia']['pct']}%")
    print('Salida pública: agregados protegidos, sin registros individuales.')


if __name__ == '__main__':
    imprimir(calcular())
