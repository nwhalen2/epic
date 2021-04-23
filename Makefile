# Makefile

VENV := epic_venv

activate: requirements.txt
	python3 -m venv $(VENV)
	./${VENV}/bin/pip install -r requirements.txt

run: epic_venv/bin/activate
	./${VENV}/bin/python3 Epic_Translation/src/translation/__init__.py

test: Epic_Translation/tests/test_translation.py
	./${VENV}/bin/python3 -m unittest Epic_Translation.tests.test_translation 

deactivate:
	rm -rf ${VENV}
