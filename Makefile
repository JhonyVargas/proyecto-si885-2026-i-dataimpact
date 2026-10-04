.PHONY: all install pipeline test limpiar

all: pipeline

install:
	python -m pip install -r requirements.txt

pipeline:
	PYTHONPATH=src python -m empleabilidad.pipeline

test:
	PYTHONPATH=src python -m pytest tests -q

limpiar:
	rm -rf data/marts dashboard/datos.json
