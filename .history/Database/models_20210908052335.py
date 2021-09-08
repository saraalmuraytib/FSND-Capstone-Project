from datetime import datetime
import os
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
DB_HOST = os.getenv('DB_HOST', '127.0.0.1:5432')  
DB_NAME = os.getenv('DB_NAME', 'capstone')  
DB_PATH = 'postgres://{}/{}'.format(DB_HOST, DB_NAME)

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''
def setup_db(app, database_path=DB_PATH):
    app.config["SQLALCHEMY_DATABASE_URI"] = DB_PATH
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)

'''
    drops the database tables and starts fresh
'''
def db_drop_and_create_all():
    db.drop_all()
    db.create_all()
#----------------------------------------------------------------------------#
class Subject(db.Model):
    __tablename__ = 'subject'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

    #----------------------- Relationship -----------------------------------
    tutor = db.relationship('Tutor', backref="subject", lazy=True)

    def __repr__(self):
        return f'<Subject ID: {self.id}, Subject Name:{self.name}>'

    def insert(self):
        db.session.add(self)
        db.session.commit()
    def delete(self):
        db.session.delete(self)
        db.session.commit()
    def update(self):
        db.session.commit()
#----------------------------------------------------------------------------#
class Tutor(db.Model):
    __tablename__ = 'tutor'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    intro = db.Column(db.String, nullable=False)
    availableTime= db.Column(db.ARRAY(db.String()))

    #----------------------- Relationship -----------------------------------
    subject_id = db.Column(db.Integer,db.ForeignKey('subject.id'),nullable=False)
    appointments = db.relationship('Appointments', backref="tutor", lazy=True)


    def __repr__(self):
        return f'<Tutor ID: {self.id}, Tutor Name:{self.name}, Tutor introduction:{self.intro}>'

    @property 
    def upcoming_appointments(self):
      upcoming_appointments = [appointment for appointment in self.appointments if appointment.start_time > datetime.now()] 
      return upcoming_appointments
    
    @property
    def num_upcoming_appointments(self):
      return len(self.upcoming_appointments)

    def format(self):
        return {
            'Id': self.id,
            'Name': self.name,
            'Introduction': self.intro,
            'Available Time': [available for available in self.availableTime]
        }

    def insert(self):
        db.session.add(self)
        db.session.commit()
    def delete(self):
        db.session.delete(self)
        db.session.commit()
    def update(self):
        db.session.commit()
#----------------------------------------------------------------------------#

class Appointments(db.Model):
    __tablename__ = 'appointments'

    id = db.Column(db.Integer, primary_key=True)
    start_time= db.Column(db.DateTime, nullable=False)
    duration=db.Column(db.Integer)
    confirmation = db.Column(db.Boolean)
    #----------------------- Relationship -----------------------------------
    tutor_id = db.Column(db.Integer,db.ForeignKey('tutor.id'),nullable=False)
    student_id = db.Column(db.Integer,db.ForeignKey('student.id'),nullable=False)

    def format(self):
        return {
            'Id': self.id,
            'Start Time': self.start_time,
            'Duration': self.duration,
            'confirmation': self.confirmation
        }
        
    def insert(self):
        db.session.add(self)
        db.session.commit()
    def delete(self):
        db.session.delete(self)
        db.session.commit()
    def update(self):
        db.session.commit()

 #----------------------------------------------------------------------------#

class Student(db.Model):
    __tablename__ = 'student'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String)
    age = db.Column(db.Integer)
    grade= db.Column(db.String)

    #----------------------- Relationship -----------------------------------
    appointments = db.relationship('Appointments', backref="student", lazy=True)

    @property 
    def upcoming_appointments(self):
      upcoming_appointments = [appointment for appointment in self.appointments if appointment.start_time > datetime.now()] 
      return upcoming_appointments
    
    @property
    def num_upcoming_appointments(self):
      return len(self.upcoming_appointments)
    def insert(self):
        db.session.add(self)
        db.session.commit()
    def delete(self):
        db.session.delete(self)
        db.session.commit()
    def update(self):
        db.session.commit()


    
