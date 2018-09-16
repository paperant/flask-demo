# encoding = utf-8
import logging
from flask import Flask, jsonify
from .view import view
from .api import api

app = Flask(__name__)
LOG = logging.getLogger(__name__)


@app.errorhandler(500)
def internal_error(e):
    LOG.exception("An internal error occurred. ")
    return jsonify({'status': 1, 'msg': 'Internal error.'})


app.register_blueprint(view)
app.register_blueprint(api)
