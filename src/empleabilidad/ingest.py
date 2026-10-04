"""Ingesta: nomina nominal (privada) -> semilla seudonimizada (publicable).

Esta es la unica etapa que ve nombres reales. Todo lo que sigue trabaja sobre
identificadores seudonimos, de modo que el resto del pipeline y sus salidas
pueden publicarse sin exponer datos personales.
"""

import csv
import hashlib
import os
import sys
from datetime import date, datetime
from pathlib import Path

from empleabilidad.clasificacion import clasificar

RAIZ = Path(__file__).resolve().parents[2]
ENTRADA = RAIZ / "data" / "raw" / "nomina_oficial_upt.csv"
SALIDA = RAIZ / "data" / "seed" / "egresados_seed.csv"

COLUMNAS_SALIDA = [
    "sk_egresado", "anio_grado", "fecha_grado", "estado_evidencia",
    "empleador", "cargo", "area", "es_afin", "sector", "ambito",
    "nivel_confianza", "fuente",
]


class ErrorContrato(Exception):
    """El archivo de entrada no cumple el contrato de datos."""


def _sal():
    sal = os.environ.get("UPT_SALT")
    if not sal or sal == "cambiar-por-una-sal-aleatoria":
        # Sal de desarrollo: reproducible para que el pipeline corra sin
        # configuracion. En produccion se exige una sal real via .env.
        return "desarrollo-sal-no-usar-en-produccion"
    return sal


def seudonimizar(nombre, sal):
    """Hash salado y truncado. Determinista: la misma persona produce el mismo
    identificador entre oleadas de encuesta, sin ser reversible."""
    digest = hashlib.sha256((nombre.strip().lower() + sal).encode("utf-8"))
    return "EG-" + digest.hexdigest()[:10].upper()


def validar_contrato(filas):
    """Contrato de datos. Falla ruidosamente: un dato malo detiene el pipeline
    en vez de propagarse silenciosamente hasta el dashboard."""
    errores = []
    hoy = date.today()
    vistos = set()

    for f in filas:
        nro = f.get("nro", "?")

        if not f.get("nombre_completo", "").strip():
            errores.append(f"registro {nro}: nombre_completo vacio")

        try:
            fecha = datetime.strptime(f["fecha_grado"], "%d/%m/%Y").date()
            if not (date(2017, 1, 1) <= fecha <= hoy):
                errores.append(
                    f"registro {nro}: fecha_grado {fecha} fuera del rango 2017-hoy")
        except (ValueError, KeyError):
            errores.append(
                f"registro {nro}: fecha_grado invalida ({f.get('fecha_grado')!r})")

        if nro in vistos:
            errores.append(f"registro {nro}: numero duplicado")
        vistos.add(nro)

    if errores:
        raise ErrorContrato(
            "El archivo de entrada no cumple el contrato:\n  - "
            + "\n  - ".join(errores))
    return True


def ejecutar():
    if not ENTRADA.exists():
        raise SystemExit(
            f"No se encontro {ENTRADA}.\n"
            "La nomina nominal no se versiona (contiene datos personales).\n"
            "Colocala en data/raw/ antes de correr el pipeline.")

    with ENTRADA.open(encoding="utf-8") as fh:
        filas = list(csv.DictReader(fh))

    validar_contrato(filas)

    sal = _sal()
    SALIDA.parent.mkdir(parents=True, exist_ok=True)

    escritas = 0
    with SALIDA.open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=COLUMNAS_SALIDA)
        w.writeheader()
        for f in filas:
            fecha = datetime.strptime(f["fecha_grado"], "%d/%m/%Y").date()
            clas = clasificar(f.get("donde_labora"), f.get("fuente"))
            w.writerow({
                "sk_egresado": seudonimizar(f["nombre_completo"], sal),
                "anio_grado": fecha.year,
                "fecha_grado": fecha.isoformat(),
                "estado_evidencia": clas["estado_evidencia"],
                "empleador": clas["empleador"] or "",
                "cargo": clas["cargo"] or "",
                "area": clas["area"],
                "es_afin": "" if clas["es_afin"] is None else int(clas["es_afin"]),
                "sector": clas["sector"],
                "ambito": clas["ambito"],
                "nivel_confianza": clas["nivel_confianza"],
                "fuente": (f.get("fuente") or "").strip(),
            })
            escritas += 1

    print(f"  ingesta: {escritas} registros -> {SALIDA.relative_to(RAIZ)}")
    return escritas


if __name__ == "__main__":
    sys.exit(0 if ejecutar() else 1)
