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
    __tablename__ = 'Subject'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    tutor = db.relationship('Tutor', backref="subject", lazy=True)

    def __repr__(self):
        return f'<Subject ID: {self.id}, Subject Name:{self.name}>'
#----------------------------------------------------------------------------#
class Tutor(db.Model):
    __tablename__ = 'Tutor'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    intro = db.Column(db.String)
    #availableHours= db.Column()

    subject_id = db.Column(db.Integer,db.ForeignKey('Subject.id'),nullable=False)
    appointments = db.relationship('Appointments', backref="tutor", lazy=True)


    def __repr__(self):
        return f'<Tutor ID: {self.id}, Tutor Name:{self.name}, Tutor introduction:{self.intro}>'
#----------------------------------------------------------------------------#

class Appointments(db.Model):
    __tablename__ = 'Appointments'

    id = db.Column(db.Integer, primary_key=True)
    
    student_id = db.Column(db.Integer,db.ForeignKey('Student.id'),nullable=False)
    tutor_id = db.Column(db.Integer,db.ForeignKey('Tutor.id'),nullable=False)


 #----------------------------------------------------------------------------#
class Student(db.Model):
    __tablename__ = 'Student'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    appointments = db.relationship('Appointments', backref="student", lazy=True)



    