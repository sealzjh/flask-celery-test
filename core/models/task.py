# -*- coding: utf8 -*-

from core import db
from core.models.base import Model

class Task(Model):
    __tablename__ = 'task'
    __table_args__ = {"mysql_engine": "InnoDB", "mysql_charset": "utf8"}

    id = db.Column(db.BigInteger, primary_key=True, nullable=False)
    order_id = db.Column(db.Integer, default=0)
    allow_accept_time = db.Column(db.Integer, default=0)

