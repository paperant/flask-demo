# encoding = utf-8
from flask import Blueprint, request

api = Blueprint('api', __name__)


@api.route('/api', methods=['POST'])
def app_api():
    params = request.get_data()
    if params is None:
        return 'No params'
    else:
        return params
