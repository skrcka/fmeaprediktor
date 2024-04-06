#!/bin/bash
set -ex

poetry install
poetry run python generate_api.py
poetry run uvicorn main:app --reload
