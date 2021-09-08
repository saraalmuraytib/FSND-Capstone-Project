'''
* General Specifications *
** Models will include at least…
  * Two classes with primary keys at at least two attributes each
  * [Optional but encouraged] One-to-many or many-to-many relationships between classes
** Endpoints will include at least…
  * Two GET requests --> Get Subjects, Get Tutors based on selected Subject
  * One POST request --> 
  * One PATCH request --> 
  * One DELETE request --> 
** Roles will include at least…
  * Two roles with different permissions --> 
  * Permissions specified for all endpoints
** Tests will include at least….
  * One test for success behavior of each endpoint
  * One test for error behavior of each endpoint
  * At least two tests of RBAC for each role
'''

import os
from flask import Flask, request, abort, jsonify,render_template
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

#------------------------
from Database.models import *

  # create and configure the app
app = Flask(__name__)
CORS(app)
setup_db(app)
Migrate(app, db)

'''
  !! NOTE THIS WILL DROP ALL RECORDS AND START YOUR DB FROM SCRATCH
  !! NOTE THIS MUST BE UNCOMMENTED ON FIRST RUN
  !! Running this funciton will add one
  '''
  #db_drop_and_create_all()

# @app.route('/', methods=['GET'])
# def index(): 
#     return '<h1>Welcome to Virtual Tutor</h1>'
  
# ROUTES
'''
    GET /subject
        it should be a public endpoint
    returns status code 200 and json {"success": True, "subjects": subjects } 
'''
@app.route('/subjects')


if __name__ == '__main__':
  app.run()