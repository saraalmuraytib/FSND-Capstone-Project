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

#----------------------- ROUTES -----------------------

@app.route('/', methods=['GET'])
def index(): 
    return '<h1>Welcome to Virtual Tutor</h1>'
  
'''
    GET /subject
        it should be a public endpoint
    returns status code 200 and json {"success": True, "subjects": subjects } 
'''
@app.route('/subjects')
def get_subjects(): 
  subjects = Subject.query.all()

  if len(subjects) == 0:
    abort(404)

  return jsonify({
            'success': True,
            'Subjects': {subject.id: subject.name for subject in subjects}
        }) 

'''
  GET /subjects/<int:subject_id>/tutors 
    it should get tutors based on subject. 
  '''
@app.route('/subjects/<int:subject_id>/tutors', methods=['GET'])
def get_tutors_based_on_subject(subject_id):
     subject = Subject.query.filter(Subject.id == subject_id).one_or_none()
     if category is None:
         abort(404)

     else:
         tutors = Tutor.query.filter(
             Tutor.subject_id == str(subject_id)).all()
         return jsonify({
             'success': True,
             'Tutors': [tutor.format() for tutor in tutorsors],
             'total_Tutor': len(questions),
             'Subject': category.type
         })

  
if __name__ == '__main__':
  app.run()