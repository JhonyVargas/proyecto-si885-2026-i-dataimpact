# ADR 003 — La afinidad formativa es tri-estado, no booleana

**Estado:** aceptada · **Fecha:** 2026-09-20

## Contexto

El campo de origen a veces declara empresa y cargo ("NTT DATA, Desarrollador
Frontend"), a veces solo la empresa ("Caja Tacna"). En el segundo caso no se
puede saber si la persona se desempeña en un área afín a Ingeniería de Sistemas:
una caja municipal emplea tanto desarrolladores como cajeros.

## Decisión

`es_afin` admite tres valores: `1` (afín), `0` (no afín) y `NULL` (desconocido).
El indicador de afinidad se calcula solo sobre los casos con cargo identificable,
y el denominador se reporta junto al porcentaje.

## Alternativas descartadas

- **Forzar a `0`.** Subestima la afinidad y castiga a egresados sobre los que
  simplemente no hay dato.
- **Forzar a `1`.** Infla el indicador, que es justamente la cifra que la Escuela
  usaría para defender la pertinencia de su plan de estudios.
- **Inferir el cargo desde el sector.** Inventar datos.

## Consecuencias

- El denominador de afinidad original (12) es mucho menor que el de empleo verificado
  (35). La cifra es menos vistosa y más defendible.
- Hay un test que impide que una futura refactorización colapse el `NULL` a
  `False`.

Actualización 2026-10-10: el denominador se corrige a 11 al retirar la inferencia
de docencia desde un empleador educativo sin cargo declarado. Ver ADR 004.
