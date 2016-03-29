# -*- encoding: utf8 -*-

import os
import api.views
from core import app
import core.signals.listener

if __name__ == '__main__':
        app.run(host="0.0.0.0", port=6001, debug=True)
