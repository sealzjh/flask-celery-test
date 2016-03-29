# -*- encoding: utf8 -*-

from flask import request
from core import app
from core import db
from core.models.task import Task

@app.route("/v1_0/test/")
def test():
#    task = Task.query.get(1)
#    task.allow_accept_time = 111
#    print task.allow_accept_time
    
    task = Task(**{"order_value": 33, "supplier_id": 586})
    task.save()
    return "ok"
