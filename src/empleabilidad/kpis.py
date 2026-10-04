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
        ORDER BY n DESC
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
    "por_sector": """
        SELECT sector, COUNT(*) AS n
        FROM fact_observacion_laboral
        WHERE tiene_evidencia_empleo = 1
        GROUP BY sector
        ORDER BY n DESC
    """,
    "por_area": """
        SELECT area, COUNT(*) AS n
        FROM fact_observacion_laboral f
        JOIN dim_area a USING (sk_area)
        WHERE tiene_evidencia_empleo = 1 AND area <> 'No determinada'
        GROUP BY area
        ORDER BY n DESC
    """,
    "top_empleadores": """
        SELECT e.nombre AS empleador, e.sector, COUNT(*) AS n
        FROM fact_observacion_laboral f
        JOIN dim_empleador e USING (sk_empleador)
        GROUP BY e.nombre, e.sector
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
        ORDER BY n DESC
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


def calcular():
    if not ALMACEN.exists():
        raise SystemExit("Falta el almacen. Corre primero: make modelo")

    con = duckdb.connect(str(ALMACEN), read_only=True)
    resultados = {nombre: _filas(con, sql) for nombre, sql in CONSULTAS.items()}
    con.close()

    # Supresion por celda pequena sobre los cortes publicables.
    for corte in ("por_sector", "por_area"):
        for fila in resultados[corte]:
            if fila["n"] < UMBRAL_SUPRESION:
                fila["suprimido"] = True

    # Filas individuales (ya seudonimizadas) para que el tablero recalcule cada
    # indicador con los filtros aplicados, en vez de servir agregados fijos.
    # Son 139 registros: cabe de sobra en el navegador y hace el filtrado real.
    con = duckdb.connect(str(ALMACEN), read_only=True)
    resultados["filas"] = _filas(con, """
        SELECT
            f.sk_egresado, f.anio_grado, f.estado_evidencia, f.sector,
            f.ambito, f.nivel_confianza, f.tiene_evidencia_empleo, f.es_afin,
            COALESCE(e.nombre, '')  AS empleador,
            COALESCE(a.area, '')    AS area
        FROM fact_observacion_laboral f
        LEFT JOIN dim_empleador e USING (sk_empleador)
        LEFT JOIN dim_area      a USING (sk_area)
        ORDER BY f.anio_grado, f.sk_egresado
    """)
    con.close()

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
    print("  Control de calidad:")
    print(f"    Registros sin clasificar       {cal['sin_clasificar']:>4}")
    print(f"    Con tiempo de insercion        {cal['con_tiempo_insercion']:>4}"
          "   <- requiere encuesta")
    print("  " + "=" * 58)


if __name__ == "__main__":
    imprimir(calcular())
    sys.exit(0)
