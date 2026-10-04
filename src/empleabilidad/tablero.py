"""Render del tablero: plantilla HTML + datos embebidos -> index.html.

Los datos se inyectan en el HTML en vez de cargarse con fetch(), para que el
tablero funcione abierto directamente desde el disco (file://), en GitHub Pages
y en cualquier servidor estatico, sin dependencias ni servidor.
"""

import json
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
PLANTILLA = RAIZ / "dashboard" / "plantilla.html"
DATOS = RAIZ / "dashboard" / "datos.json"
SALIDA = RAIZ / "dashboard" / "index.html"

MARCA = "/*__DATOS__*/ null"


def render():
    if not DATOS.exists():
        raise SystemExit("Faltan los datos. Corre primero el calculo de KPIs.")

    html = PLANTILLA.read_text(encoding="utf-8")
    if MARCA not in html:
        raise SystemExit(f"La plantilla no contiene el marcador {MARCA!r}")

    datos = json.loads(DATOS.read_text(encoding="utf-8"))
    # Se escapa </script> por si algun valor de texto lo contuviera.
    payload = json.dumps(datos, ensure_ascii=False).replace("</", "<\/")

    SALIDA.write_text(html.replace(MARCA, payload), encoding="utf-8")
    kb = SALIDA.stat().st_size / 1024
    print(f"  tablero: dashboard/index.html ({kb:.0f} KB, sin dependencias)")
    return SALIDA


if __name__ == "__main__":
    render()
    sys.exit(0)
