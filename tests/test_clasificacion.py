"""Tests de la capa de clasificacion.

El test que mas importa es test_titular_no_es_empleo: es precisamente el error
que infla la cifra de egresados empleados en el informe de origen.
"""

import pytest

from empleabilidad.clasificacion import (
    EMPLEO_VERIFICADO,
    NO_CONFIRMADO,
    SEGUNDO_GRADO,
    SIN_EVIDENCIA,
    SIN_INFORMACION,
    clasificar,
)


def test_campo_vacio_es_sin_informacion():
    r = clasificar("", "")
    assert r["estado_evidencia"] == SIN_INFORMACION
    assert r["es_afin"] is None


def test_titular_no_es_empleo():
    """Un titular de LinkedIn que solo dice 'Egresado' no es evidencia de
    empleo. Contarlo como empleado sobreestima la empleabilidad."""
    for titular in (
        "Bachiller en Ingenieria de Sistemas",
        "Egresado UPT",
        "Estudiante / Egresado UPT",
        "Portafolio profesional; empleador no visible",
    ):
        r = clasificar(titular, "LinkedIn")
        assert r["estado_evidencia"] == SIN_EVIDENCIA, titular
        assert r["empleador"] is None


def test_no_confirmado_no_cuenta_como_empleo():
    r = clasificar("No confirmado (solo educacion visible)", "LinkedIn")
    assert r["estado_evidencia"] == NO_CONFIRMADO


def test_segundo_grado_se_marca_como_duplicado():
    r = clasificar("(2do grado - bachiller ya en 2023)", "")
    assert r["estado_evidencia"] == SEGUNDO_GRADO


def test_separa_empleador_y_cargo():
    r = clasificar("NTT DATA (Desarrollador Frontend)", "LinkedIn")
    assert r["empleador"] == "NTT DATA"
    assert r["cargo"] == "Desarrollador Frontend"
    assert r["es_afin"] == 1 or r["es_afin"] is True


def test_cargo_sin_empleador():
    r = clasificar("Web Developer", "LinkedIn")
    assert r["empleador"] is None
    assert r["cargo"] == "Web Developer"
    assert r["estado_evidencia"] == EMPLEO_VERIFICADO


def test_afinidad_desconocida_no_es_falsa():
    """Con empleador pero sin cargo no se puede saber si trabaja en area afin.
    Debe quedar None (desconocido), nunca False."""
    r = clasificar("Caja Tacna", "LinkedIn perfil directo")
    assert r["estado_evidencia"] == EMPLEO_VERIFICADO
    assert r["es_afin"] is None, "afinidad desconocida no debe forzarse a False"


def test_alias_de_empleador_se_resuelve():
    a = clasificar("Data Consulting", "LinkedIn perfil directo")
    b = clasificar("Data Consulting SAC", "LinkedIn (directorio)")
    assert a["empleador"] == b["empleador"] == "Data Consulting"


def test_confianza_segun_fuente():
    directo = clasificar("Caja Tacna", "LinkedIn perfil directo")
    dirtorio = clasificar("Prosegur", "LinkedIn (directorio)")
    assert directo["nivel_confianza"] == "Alta"
    assert dirtorio["nivel_confianza"] == "Media"


def test_valor_desconocido_se_marca_para_revision():
    r = clasificar("Empresa Nueva Que No Existia Antes", "LinkedIn")
    assert r["estado_evidencia"] == "Requiere revision"

def test_empleador_educativo_no_implica_docencia():
    r = clasificar('Instituto Superior John von Neumann', 'LinkedIn')
    assert r['cargo'] is None
    assert r['area'] == 'No determinada'
    assert r['es_afin'] is None
