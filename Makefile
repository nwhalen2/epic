# Makefile

VENV := Epic_Translation/epic_venv

install: requirements.txt
	python3 -m venv $(VENV)
	./${VENV}/bin/pip install -r requirements.txt

run: 
	./${VENV}/bin/python3 Epic_Translation/__main__.py

test: Epic_Translation/tests/test_translation.py
	./${VENV}/bin/python3 -m unittest Epic_Translation.tests.test_translation -v 

deactivate:
	rm -rf ${VENV}
