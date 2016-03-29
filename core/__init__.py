# -*- encoding: utf8 -*-

from flask import Flask
from core.config.localconfig import config
from flask.ext.sqlalchemy import  SQLAlchemy
from celery import Celery

def createApp():
    app = Flask(__name__, template_folder=config.TEMPLATE_FOLDER, static_folder=config.STATIC_FOLDER)
    app.config.from_object(config)
    app.template_folder = app.config['TEMPLATE_FOLDER']
    app.static_folder = app.config['STATIC_FOLDER']
    return app

app = createApp()

db = SQLAlchemy(app)

def createCelery(main, app, backend_url,broker_url):
    celery = Celery(main, backend = backend_url, broker=broker_url)
    celery.conf.update(app.config)

    TaskBase = celery.Task

    class ContextTask(TaskBase):
        abstract = True

        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)
    celery.Task = ContextTask
    return celery

celery_default = createCelery('default', app, app.config['CELERY_DEFAULT_RESULT_BACKEND'], app.config['CELERY_DEFAULT_BROKER_URL'])
celery_order = createCelery('order', app, app.config['CELERY_ORDER_RESULT_BACKEND'], app.config['CELERY_ORDER_BROKER_URL'])

