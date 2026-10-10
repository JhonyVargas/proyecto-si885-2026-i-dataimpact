"""Construccion del Data Mart dimensional sobre DuckDB.

Idempotente: cada ejecucion reconstruye el almacen desde la semilla. Correrlo
dos veces produce exactamente el mismo resultado.
"""

import sys
from pathlib import Path

import duckdb

RAIZ = Path(__file__).resolve().parents[2]
SEMILLA = RAIZ / "data" / "seed" / "egresados_seed.csv"
SCRIPT_SQL = RAIZ / "sql" / "modelo_estrella.sql"
ALMACEN = RAIZ / "data" / "marts" / "empleabilidad.duckdb"


def construir():
    if not SEMILLA.exists():
        raise SystemExit(
            f"Falta la semilla {SEMILLA.relative_to(RAIZ)}. Corre primero la ingesta.")

    ALMACEN.parent.mkdir(parents=True, exist_ok=True)
    if ALMACEN.exists():
        ALMACEN.unlink()

    con = duckdb.connect(str(ALMACEN))

    # Staging: todo como texto. La limpieza y el tipado ocurren al construir
    # las dimensiones, no al cargar.
    con.execute(
        "CREATE OR REPLACE TABLE stg_egresados AS "
        "SELECT * FROM read_csv_auto(?, header = true, all_varchar = true)",
        [str(SEMILLA)],
    )

    # Corrige semillas anteriores sin inventar un cargo a partir del empleador.
    con.execute("UPDATE stg_egresados SET area = 'No determinada', es_afin = NULL "
                "WHERE NULLIF(TRIM(cargo), '') IS NULL")

    con.execute(SCRIPT_SQL.read_text(encoding="utf-8"))

    tablas = con.execute(
        "SELECT table_name FROM information_schema.tables "
        "WHERE table_name LIKE 'dim_%' OR table_name LIKE 'fact_%' "
        "ORDER BY table_name"
    ).fetchall()

    for (tabla,) in tablas:
        n = con.execute(f"SELECT COUNT(*) FROM {tabla}").fetchone()[0]
        print(f"  {tabla:<28} {n:>4} filas")

    con.close()
    return ALMACEN


if __name__ == "__main__":
    construir()
    sys.exit(0)
