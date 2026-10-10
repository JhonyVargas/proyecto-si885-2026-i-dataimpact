"""Reglas de clasificacion del campo libre 'donde_labora'.

El campo de origen mezcla tres cosas distintas: empleador, cargo y titulares de
LinkedIn que no dicen nada sobre empleo. Aqui se separan y se clasifican.

Criterio: con 35 registros con evidencia, una tabla curada y auditable es
preferible a una heuristica. Cada decision queda explicita y revisable en un
diff. Las heuristicas de respaldo solo actuan sobre datos nuevos (encuesta).
"""

# --- Estados de evidencia ---------------------------------------------------
EMPLEO_VERIFICADO = "Empleo verificado"
NO_CONFIRMADO = "No confirmado"
SIN_EVIDENCIA = "Sin evidencia laboral"
SIN_INFORMACION = "Sin informacion"
SEGUNDO_GRADO = "Segundo grado (duplicado)"

# --- Areas de desempeno -----------------------------------------------------
DESARROLLO = "Desarrollo de Software"
DATOS_BI = "Datos / BI / IA"
INFRA_SOPORTE = "Infraestructura y Soporte"
GESTION = "Gestion de Proyectos"
DOCENCIA = "Docencia"
NO_DETERMINADA = "No determinada"

# Areas consideradas afines a la formacion en Ingenieria de Sistemas.
AREAS_AFINES = {DESARROLLO, DATOS_BI, INFRA_SOPORTE, GESTION}

# --- Sectores ---------------------------------------------------------------
SECTOR_TI = "TI / Consultoria"
SECTOR_PUBLICO = "Publico"
SECTOR_EDUCACION = "Educacion"
SECTOR_FINANCIERO = "Financiero"
SECTOR_MINERIA = "Mineria"
SECTOR_SERVICIOS = "Servicios"
SECTOR_INDEPENDIENTE = "Independiente"
SECTOR_NO_DET = "No determinado"

# --- Ambito geografico ------------------------------------------------------
# Criterio de asignacion: solo se declara la ubicacion cuando es verificable a
# partir del propio empleador, no del egresado. Tres casos la habilitan:
#   (a) el nombre contiene el topónimo ("Caja Tacna", "Municipalidad Distrital
#       de Ilabaya"),
#   (b) la entidad tiene sede unica conocida (Universidad Privada de Tacna),
#   (c) la empresa figura como empleador local en la fuente (Data Consulting).
# Todo lo demas queda 'No determinado'. Inferir la ubicacion de una persona a
# partir del alcance nacional de su empleador seria inventar: quien trabaja en
# NTT DATA puede estar en Lima o en remoto. Este hueco lo cierra la encuesta.
TACNA = "Tacna"
LIMA = "Lima"
AMBITO_NO_DET = "No determinado"

SECTOR_POR_EMPLEADOR = {
    "Cibergestion": (SECTOR_TI, AMBITO_NO_DET),
    "Data Consulting": (SECTOR_TI, TACNA),
    "Data Consulting SAC": (SECTOR_TI, TACNA),
    "Universidad Privada de Tacna": (SECTOR_EDUCACION, TACNA),
    "Caja Cencosud Scotiabank": (SECTOR_FINANCIERO, AMBITO_NO_DET),
    "Prosegur": (SECTOR_SERVICIOS, AMBITO_NO_DET),
    "Vurbis Interactive": (SECTOR_TI, AMBITO_NO_DET),
    "Municipalidad Distrital de Ilabaya": (SECTOR_PUBLICO, TACNA),
    "INCOTEC - Innovacion Eficiente": (SECTOR_TI, AMBITO_NO_DET),
    "CCITEC Ingenieria y Tecnologia": (SECTOR_TI, AMBITO_NO_DET),
    "Ensolvers": (SECTOR_TI, AMBITO_NO_DET),
    # Sede peruana en Lima; el egresado podria estar en remoto, pero la
    # operacion nacional de NTT DATA Peru es limena.
    "NTT DATA": (SECTOR_TI, LIMA),
    "Banco Falabella": (SECTOR_FINANCIERO, LIMA),
    "Instituto Superior John von Neumann": (SECTOR_EDUCACION, AMBITO_NO_DET),
    "Tsoft": (SECTOR_TI, AMBITO_NO_DET),
    "GLADCON GROUP": (SECTOR_NO_DET, AMBITO_NO_DET),
    "Southern Peru Copper Corporation": (SECTOR_MINERIA, AMBITO_NO_DET),
    "NAVITRACK": (SECTOR_TI, AMBITO_NO_DET),
    "Caja Tacna": (SECTOR_FINANCIERO, TACNA),
    "CAPSUR - Corporacion Capacitadora del Sur": (SECTOR_EDUCACION, AMBITO_NO_DET),
    "Servicios y Software del Sur S.A.C.": (SECTOR_TI, AMBITO_NO_DET),
    "Municipalidad Distrital Gregorio Albarracin Lanchipa": (SECTOR_PUBLICO, TACNA),
    "Freelance": (SECTOR_INDEPENDIENTE, AMBITO_NO_DET),
}

# Tabla curada: texto crudo -> (empleador, cargo, area)
# empleador None = la fuente solo declara un cargo, sin empresa.
# area NO_DETERMINADA = hay empleador pero no se conoce el cargo, por lo que la
# afinidad NO puede afirmarse ni negarse (queda NULL, no False).
CLASIFICACION = {
    "Cibergestion": ("Cibergestion", None, NO_DETERMINADA),
    "Data Consulting": ("Data Consulting", None, NO_DETERMINADA),
    "Data Consulting SAC": ("Data Consulting SAC", None, NO_DETERMINADA),
    "Universidad Privada de Tacna": ("Universidad Privada de Tacna", None, NO_DETERMINADA),
    "Caja Cencosud Scotiabank": ("Caja Cencosud Scotiabank", None, NO_DETERMINADA),
    "Prosegur": ("Prosegur", None, NO_DETERMINADA),
    "Vurbis Interactive": ("Vurbis Interactive", None, NO_DETERMINADA),
    "Municipalidad Distrital de Ilabaya": (
        "Municipalidad Distrital de Ilabaya", None, NO_DETERMINADA),
    "INCOTEC - Innovacion Eficiente": (
        "INCOTEC - Innovacion Eficiente", None, NO_DETERMINADA),
    "Frontend Developer / Graphic Designer (freelance)": (
        "Freelance", "Frontend Developer", DESARROLLO),
    "CCITEC Ingenieria y Tecnologia": (
        "CCITEC Ingenieria y Tecnologia", None, NO_DETERMINADA),
    "Ensolvers": ("Ensolvers", None, NO_DETERMINADA),
    "Web Developer": (None, "Web Developer", DESARROLLO),
    "Data Project Manager / AI / Digital Transformation": (
        None, "Data Project Manager", DATOS_BI),
    "Ingeniero de Sistemas - Sector Minero y Educacion": (
        None, "Ingeniero de Sistemas", INFRA_SOPORTE),
    "NTT DATA (Desarrollador Frontend)": (
        "NTT DATA", "Desarrollador Frontend", DESARROLLO),
    "Banco Falabella / Backend (Golang PostgreSQL Kafka GRPC)": (
        "Banco Falabella", "Desarrollador Backend", DESARROLLO),
    "Instituto Superior John von Neumann": (
        "Instituto Superior John von Neumann", None, NO_DETERMINADA),
    "Tsoft (Full Stack Developer / Node.js / NestJS / React / AWS)": (
        "Tsoft", "Full Stack Developer", DESARROLLO),
    "NTT DATA": ("NTT DATA", None, NO_DETERMINADA),
    "GLADCON GROUP": ("GLADCON GROUP", None, NO_DETERMINADA),
    "Desarrollador Web (JS / TS / React / NextJS)": (
        None, "Desarrollador Web", DESARROLLO),
    "Systems engineering graduate / Support TI / PowerBI": (
        None, "Soporte TI / Power BI", INFRA_SOPORTE),
    "Southern Peru Copper Corporation": (
        "Southern Peru Copper Corporation", None, NO_DETERMINADA),
    "NAVITRACK": ("NAVITRACK", None, NO_DETERMINADA),
    "Bachiller Software Developer (.NET / C# / Python / PHP / SQL)": (
        None, "Software Developer", DESARROLLO),
    "Caja Tacna": ("Caja Tacna", None, NO_DETERMINADA),
    "CAPSUR - Corporacion Capacitadora del Sur": (
        "CAPSUR - Corporacion Capacitadora del Sur", None, NO_DETERMINADA),
    "Servicios y Software del Sur S.A.C.": (
        "Servicios y Software del Sur S.A.C.", None, NO_DETERMINADA),
    "Municipalidad Distrital Gregorio Albarracin Lanchipa": (
        "Municipalidad Distrital Gregorio Albarracin Lanchipa", None, NO_DETERMINADA),
    "Full Stack Developer (Vue React JavaScript PHP MySQL)": (
        None, "Full Stack Developer", DESARROLLO),
}

# Titulares de LinkedIn que NO son evidencia de empleo. Contarlos como
# empleados es el error que infla la cifra de 35 a 42 en el informe de origen.
TITULARES_SIN_EVIDENCIA = {
    "Bachiller en Ingenieria de Sistemas",
    "Egresado en Ingenieria de Sistemas",
    "Egresado UPT",
    "Estudiante / Egresado UPT",
    "Portafolio profesional; empleador no visible",
}

# Resolucion de entidades: variantes del mismo empleador que la fuente escribe
# de forma distinta. Sin esto, "Data Consulting" y "Data Consulting SAC" se
# cuentan como dos empresas y el ranking de empleadores queda mal.
ALIAS_EMPLEADOR = {
    "Data Consulting SAC": "Data Consulting",
}

# Confiabilidad segun la fuente de la observacion.
CONFIANZA_POR_FUENTE = {
    "LinkedIn perfil directo": "Alta",
    "LinkedIn + UPT": "Alta",
    "LinkedIn": "Media",
    "LinkedIn (directorio)": "Media",
}


def _norm(texto):
    """Normaliza acentos para que el lookup no dependa de la codificacion."""
    if texto is None:
        return ""
    reemplazos = {
        "á": "a", "é": "e", "í": "i", "ó": "o", "ú": "u", "ñ": "n",
        "Á": "A", "É": "E", "Í": "I", "Ó": "O", "Ú": "U", "Ñ": "N",
        "—": "-", "–": "-",
    }
    for viejo, nuevo in reemplazos.items():
        texto = texto.replace(viejo, nuevo)
    return texto.strip()


def clasificar(donde_labora, fuente):
    """Convierte el texto libre en campos estructurados.

    Devuelve un dict con estado_evidencia, empleador, cargo, area, es_afin,
    sector, ambito y nivel_confianza.
    """
    crudo = _norm(donde_labora)
    vacio = {
        "estado_evidencia": SIN_INFORMACION,
        "empleador": None,
        "cargo": None,
        "area": NO_DETERMINADA,
        "es_afin": None,
        "sector": SECTOR_NO_DET,
        "ambito": AMBITO_NO_DET,
        "nivel_confianza": "Sin fuente",
    }

    if not crudo:
        return vacio

    if crudo.startswith("(2do grado"):
        return {**vacio, "estado_evidencia": SEGUNDO_GRADO}

    if crudo.startswith("No confirmado"):
        return {
            **vacio,
            "estado_evidencia": NO_CONFIRMADO,
            "nivel_confianza": CONFIANZA_POR_FUENTE.get(_norm(fuente), "Baja"),
        }

    if crudo in TITULARES_SIN_EVIDENCIA:
        return {
            **vacio,
            "estado_evidencia": SIN_EVIDENCIA,
            "nivel_confianza": CONFIANZA_POR_FUENTE.get(_norm(fuente), "Baja"),
        }

    if crudo in CLASIFICACION:
        empleador, cargo, area = CLASIFICACION[crudo]
        empleador = ALIAS_EMPLEADOR.get(empleador, empleador)
        sector, ambito = SECTOR_POR_EMPLEADOR.get(
            empleador, (SECTOR_NO_DET, AMBITO_NO_DET))
        # es_afin solo se afirma cuando el cargo es conocido. Con empleador
        # pero sin cargo la afinidad es desconocida, no falsa.
        if not cargo:
            area = NO_DETERMINADA
        es_afin = None if area == NO_DETERMINADA else (area in AREAS_AFINES)
        return {
            "estado_evidencia": EMPLEO_VERIFICADO,
            "empleador": empleador,
            "cargo": cargo,
            "area": area,
            "es_afin": es_afin,
            "sector": sector,
            "ambito": ambito,
            "nivel_confianza": CONFIANZA_POR_FUENTE.get(_norm(fuente), "Baja"),
        }

    # Valor no catalogado: se marca para revision manual en vez de adivinar.
    return {**vacio, "estado_evidencia": "Requiere revision", "cargo": crudo}
