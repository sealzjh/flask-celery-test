# -*- coding: utf-8 -*-

from core import celery_order

@celery_order.task()
def save_task_async(task_id, created = True):
    print "save_task_async: %s" % task_id

