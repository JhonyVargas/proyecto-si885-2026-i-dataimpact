"""Orquestador. Un solo comando reconstruye todo desde la nomina cruda."""

import sys

from empleabilidad import ingest, kpis, modelo, tablero


def main():
    print("\n[1/4] Ingesta y seudonimizacion")
    ingest.ejecutar()

    print("\n[2/4] Construccion del Data Mart")
    modelo.construir()

    print("\n[3/4] Calculo de indicadores")
    kpis.imprimir(kpis.calcular())

    print("\n[4/4] Render del tablero")
    tablero.render()

    print("\nListo. Abrir: dashboard/index.html\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
