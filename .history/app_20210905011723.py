'''
* General Specifications *
** Models will include at least…
  * Two classes with primary keys at at least two attributes each
  * [Optional but encouraged] One-to-many or many-to-many relationships between classes
** Endpoints will include at least…
  * Two GET requests
  * One POST request
  * One PATCH request
  * One DELETE request
** Roles will include at least…
  * Two roles with different permissions
  * Permissions specified for all endpoints
** Tests will include at least….
  * One test for success behavior of each endpoint
  * One test for error behavior of each endpoint
  * At least two tests of RBAC for each role
'''

import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

#------------------------
from Database.models import *


def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  CORS(app)
  setup_db(app)
  return app

APP = create_app()

if __name__ == '__main__':
    APP.run(host='0.0.0.0', port=8080, debug=True)