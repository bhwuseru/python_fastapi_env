#!/bin/bash

if [ ! -d "$PROJECT_NAME" ]; then
	CURRENT_PATH=$(pwd)
	mkdir "$PROJECT_NAME"
	chmod 777  "$PROJECT_NAME"
	cd "$PROJECT_NAME"
	python3 -m venv venv
	source venv/bin/activate
	pip install pip --upgrade
	pip3 install fastapi
	pip3 install "uvicorn[standard]"
fi