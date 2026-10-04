# ADR 002 — Reportar cobertura de información, no tasa de empleabilidad

**Estado:** aceptada · **Fecha:** 2026-09-20

## Contexto

De 139 egresados del marco censal, 35 tienen empleo verificable en fuentes
públicas. La lectura tentadora es "25.2 % de empleabilidad". Es falsa: los 104
restantes no son desempleados, son casos sin información.

Las fuentes públicas no permiten distinguir "no trabaja" de "no publica".

## Decisión

El indicador se nombra **cobertura de información** en todo el proyecto: código,
tablero e informes. La tasa de empleabilidad se declara **no estimable** con las
fuentes disponibles.

La advertencia viaja dentro del tablero, no solo en el informe, porque el
tablero circula solo.

## Consecuencias

- El proyecto no puede responder "¿cuántos egresados trabajan?". Es una
  limitación de los datos, no del diseño.
- La cobertura resulta ser un indicador valioso por sí mismo: mide qué tan bien
  la Escuela conoce a sus egresados, y un 75 % de invisibilidad es accionable
  para el seguimiento y la acreditación.
- La encuesta directa deja de ser un complemento y pasa a ser el único camino
  hacia la empleabilidad real y el tiempo de inserción.
