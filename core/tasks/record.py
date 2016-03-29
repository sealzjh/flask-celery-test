# -*- coding: utf-8 -*-

from core import celery_default

@celery_default.task()
def save_task_log(task_id, created = True):
    print "save_task_log:%s" % task_id

