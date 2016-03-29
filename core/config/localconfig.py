# -*- encoding: utf8 -*-

import sys
import os
from core.config.config import Config

root_path = os.path.dirname(os.path.abspath(__file__))+'/../../'

class LocalConfig(Config):
    DEBUG = True
    TESTING = False

    SQLALCHEMY_ECHO = False

    SHOULD_OAUTH = False
    SHOULD_SEND_NOTIFICATIONS = False
    SHOULD_PUSH_NOTIFICATION = False

    SQLALCHEMY_DATABASE_URI = 'mysql://root:123456@127.0.0.1/test'

config = LocalConfig()
