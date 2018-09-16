# encoding = utf-8
import logging
import os
from datetime import date

HOST = 'localhost'
PORT = 9999
DEBUG = False
PROJECT_NAME = 'flask-app-template'
LOG_FILE = os.path.join(os.path.dirname(__file__), 'logs',
                        '.'.join([PROJECT_NAME, date.today().isoformat(), 'log']))
logging.basicConfig(level=logging.INFO,
                    filename=LOG_FILE,
                    format='%(asctime)s - %(levelname)s - %(name)s - %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p')
