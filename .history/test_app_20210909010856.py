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
from app import db,create_app
from Database.models import *

# OAuth setup
AUTH0_DOMAIN = 'saramohammed.us.auth0.com'
ALGORITHMS = ['RS256']
API_AUDIENCE = 'VirtualTutor'

STUDENT_TOKEN = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjUyWEpERzlORkhUUUg1NnMtR3NIaSJ9.eyJpc3MiOiJodHRwczovL3NhcmFtb2hhbW1lZC51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjEzOTJlNzg0ZmVjNmQwMDY4MmE4MGJiIiwiYXVkIjoiVmlydHVhbCBUdXRvciIsImlhdCI6MTYzMTEzNzQzMSwiZXhwIjoxNjMxMTQ0NjMxLCJhenAiOiIyN2NjVWMxOVk2c2ZkeUwyc01WUnpXYm5iSDNWdktaZCIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmRlbGV0ZV9hcHBvaW50bWVudCIsImdldDphcHBvaW50bWVudHNfc3R1ZGVudCIsImdldDpzdWJqZWN0cyIsImdldDp0dXRvcnNfYmFzZWRfb25fc3ViamVjdCIsInBvc3Q6Y3JlYXRlX2FwcG9pbnRtZW50Il19.D-hr-dfKJr_JWaStEhaGtbswDV9g6SemvTGWnECbbQf6-rhcegQwaXtTcBPF7O4sW_jcfql7i2l-ezFf5djLiuJKEhy1Ds1vsOFjLMPLhkA9RfvfITgSZZdqYWs-SBMhDAOARyV5bZMx28v2Ym7AeYhPEvkjOYlafWeeNz32CQLBxPQ7C9mJPTWG5NgfMIiRjLHKU_dojVQem-_ff-J1iTZ8YvLN1OuJdI4GUGIjPrZTibsmvXaSerNkVwIyK-3XbLQ5skYU2fAcVjNmLhSjuXN7wG-BahtBWUZoYo7foim7ACUh8-TVsyOq_dOLJD6HL7fnSj1B2hngglmFyK9wWA'
MANAGER_TOKEN = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjUyWEpERzlORkhUUUg1NnMtR3NIaSJ9.eyJpc3MiOiJodHRwczovL3NhcmFtb2hhbW1lZC51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjEzOTI3Nzg2MWJkMWUwMDY4MDIwNjBhIiwiYXVkIjoiVmlydHVhbCBUdXRvciIsImlhdCI6MTYzMTEzNzI2MiwiZXhwIjoxNjMxMTQ0NDYyLCJhenAiOiIyN2NjVWMxOVk2c2ZkeUwyc01WUnpXYm5iSDNWdktaZCIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmRlbGV0ZV9hcHBvaW50bWVudCIsImdldDphcHBvaW50bWVudHNfc3R1ZGVudCIsImdldDphcHBvaW50bWVudHNfdHV0b3IiLCJnZXQ6c3ViamVjdHMiLCJnZXQ6dHV0b3JzX2Jhc2VkX29uX3N1YmplY3QiLCJwYXRjaDp1cGRhdGVfYXBwb2ludG1lbnQiLCJwb3N0OmNyZWF0ZV9hcHBvaW50bWVudCIsInBvc3Q6Y3JlYXRlX3R1dG9yIl19.N9wi9LxHDg-KD5wWsEd1_mGJEhPSO3Lrs43AHaLjWIg1BIwqjpj9ImxgziNgeP3dM_xXdLD93YedStloRUaChEML6WAeC9l0Yc6P5AfCAqjBMIXuA42lhhTl2NrFk0-pyyUOXzR_jRQX_kHd08zxACugUNO3RBMnMEeHydObG3FqFOi0B7w9_v_0a7uYLAyQRTeFssNsO4zzCIGl4qZrVlRv5AiDAVNJqI7FNPwtRmbGymbCfEWe7CnsOKKVQAdlqHsBP0IYcA9dTF_Qu1rLonqCQc7r5kdtYzUTe8Ceq-QTTnaF5NvNchSDzHo_cRW63P7vOg4s2wOC10eL6GJGmQ'
TUTOR_TOKEN='eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjUyWEpERzlORkhUUUg1NnMtR3NIaSJ9.eyJpc3MiOiJodHRwczovL3NhcmFtb2hhbW1lZC51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjEzOTJlZDljYmQyNzAwMDY5ZjgzZWJhIiwiYXVkIjoiVmlydHVhbCBUdXRvciIsImlhdCI6MTYzMTEzNzUzMywiZXhwIjoxNjMxMTQ0NzMzLCJhenAiOiIyN2NjVWMxOVk2c2ZkeUwyc01WUnpXYm5iSDNWdktaZCIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmRlbGV0ZV9hcHBvaW50bWVudCIsImdldDphcHBvaW50bWVudHNfdHV0b3IiLCJnZXQ6c3ViamVjdHMiLCJnZXQ6dHV0b3JzX2Jhc2VkX29uX3N1YmplY3QiLCJwYXRjaDp1cGRhdGVfYXBwb2ludG1lbnQiXX0.n_UTu_QxDRz25e3-prPZeUyRBnS9nZFyuXktx70uirH4-ENWcNfDj5x5VmQBDA1hzN88izc2PS0vC74nPyXK7Np-nFkoYTTlhyttnbKHEVDRbdYjgvjOmHYy7QkpYzME90_cxh4hekcqzYDF6Amg2fr_rd38LAQ1_pZ1KuyOArO1pwYV4x3TtBQezmxeVxhXky11fLFF1AHhua_br0GLBb1NIkr8hjb4e8mqsl7DUm30xkzdUa64VlQl0SVqDBD0HQvFlcQ8s7j7kFX4nKovnGX6QI4Qc4gS3QjPAECewEtuAotuPtsQxJKp41RrWmvUqLvmjDMbBJPAjTf7V0zMgw'

LOGIN_URL = 'https://saramohammed.us.auth0.com/authorize?audience=Virtual Tutor&response_type=token&client_id=27ccUc19Y6sfdyL2sMVRzWbnbH3VvKZd&redirect_uri=http://127.0.0.1:5000/'

class VirtualTutorTestCase(unittest.TestCase):
    """This class represents the Virtual Tutor test case"""

    def setUp(self):

        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "capstone_test"
        self.database_path = "postgresql://{}/{}".format('localhost:5432', self.database_name)
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
    ** Tests will include at least???.
        * One test for success behavior of each endpoint
        * One test for error behavior of each endpoint
???
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
#___________________ get_subjects ____________________
    def test_get_subjects(self):
        res = self.client().get('/subjects')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['subject'])

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
