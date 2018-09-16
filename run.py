# encoding = utf-8
import logging

from app import app as flask_app
from config import HOST, PORT, DEBUG

LOG = logging.getLogger(__name__)
LOG.warning(" -*-*-*-*- application start -*-*-*-*- ")


def main():
    flask_app.run(host=HOST, port=PORT, debug=DEBUG)


if __name__ == '__main__':
    main()
