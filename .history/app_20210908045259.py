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
#-------------------- Get Requests --------------------

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

@app.route('/tutor/<int:tutor_id>/appointments', methods=['GET'])
def get_appointments_tutor(tutor_id):
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

@app.route('/student/<int:student_id>/appointments', methods=['GET'])
def get_appointments_student(student_id):
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

#-------------------- POST Requests --------------------
#-------------------- PATCH Requests --------------------
@app.route("/appointments/edit/<int:appointment_id>", methods=['PATCH'])
def update_appointment(appointment_id):
    appointment = Appointments.query.filter(Appointments.id == appointment_id).one_or_none()
    if appointment is None:
         abort(404)
    else:
        try:
            body = request.get_json()
            confirmation = body.get('confirmation')
            if confirmation:
                appointment.confirmation = confirmation
            appointment.update()
            return jsonify({
                'success': True,
                'Appointment Confirmation': "Confirmed" if appointment.confirmation in (True, 't', 'True') else "Not Confirmed"
            })
        except:
            abort(422)



  
if __name__ == '__main__':
  app.run()
