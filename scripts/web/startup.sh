#!/usr/bin/env bash

#exec python src/main.py
exec uvicorn src.main_temp:create_app --host=$BIND_IP --port=$BIND_PORT

