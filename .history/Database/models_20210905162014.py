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
    db.create_all()

#----------------------------------------------------------------------------#
class Subject(db.Model):
    __tablename__ = 'Subject'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    tutor = db.relationship('Tutor', backref="subject", lazy=True)

#----------------------------------------------------------------------------#
class Tutor(db.Model):
    __tablename__ = 'Tutor'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    intro = db.Column(db.String)
    availableHours= db.Column()

    subject_id = db.Column(db.Integer,db.ForeignKey('Subject.id'),nullable=False)
#----------------------------------------------------------------------------#
class Student(db.Model):
    __tablename__ = 'Student'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)


#----------------------------------------------------------------------------#
class Appointments(db.Model):
    __tablename__ = 'Appointments'

    id = db.Column(db.Integer, primary_key=True)

    