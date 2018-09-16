import logging

from flask import Blueprint

from .constants import HELLO_WORLD

view = Blueprint('view', __name__)

LOG = logging.getLogger(__name__)


@view.route('/')
def hello_world():
    LOG.info("mapping for hello world. ")
    return HELLO_WORLD


@view.route('/error', methods=['GET'])
def server_error():
    raise Exception('This is an internal error.')
