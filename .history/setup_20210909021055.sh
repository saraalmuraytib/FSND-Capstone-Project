# OAuth setup
export AUTH0_DOMAIN = 'saramohammed.us.auth0.com'
export ALGORITHMS = ['RS256']
export API_AUDIENCE = 'Virtual Tutor'

# JWT for student,manager,tutor
STUDENT_TOKEN = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjUyWEpERzlORkhUUUg1NnMtR3NIaSJ9.eyJpc3MiOiJodHRwczovL3NhcmFtb2hhbW1lZC51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjEzOTJlNzg0ZmVjNmQwMDY4MmE4MGJiIiwiYXVkIjoiVmlydHVhbCBUdXRvciIsImlhdCI6MTYzMTEzNzQzMSwiZXhwIjoxNjMxMTQ0NjMxLCJhenAiOiIyN2NjVWMxOVk2c2ZkeUwyc01WUnpXYm5iSDNWdktaZCIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmRlbGV0ZV9hcHBvaW50bWVudCIsImdldDphcHBvaW50bWVudHNfc3R1ZGVudCIsImdldDpzdWJqZWN0cyIsImdldDp0dXRvcnNfYmFzZWRfb25fc3ViamVjdCIsInBvc3Q6Y3JlYXRlX2FwcG9pbnRtZW50Il19.D-hr-dfKJr_JWaStEhaGtbswDV9g6SemvTGWnECbbQf6-rhcegQwaXtTcBPF7O4sW_jcfql7i2l-ezFf5djLiuJKEhy1Ds1vsOFjLMPLhkA9RfvfITgSZZdqYWs-SBMhDAOARyV5bZMx28v2Ym7AeYhPEvkjOYlafWeeNz32CQLBxPQ7C9mJPTWG5NgfMIiRjLHKU_dojVQem-_ff-J1iTZ8YvLN1OuJdI4GUGIjPrZTibsmvXaSerNkVwIyK-3XbLQ5skYU2fAcVjNmLhSjuXN7wG-BahtBWUZoYo7foim7ACUh8-TVsyOq_dOLJD6HL7fnSj1B2hngglmFyK9wWA'
MANAGER_TOKEN = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjUyWEpERzlORkhUUUg1NnMtR3NIaSJ9.eyJpc3MiOiJodHRwczovL3NhcmFtb2hhbW1lZC51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjEzOTI3Nzg2MWJkMWUwMDY4MDIwNjBhIiwiYXVkIjoiVmlydHVhbCBUdXRvciIsImlhdCI6MTYzMTEzNzI2MiwiZXhwIjoxNjMxMTQ0NDYyLCJhenAiOiIyN2NjVWMxOVk2c2ZkeUwyc01WUnpXYm5iSDNWdktaZCIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmRlbGV0ZV9hcHBvaW50bWVudCIsImdldDphcHBvaW50bWVudHNfc3R1ZGVudCIsImdldDphcHBvaW50bWVudHNfdHV0b3IiLCJnZXQ6c3ViamVjdHMiLCJnZXQ6dHV0b3JzX2Jhc2VkX29uX3N1YmplY3QiLCJwYXRjaDp1cGRhdGVfYXBwb2ludG1lbnQiLCJwb3N0OmNyZWF0ZV9hcHBvaW50bWVudCIsInBvc3Q6Y3JlYXRlX3R1dG9yIl19.N9wi9LxHDg-KD5wWsEd1_mGJEhPSO3Lrs43AHaLjWIg1BIwqjpj9ImxgziNgeP3dM_xXdLD93YedStloRUaChEML6WAeC9l0Yc6P5AfCAqjBMIXuA42lhhTl2NrFk0-pyyUOXzR_jRQX_kHd08zxACugUNO3RBMnMEeHydObG3FqFOi0B7w9_v_0a7uYLAyQRTeFssNsO4zzCIGl4qZrVlRv5AiDAVNJqI7FNPwtRmbGymbCfEWe7CnsOKKVQAdlqHsBP0IYcA9dTF_Qu1rLonqCQc7r5kdtYzUTe8Ceq-QTTnaF5NvNchSDzHo_cRW63P7vOg4s2wOC10eL6GJGmQ'
TUTOR_TOKEN='eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjUyWEpERzlORkhUUUg1NnMtR3NIaSJ9.eyJpc3MiOiJodHRwczovL3NhcmFtb2hhbW1lZC51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjEzOTJlZDljYmQyNzAwMDY5ZjgzZWJhIiwiYXVkIjoiVmlydHVhbCBUdXRvciIsImlhdCI6MTYzMTEzNzUzMywiZXhwIjoxNjMxMTQ0NzMzLCJhenAiOiIyN2NjVWMxOVk2c2ZkeUwyc01WUnpXYm5iSDNWdktaZCIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmRlbGV0ZV9hcHBvaW50bWVudCIsImdldDphcHBvaW50bWVudHNfdHV0b3IiLCJnZXQ6c3ViamVjdHMiLCJnZXQ6dHV0b3JzX2Jhc2VkX29uX3N1YmplY3QiLCJwYXRjaDp1cGRhdGVfYXBwb2ludG1lbnQiXX0.n_UTu_QxDRz25e3-prPZeUyRBnS9nZFyuXktx70uirH4-ENWcNfDj5x5VmQBDA1hzN88izc2PS0vC74nPyXK7Np-nFkoYTTlhyttnbKHEVDRbdYjgvjOmHYy7QkpYzME90_cxh4hekcqzYDF6Amg2fr_rd38LAQ1_pZ1KuyOArO1pwYV4x3TtBQezmxeVxhXky11fLFF1AHhua_br0GLBb1NIkr8hjb4e8mqsl7DUm30xkzdUa64VlQl0SVqDBD0HQvFlcQ8s7j7kFX4nKovnGX6QI4Qc4gS3QjPAECewEtuAotuPtsQxJKp41RrWmvUqLvmjDMbBJPAjTf7V0zMgw'

#  student,manager,tutor
#Email: 
student@gmail.com
#Password: 
St123456 

#Email: 
manager@gmail.com 
#Password:
Ma123456 

#Email: 
tutor@gmail.com 
#Password:
Tu123456 

LOGIN_URL = 'https://fsnd-class.us.auth0.com/authorize?audience=developer&response_type=token&client_id=ceQ2QXcul85lqvr59eZvaaL0nDLE5V4J&redirect_uri=https://animal-rescue-and-shelter.herokuapp.com/all-pets'
