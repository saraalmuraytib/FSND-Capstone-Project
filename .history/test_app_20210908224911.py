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
from app import app, db
from Database.models import *

# OAuth setup
AUTH0_DOMAIN = 'saramohammed.us.auth0.com'
ALGORITHMS = ['RS256']
API_AUDIENCE = 'VirtualTutor'

STUDENT_TOKEN = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjkydjQ2dGg2Z1JGUUVjN2swQWZHdCJ9.eyJpc3MiOiJodHRwczovL2ZzbmQtY2xhc3MudXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYxMzJmODJjM2YyMzYyMDA2OTRlNDk5OSIsImF1ZCI6ImRldmVsb3BlciIsImlhdCI6MTYzMTExNDAxMywiZXhwIjoxNjMxMTIxMjEzLCJhenAiOiJjZVEyUVhjdWw4NWxxdnI1OWVadmFhTDBuRExFNVY0SiIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmludGVydmlldyIsImdldDppbnRlcnZpZXciLCJnZXQ6aW50ZXJ2aWV3cyIsImdldDpwZXQiLCJwYXRjaDppbnRlcnZpZXciLCJwb3N0OmludGVydmlldyJdfQ.a0C_YYxAxsiN6umnzHANSDuM41OAWmEnDuTZeNJcxW48-ClTSR87K762VeTej7MrQks2mUGUToC1Ld82scq2MpgedBOhFQdo3KSw30922vAaLi8eR9lLAaHCcjcMxo_XZUyFpPk4apnDfON8BsaZNhrOOSVvI423AOIOtg4g4BMdsa2DacU04toxyWcohnyusYI65F_fpwRveGH_eeDyuxHA8eu1elma07vbZudtNlgspVAGUNowow332ZCYMKAbdXd4b4Wa5VizkOhD8vpkKGpMJKJdTyqTpN9VuUsmwFEjOR5yqlLCoPwfKxt8PMm-9tROBhKudSQcyjQFS4Ub-w&'
MANAGER_TOKEN = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjkydjQ2dGg2Z1JGUUVjN2swQWZHdCJ9.eyJpc3MiOiJodHRwczovL2ZzbmQtY2xhc3MudXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYxMzJmN2VhN2I4ZTNhMDA2OWZlNTY2NiIsImF1ZCI6ImRldmVsb3BlciIsImlhdCI6MTYzMTExNDIwMywiZXhwIjoxNjMxMTIxNDAzLCJhenAiOiJjZVEyUVhjdWw4NWxxdnI1OWVadmFhTDBuRExFNVY0SiIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmJyZWVkIiwiZGVsZXRlOmludGVydmlldyIsImRlbGV0ZTpwZXQiLCJkZWxldGU6c3BlY2llIiwiZ2V0OmFsbC1hZG9wdGVkLXBldHMiLCJnZXQ6YWxsLWJyZWVkcyIsImdldDphbGwtSW50ZXJ2aWV3c1x0IiwiZ2V0OmFsbC1zcGVjaWVzIiwiZ2V0OmludGVydmlldyIsImdldDppbnRlcnZpZXdzIiwiZ2V0OnBldCIsImdldDpwZXRzLWRldGFpbCIsInBhdGNoOmJyZWVkIiwicGF0Y2g6aW50ZXJ2aWV3IiwicGF0Y2g6cGV0IiwicGF0Y2g6c3BlY2llIiwicG9zdDpicmVlZCIsInBvc3Q6aW50ZXJ2aWV3IiwicG9zdDpwZXQiLCJwb3N0OnNwZWNpZSJdfQ.n603tx4BLGaBo4gKl57CK7fWEFW4bCe3ex8dAp2QNwqXBBEPTd70HempaLFMB06FS94pxobV0HOvEqzbmOOwUvIdEZ20Ws6mrV1yOYg3o8KbroQEiIk94-llOwFmNlDFrUqvlWzjLIy7maBKP8GaXGVawSkq2mvBoVew-4F9VAL0FbGaWy7aGgJD1cZ2aFr5ZpQxgEl_xjhR0oCSp07ZO1J_VpFoJnHWGPdu-cZOzDAFCKvSkus-0zy7xX9Stu70SBeBcI57NXutb8hVCFCZvjJz0mEoSUuOTpHRf7m2vZA9TtxfoLBTMcdl4G7HhpDRBQhwSkEr9Mi3OcirHknGUA'
TUTOR_TOKEN=''

LOGIN_URL = 'https://saramohammed.us.auth0.com/authorize?audience=Virtual Tutor&response_type=token&client_id=27ccUc19Y6sfdyL2sMVRzWbnbH3VvKZd&redirect_uri=http://127.0.0.1:5000/'

class VurtualTutorTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "trivia_test"
        self.database_path = "postgres://{}/{}".format('localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

        self.new_question = {
            'question': 'test question',
            'answer': 'test answer',
            'difficulty': 3,
            'category': 3
        }
    

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()
    
    def tearDown(self):
        """Executed after reach test"""
        pass
