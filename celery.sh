#!/bin/bash

#start:
celery -A core.celery_default worker -Q default --loglevel=info
celery -A core.celery_order worker -Q order --loglevel=info

#args start
#celery multi $1 1 -E -A core.celery_default -l info -Q default -c 1 --logfile=celery_default.log --pidfile=celery_default.pid
