'''
* General Specifications *
** Models will include at least…
  ✓ Two classes with primary keys at at least two attributes each 
  ✓ [Optional but encouraged] One-to-many or many-to-many relationships between classes
** Endpoints will include at least…
  ✓ Two GET requests 
  ✓ One POST request 
  ✓ One PATCH request
  ✓ One DELETE request
** Roles will include at least…
  ✓ Two roles with different permissions 
  ✓ Permissions specified for all endpoints 
** Tests will include at least….
  * One test for success behavior of each endpoint
  * One test for error behavior of each endpoint
  * At least two tests of RBAC for each role
'''

import os
from flask import Flask, request, abort, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from datetime import datetime

# ------------------------
from Database.models import *
from auth.auth import AuthError, requires_auth
def create_app():
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)
    CORS(app)
    Migrate(app, db)


  '''
    !! NOTE THIS WILL DROP ALL RECORDS AND START YOUR DB FROM SCRATCH
    !! NOTE THIS MUST BE UNCOMMENTED ON FIRST RUN
    !! Running this funciton will add one
    '''
  # db_drop_and_create_all()

  # ----------------------- ROUTES -----------------------
  # -------------------- Get Requests --------------------


  @app.route('/', methods=['GET'])
  def index():
      return '<h1>Welcome to Virtual Tutor</h1>'

  #  It should be a public endpoint
  @app.route('/subjects')
  def get_subjects():
      subjects = Subject.query.all()

      if len(subjects) == 0:
          abort(404)

      return jsonify({
          'success': True,
          'Subjects': {subject.id: subject.name for subject in subjects}
      })

  #  It should be a public endpoint
  @app.route('/subjects/<int:subject_id>/tutors', methods=['GET'])
  def get_tutors_based_on_subject(subject_id):
      subject = Subject.query.filter(Subject.id == subject_id).one_or_none()
      if subject is None:
          abort(404)

      else:
          tutors = Tutor.query.filter(Tutor.subject_id == str(subject_id)).all()

          return jsonify({
              'success': True,
              'Tutors': [tutor.format() for tutor in tutors],
              'total_Tutor': len(tutors),
              'Subject': subject.name
          })

  #  It should require the 'get:appointments_tutor' permission
  @app.route('/tutor/<int:tutor_id>/appointments', methods=['GET'])
  @requires_auth('get:appointments_tutor')
  def get_appointments_tutor(tutor_id,payload):
      tutor = Tutor.query.filter(Tutor.id == tutor_id).one_or_none()

      if tutor is None:
          abort(404)
      else:
          appointments = Appointments.query.filter(
              Appointments.tutor_id == str(tutor_id)).all()
          if len(appointments) == 0:
              return jsonify({
                  'success': True,
                  'Total Appointments': len(appointments)
              })
          else:
              upcoming_appointments = []
              for appointment in tutor.upcoming_appointments:
                  student = Student.query.get(appointment.student_id)

                  upcoming_appointments.append({
                      'Appointment ID': appointment.id,
                      "Student ID": appointment.student_id,
                      "Student name": student.name,
                      'Start Time': appointment.start_time,
                      'Duration in minutes': appointment.duration,
                      'confirmation': "Confirmed" if appointment.confirmation in (True, 't', 'True') else "Not Confirmed"
                  })
              return jsonify({
                  'success': True,
                  'Total Appointments': len(appointments),
                  'Total of Upcoming Appointments': tutor.num_upcoming_appointments,
                  'Upcoming Appointments': upcoming_appointments
              })

  #  It should require the 'get:appointments_student' permission
  @app.route('/student/<int:student_id>/appointments', methods=['GET'])
  @requires_auth('get:appointments_student')
  def get_appointments_student(student_id,payload):
      student = Student.query.filter(Student.id == student_id).one_or_none()

      if student is None:
          abort(404)
      else:
          appointments = Appointments.query.filter(
              Appointments.student_id == str(student_id)).all()
          if len(appointments) == 0:
              return jsonify({
                  'success': True,
                  'Total Appointments': len(appointments)
              })
          else:
              upcoming_appointments = []
              for appointment in student.upcoming_appointments:
                  tutor = Tutor.query.get(appointment.tutor_id)

                  upcoming_appointments.append({
                      'Appointment ID': appointment.id,
                      "Tutor ID": appointment.student_id,
                      "Tutor name": tutor.name,
                      'Start Time': appointment.start_time,
                      'Duration in minutes': appointment.duration,
                      'confirmation': "Confirmed" if appointment.confirmation in (True, 't', 'True') else "Not Confirmed"
                  })
              return jsonify({
                  'success': True,
                  'Total Appointments': len(appointments),
                  'Total of Upcoming Appointments': student.num_upcoming_appointments,
                  'Upcoming Appointments': upcoming_appointments
              })

  # -------------------- POST Requests ---------------------
  #  It should require the 'post:create_tutor' permission
  @app.route('/tutor', methods=['POST'])
  @requires_auth('post:create_tutor')
  def create_tutor():
      body = request.get_json()
      name = body.get('name')
      intro = body.get('intro')
      subject_id = body.get('subject_id')
      availableTime=body.get('availableTime')
      # Check if the subject exist or not
      subject = Subject.query.filter(Subject.id == subject_id).one_or_none()
    
      if subject is None:
        abort(404)
      else:
        try:
          new_tutor = Tutor(name=name, 
          intro=intro,subject_id=subject_id,availableTime=availableTime)
          new_tutor.insert()
          return jsonify({
              'success': True,
              'Appointment': new_tutor.format()
          })
        except:
          abort(422)


  @app.route('/student', methods=['POST'])
  def create_student():

      body = request.get_json()
      name = body.get('name')
      email = body.get('email')
      age = body.get('age')
      grade=body.get('grade')
    
      try:
          new_student = Student(name=name, 
          email=email,age=age,grade=grade)
          new_student.insert()
          return jsonify({
              'success': True,
              'Appointment': new_student.format()
          })
      except:
          abort(422)

  #  It should require the 'post:create_appointment' permission
  @app.route("/appointments/create/<int:student_id>", methods=['POST'])
  @requires_auth('post:create_appointment')
  def create_appointment(student_id,payload):
      student = Student.query.filter(Student.id == student_id).one_or_none()
      if student is None:
          abort(404)
      else:
          # Fetch the request body
          body = request.get_json()

          # Get start_time, duration, and tutor_id to create the appointment
          start_time = body.get('start_time')
          duration = body.get('duration')
          tutor_id = body.get('tutor_id')

          # Check if the tutor exist or not
          tutor = Tutor.query.filter(Tutor.id == tutor_id).one_or_none()
          if tutor is None:
              abort(404)
          else:
              try:
                  new_appointment = Appointments(
                      start_time=(datetime.strptime(
                          start_time, '%d/%m/%y %H:%M:%S')),
                      duration=duration, tutor_id=tutor_id, student_id=student_id)

                  new_appointment.insert()

                  return jsonify({
                      'success': True,
                      'Appointment': new_appointment.format()
                  })
              except:
                  abort(422)

  # -------------------- PATCH Requests --------------------
  #  It should require the 'patch:update_appointment' permission
  @app.route("/appointments/edit/<int:appointment_id>", methods=['PATCH'])
  @requires_auth('patch:update_appointment')
  def update_appointment(appointment_id,payload):
      appointment = Appointments.query.filter(
          Appointments.id == appointment_id).one_or_none()
      if appointment is None:
          abort(404)
      else:
          try:
              body = request.get_json()
              confirmation = body.get('confirmation')
              appointment.confirmation = confirmation
              appointment.update()
              return jsonify({
                  'success': True,
                  'Appointment Confirmation': "Confirmed" if appointment.confirmation in (True, 't', 'True') else "Not Confirmed"
              })
          except:
              abort(422)

  # -------------------- DELETE Requests --------------------
  #  It should require the 'delete:delete_appointment' permission
  @app.route("/appointments/delete/<int:appointment_id>", methods=['DELETE'])
  @requires_auth('delete:delete_appointment')
  def delete_appointment(appointment_id,payload):
      appointment = Appointments.query.filter(Appointments.id == appointment_id).one_or_none()
      if appointment is None:
          abort(404)
      else:
          try:
              appointment.delete()
              return jsonify({
                  'success': True,
                  'delete': appointment_id
              })
          except:
              abort(422)

  # -------------------- Error Handling --------------------
  '''
  Error handling for unprocessable entity
  '''
  @app.errorhandler(422)
  def unprocessable(error):
      return jsonify({
          "success": False,
          "error": 422,
          "message": "unprocessable"
      }), 422


  '''
  Error handler for 404
      error handler should conform to general task above
  '''
  @app.errorhandler(404)
  def not_found(error):
      return jsonify({
          "success": False,
          "error": 404,
          "message": "resource not found"
      }), 404

  '''
  Error handler for AuthError
      error handler should conform to general task above
  '''
  @app.errorhandler(AuthError)
  def handle_auth_error(error):
      return jsonify({
          "success": False,
          "error": error.status_code,
          'message': error.error
      }), 401


if __name__ == '__main__':
    create_app().run()
