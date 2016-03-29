# -*- encoding: utf8 -*-

from kombu import Exchange, Queue

import os
root_path = os.path.dirname(os.path.abspath(__file__)) + '/../../'

class Config:
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True

    REDIS_DATABASE_INDEX = 0


    TEMPLATE_FOLDER = root_path + 'dada/templates'
    STATIC_FOLDER = root_path + 'dada/static'

    SENTRY_DSN = ''

    # Celery config.
    CELERY_DEFAULT_BROKER_URL = 'redis://127.0.0.1:6379/1'
    CELERY_DEFAULT_RESULT_BACKEND = 'redis://127.0.0.1:6379/1'
    CELERY_ORDER_BROKER_URL = 'redis://127.0.0.1:6379/2'
    CELERY_ORDER_RESULT_BACKEND = 'redis://127.0.0.1:6379/2'
    CELERYD_CONCURRENCY = 16
    CELERY_TIMEZONE = 'Asia/Shanghai'
    CELERY_ENABLE_UTC = True
    CELERY_TASK_LOG_LEVEL = 'INFO'
    CELERY_TASK_SERIALIZER = 'json'

    CELERY_ACCEPT_CONTENT = ['json', ]
    CELERY_RESULT_SERIALIZER = 'json'
    CELERY_IGNORE_RESULT = True
    CELERY_STORE_ERRORS_EVEN_IF_IGNORED = True
    CELERY_IMPORTS = (
                       'core.tasks.record',
                       'core.tasks.order'
                      )

    CELERY_DEFAULT_QUEUE = 'default'
    CELERY_QUEUES = (
        Queue('default', Exchange('default'), routing_key='default'),
        Queue('order', Exchange('order'), routing_key='order'),
    )

    CELERY_ROUTES = {
        'core.tasks.record.save_task_log': {
        'queue': 'default',
        'routing_key': 'default',
        },
        'core.tasks.order.save_task_async': {
        'queue': 'order',
        'routing_key': 'order',
        },
    }

#    CELERY_QUEUES = {
#        "default": {"exchange": "default"},
#        "order": {"exchange": "order"},
#    }
#
#    CELERY_ROUTES = {
#        'core.tasks.record.save_task_log': {
#            'queue': 'default',
#        },
#        'core.tasks.order.save_task_async': {
#            'queue': 'order',
#        },
#    }

    CELERY_DEFAULT_EXCHANGE = 'default'
    CELERY_DEFAULT_ROUTING_KEY = 'default'
    CELERY_DEFAULT_EXCHANGE_TYPE = 'direct'
