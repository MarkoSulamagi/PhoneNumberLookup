#!/bin/bash

# NOTICE
# If you change this file then you need to re-build docker image

echo "Starting Gunicorn"
exec gunicorn app:app --log-config /logging.conf --enable-stdio-inheritance --bind 0.0.0.0:8000 --workers 2 --reload -k gevent --timeout=300