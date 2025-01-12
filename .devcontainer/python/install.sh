#!/bin/bash

if [ ! -d "$PROJECT_NAME" ]; then
	CURRENT_PATH=$(pwd)
	mkdir "${PROJECT_NAME}"
	mkdir "${PROJECT_NAME}/templates"
	touch "${PROJECT_NAME}/templates/index.html"
	cp '/var/www/html/main.py' "/var/www/html/${PROJECT_NAME}"
	cp '/var/www/html/start_app.sh' "/var/www/html/${PROJECT_NAME}"

	chmod 777  "$PROJECT_NAME"
	cd "$PROJECT_NAME"
	python3 -m venv venv
	source "/var/www/html/${PROJECT_NAME}/venv/bin/activate"
	pip install pip --upgrade
	pip install fastapi "uvicorn[standard]" jinja2 python-multipart
fi