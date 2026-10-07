"""Calculo de indicadores y exportacion de los marts que consume el dashboard.

Decision metodologica central
-----------------------------
Con 141 egresados en el marco censal y evidencia publica de solo una parte, NO
es posible afirmar una tasa de empleabilidad. Lo que se mide es COBERTURA DE
INFORMACION: que porcentaje del universo tiene situacion laboral conocida.

    cobertura      = egresados con evidencia / universo total
    empleabilidad  = NO ESTIMABLE con fuentes publicas

Confundir ambas cifras seria el error metodologico que invalidaria el estudio.
Todo indicador derivado se reporta sobre su denominador explicito.

Politica de publicacion
-----------------------
El JSON que se embebe en el tablero publico contiene SOLO agregados, nunca
registros individuales:

    por promocion   -> conteos de cobertura (estado de la evidencia)
    perfil laboral  -> solo el total de promociones; en sector y area, las
                       categorias con menos de UMBRAL_SUPRESION casos se
                       agrupan en "Otros"

Cruzar la promocion con el empleador, el sector o la ubicacion aislaria a
personas concretas en cohortes de 6 a 32 egresados.
"""

import json
import sys
from pathlib import Path

import duckdb

RAIZ = Path(__file__).resolve().parents[2]
ALMACEN = RAIZ / "data" / "marts" / "empleabilidad.duckdb"
SALIDA_JSON = RAIZ / "dashboard" / "datos.json"

# Umbral de supresion por celda pequena. Con cohortes de ~20 personas, un cruce
# de filtros puede aislar a un individuo. Por debajo de este n no se publica el
# detalle. Practica estandar de control de divulgacion estadistica.
UMBRAL_SUPRESION = 5

# "No determinado" es ausencia de dato, no un atributo de la persona: no se
# agrupa con categorias reales, para no mezclar lo desconocido con lo raro.
SIN_DETERMINAR = {"No determinado", "No determinada"}

CONSULTAS = {
    "universo": """
        SELECT COUNT(*) AS egresados_unicos
        FROM fact_observacion_laboral
    """,
    "cobertura_global": """
        SELECT
            COUNT(*)                                  AS universo,
            SUM(tiene_evidencia_empleo)               AS con_evidencia,
            ROUND(100.0 * SUM(tiene_evidencia_empleo) / COUNT(*), 1)
                                                      AS pct_cobertura
        FROM fact_observacion_laboral
    """,
    "estado_evidencia": """
        SELECT estado_evidencia, COUNT(*) AS n,
               ROUND(100.0 * COUNT(*) / SUM(COUNT(*)) OVER (), 1) AS pct
        FROM fact_observacion_laboral
        GROUP BY estado_evidencia
        ORDER BY n DESC, estado_evidencia
    """,
    "por_anio": """
        SELECT
            anio_grado,
            COUNT(*)                    AS egresados,
            SUM(tiene_evidencia_empleo) AS con_evidencia,
            ROUND(100.0 * SUM(tiene_evidencia_empleo) / COUNT(*), 1)
                                        AS pct_cobertura
        FROM fact_observacion_laboral
        GROUP BY anio_grado
        ORDER BY anio_grado
    """,
    # Unico corte que se publica por promocion: dice cuanto se sabe de cada
    # cohorte, no a que se dedica nadie. El tablero lo suma segun el filtro.
    "por_anio_estado": """
        SELECT anio_grado, estado_evidencia, COUNT(*) AS n
        FROM fact_observacion_laboral
        GROUP BY anio_grado, estado_evidencia
        ORDER BY anio_grado, estado_evidencia
    """,
    "nomina": """
        SELECT
            COUNT(*)                                 AS registros,
            COUNT(*) FILTER (WHERE es_segundo_grado) AS segundos_grados
        FROM dim_egresado
    """,
    "por_sector": """
        SELECT sector, COUNT(*) AS n
        FROM fact_observacion_laboral
        WHERE tiene_evidencia_empleo = 1
        GROUP BY sector
        ORDER BY n DESC, sector
    """,
    "por_area": """
        SELECT area, COUNT(*) AS n
        FROM fact_observacion_laboral f
        JOIN dim_area a USING (sk_area)
        WHERE tiene_evidencia_empleo = 1 AND area <> 'No determinada'
        GROUP BY area
        ORDER BY n DESC, area
    """,
    "por_ambito": """
        SELECT ambito, COUNT(*) AS n
        FROM fact_observacion_laboral
        WHERE tiene_evidencia_empleo = 1
        GROUP BY ambito
        ORDER BY n DESC, ambito
    """,
    # Sin el sector del empleador: el tablero no lo muestra, y publicarlo podria
    # delatar un sector que el corte por sector agrupo en "Otros".
    "top_empleadores": """
        SELECT e.nombre AS empleador, COUNT(*) AS n
        FROM fact_observacion_laboral f
        JOIN dim_empleador e USING (sk_empleador)
        GROUP BY e.nombre
        HAVING COUNT(*) >= 2
        ORDER BY n DESC, empleador
    """,
    "afinidad": """
        SELECT
            COUNT(*) FILTER (WHERE es_afin IS NOT NULL) AS cargo_conocido,
            COUNT(*) FILTER (WHERE es_afin = 1)         AS afines,
            ROUND(100.0 * COUNT(*) FILTER (WHERE es_afin = 1)
                  / NULLIF(COUNT(*) FILTER (WHERE es_afin IS NOT NULL), 0), 1)
                                                        AS pct_afinidad
        FROM fact_observacion_laboral
    """,
    "confianza": """
        SELECT nivel_confianza, COUNT(*) AS n
        FROM fact_observacion_laboral
        WHERE tiene_evidencia_empleo = 1
        GROUP BY nivel_confianza
        ORDER BY n DESC, nivel_confianza
    """,
    "calidad_datos": """
        SELECT
            COUNT(*) FILTER (WHERE estado_evidencia = 'Requiere revision')
                AS sin_clasificar,
            COUNT(*) FILTER (WHERE sk_area IS NULL)     AS sin_area,
            COUNT(*) FILTER (WHERE meses_insercion IS NOT NULL)
                AS con_tiempo_insercion
        FROM fact_observacion_laboral
    """,
}


def _filas(con, sql):
    cur = con.execute(sql)
    cols = [d[0] for d in cur.description]
    return [dict(zip(cols, fila)) for fila in cur.fetchall()]


def agrupar_menores(filas, clave, etiqueta, umbral=UMBRAL_SUPRESION):
    """Suma en una sola fila `etiqueta` las categorias con menos de `umbral`
    casos, sin revelar cuales son.

    Un unico egresado en mineria, o dos en el sector publico, bastan para
    reconocer a alguien en cohortes pequenas. Solo se publican por separado las
    categorias que alcanzan el umbral; "No determinado" nunca se agrupa. Orden:
    categorias visibles de mayor a menor, luego "Otros", luego lo no determinado.
    """
    visibles, sin_determinar = [], []
    otros_n = otros_k = 0
    for fila in filas:
        if fila[clave] in SIN_DETERMINAR:
            sin_determinar.append(fila)
        elif fila["n"] >= umbral:
            visibles.append(fila)
        else:
            otros_n += fila["n"]
            otros_k += 1

    resultado = sorted(visibles, key=lambda f: (-f["n"], f[clave]))
    if otros_k:
        resultado.append({clave: etiqueta, "n": otros_n, "agrupa": otros_k})
    return resultado + sin_determinar


def calcular():
    if not ALMACEN.exists():
        raise SystemExit("Falta el almacen. Corre primero: make modelo")

    con = duckdb.connect(str(ALMACEN), read_only=True)
    resultados = {nombre: _filas(con, sql) for nombre, sql in CONSULTAS.items()}
    con.close()

    resultados["por_sector"] = agrupar_menores(
        resultados["por_sector"], "sector", "Otros sectores")
    resultados["por_area"] = agrupar_menores(
        resultados["por_area"], "area", "Otras areas")

    resultados["_meta"] = {
        "umbral_supresion": UMBRAL_SUPRESION,
        "advertencia": (
            "pct_cobertura NO es tasa de empleabilidad. Mide que porcentaje "
            "del universo tiene situacion laboral verificable en fuentes "
            "publicas. La empleabilidad real no es estimable con estos datos."
        ),
    }

    SALIDA_JSON.parent.mkdir(parents=True, exist_ok=True)
    SALIDA_JSON.write_text(
        json.dumps(resultados, indent=2, ensure_ascii=False), encoding="utf-8")

    return resultados


def imprimir(r):
    cob = r["cobertura_global"][0]
    afi = r["afinidad"][0]
    cal = r["calidad_datos"][0]

    print()
    print("  " + "=" * 58)
    print("  INDICADORES DE EMPLEABILIDAD - EPIS UPT 2017-2024")
    print("  " + "=" * 58)
    print(f"  Universo (marco censal)          {cob['universo']:>6}")
    print(f"  Con evidencia laboral publica    {cob['con_evidencia']:>6}")
    print(f"  Cobertura de informacion         {cob['pct_cobertura']:>5}%")
    print(f"  Situacion laboral desconocida    "
          f"{100 - cob['pct_cobertura']:>5}%")
    print()
    print(f"  Cargo identificable              {afi['cargo_conocido']:>6}")
    print(f"  De esos, en area afin            {afi['afines']:>6}"
          f"  ({afi['pct_afinidad']}%)")
    print()
    print("  Estado de la evidencia:")
    for fila in r["estado_evidencia"]:
        print(f"    {fila['estado_evidencia']:<30} {fila['n']:>4}"
              f"  {fila['pct']:>5}%")
    print()
    print("  Top empleadores (>=2 egresados):")
    for fila in r["top_empleadores"]:
        print(f"    {fila['empleador']:<42} {fila['n']:>3}")
    print()
    print(f"  Sector publicado (categorias < {UMBRAL_SUPRESION} agrupadas):")
    for fila in r["por_sector"]:
        nota = f"  (agrupa {fila['agrupa']})" if "agrupa" in fila else ""
        print(f"    {fila['sector']:<42} {fila['n']:>3}{nota}")
    print()
    print("  Control de calidad:")
    print(f"    Registros sin clasificar       {cal['sin_clasificar']:>4}")
    print(f"    Con tiempo de insercion        {cal['con_tiempo_insercion']:>4}"
          "   <- requiere encuesta")
    print("  " + "=" * 58)


if __name__ == "__main__":
    imprimir(calcular())
    sys.exit(0)
