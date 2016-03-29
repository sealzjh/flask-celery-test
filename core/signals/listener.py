# -*- encoding: utf8 -*-

from core import celery_default, celery_order
from core.signals import pre_save
from core.signals import post_save
from core.models.task import Task

def listen_task(sender, instance, created=True, **kwargs):
    task_id = instance.id
    print "listen_task: %s" % task_id

    if created:
        print "is created"

    celery_default.send_task('core.tasks.record.save_task_log', args=[task_id, created], queue='default')
    celery_order.send_task('core.tasks.order.save_task_async', args=[task_id, created], queue='order')

#注册的方法
#    from core.tasks.order import save_task_async
#    save_task_async.delay(task_id, created)
#    from core.tasks.record import save_task_log
#    save_task_log.delay(task_id, created)

post_save.connect(listen_task, Task)
