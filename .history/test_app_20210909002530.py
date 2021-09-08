'''
Email: student@gmail.com
Password: St123456 

Email: manager@gmail.com 
Password:Ma123456 

Email: tutor@gmail.com 
Password:Ta123456 
'''

import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
import unittest
from app import app, db,create_app
from Database.models import *

# OAuth setup
AUTH0_DOMAIN = 'saramohammed.us.auth0.com'
ALGORITHMS = ['RS256']
API_AUDIENCE = 'VirtualTutor'

STUDENT_TOKEN = ''
MANAGER_TOKEN = ''
TUTOR_TOKEN=''

LOGIN_URL = 'https://saramohammed.us.auth0.com/authorize?audience=Virtual Tutor&response_type=token&client_id=27ccUc19Y6sfdyL2sMVRzWbnbH3VvKZd&redirect_uri=http://127.0.0.1:5000/'

class VirtualTutorTestCase(unittest.TestCase):
    """This class represents the Virtual Tutor test case"""

    def setUp(self):

        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "capstone_test"
        self.database_path = "postgres://{}/{}".format('localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)
    
        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()
    
    def tearDown(self):
        """Executed after reach test"""
        pass

    '''
    ** Tests will include at least….
        * One test for success behavior of each endpoint
        * One test for error behavior of each endpoint
✓
        Endpoints:
        - Get:
        - get_subjects
        - get_tutors_based_on_subject
        - get_appointments_tutor
        - get_appointments_student
        - Post:
        - create_tutor
        - create_student
        - create_appointment
        - Patch:
        - update_appointment
        - Delete:
        - delete_appointment
    '''
