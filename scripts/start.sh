#! /bin/bash

source env/env.sh

export PYTHONPATH=StatisticsMicroservice

yoyo apply --batch
uvicorn app.entrypoint.api:app_factory --factory --host 0.0.0.0 --port 8000

