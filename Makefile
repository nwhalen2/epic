# Makefile

VENV := epic_venv

activate: requirements.txt
	python3 -m venv $(VENV)
	./${VENV}/bin/pip install -r requirements.txt

run: epic_venv/bin/activate
	./${VENV}/bin/python3 Epic_Translation/src/translation/translation.py

deactivate:
	rm -rf ${VENV}
