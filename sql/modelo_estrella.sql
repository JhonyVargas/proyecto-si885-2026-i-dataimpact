-- ---------------------------------------------------------------------------
-- Data Mart de empleabilidad - EPIS UPT
-- Modelo dimensional (Kimball) sobre DuckDB.
--
-- Grano de la tabla de hechos:
--   una observacion de la situacion laboral de un egresado,
--   en una fecha, proveniente de una fuente determinada.
--
-- Modelar la fuente y su confiabilidad es deliberado: un perfil directo de
-- LinkedIn y una entrada de directorio no son evidencia del mismo peso, y el
-- dashboard debe poder distinguirlas.
-- ---------------------------------------------------------------------------

DROP TABLE IF EXISTS fact_observacion_laboral;
DROP TABLE IF EXISTS dim_egresado;
DROP TABLE IF EXISTS dim_tiempo;
DROP TABLE IF EXISTS dim_empleador;
DROP TABLE IF EXISTS dim_area;
DROP TABLE IF EXISTS dim_fuente;

-- Nota: la tabla stg_egresados (espejo crudo de la semilla, todo VARCHAR) la
-- crea el cargador en modelo.py antes de ejecutar este script.

-- --- Dimensiones -----------------------------------------------------------

CREATE TABLE dim_egresado AS
SELECT
    sk_egresado,
    CAST(anio_grado AS INTEGER)  AS anio_grado,
    CAST(fecha_grado AS DATE)    AS fecha_grado,
    estado_evidencia = 'Segundo grado (duplicado)' AS es_segundo_grado
FROM stg_egresados;

CREATE TABLE dim_tiempo AS
SELECT DISTINCT
    CAST(anio_grado AS INTEGER) AS anio_grado,
    CASE
        WHEN CAST(anio_grado AS INTEGER) <= 2019 THEN 'Pre-pandemia'
        WHEN CAST(anio_grado AS INTEGER) <= 2021 THEN 'Pandemia'
        ELSE 'Post-pandemia'
    END AS periodo
FROM stg_egresados;

CREATE TABLE dim_empleador AS
SELECT
    ROW_NUMBER() OVER (ORDER BY empleador) AS sk_empleador,
    empleador                              AS nombre,
    ANY_VALUE(sector)                      AS sector,
    ANY_VALUE(ambito)                      AS ambito
FROM stg_egresados
WHERE empleador <> ''
GROUP BY empleador;

CREATE TABLE dim_area AS
SELECT
    ROW_NUMBER() OVER (ORDER BY area) AS sk_area,
    area,
    -- La afinidad es tri-estado: conocida afin, conocida no afin, o
    -- desconocida. No se fuerza a booleano para no inventar certeza.
    ANY_VALUE(NULLIF(es_afin, '')) IS NOT NULL AS afinidad_conocida
FROM stg_egresados
GROUP BY area;

CREATE TABLE dim_fuente AS
SELECT
    ROW_NUMBER() OVER (ORDER BY fuente) AS sk_fuente,
    CASE WHEN fuente = '' THEN 'Sin fuente' ELSE fuente END AS fuente,
    ANY_VALUE(nivel_confianza)          AS nivel_confianza
FROM stg_egresados
GROUP BY fuente;

-- --- Hechos ----------------------------------------------------------------

CREATE TABLE fact_observacion_laboral AS
SELECT
    s.sk_egresado,
    CAST(s.anio_grado AS INTEGER) AS anio_grado,
    e.sk_empleador,
    a.sk_area,
    f.sk_fuente,
    s.estado_evidencia,
    s.nivel_confianza,
    s.sector,
    s.ambito,
    s.cargo,
    -- Medidas
    CASE WHEN s.estado_evidencia = 'Empleo verificado' THEN 1 ELSE 0 END
        AS tiene_evidencia_empleo,
    CASE WHEN s.es_afin = '' THEN NULL ELSE CAST(s.es_afin AS INTEGER) END
        AS es_afin,
    -- Tiempo de insercion: NO obtenible de fuentes publicas. Queda NULL a la
    -- espera de la encuesta. Se declara aqui para no rehacer el modelo luego.
    CAST(NULL AS INTEGER) AS meses_insercion
FROM stg_egresados s
LEFT JOIN dim_empleador e ON e.nombre = s.empleador
LEFT JOIN dim_area      a ON a.area   = s.area
LEFT JOIN dim_fuente    f ON f.fuente = CASE WHEN s.fuente = ''
                                             THEN 'Sin fuente' ELSE s.fuente END
WHERE s.estado_evidencia <> 'Segundo grado (duplicado)';
