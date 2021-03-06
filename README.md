# FSND Capstone Project - Virtual Tutor 
## Virtual Tutor 
Virtual Tutor – an online website for students they can choose what they need to learn, who they want to learn, and what time they can learn and book an appointment with tutors.

The students are able to :
1. Display subjects
2. Display tutors by subject
3. Book an appointment
4. Display their upcoming appointments
5. Delete an appointment
 
## Getting Started

### Installing Dependencies for the Backend

1. **Python 3.7**
2. **Flask**  as server framework
3. **Virtual Enviornment** Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)
4. **PIP Dependencies** 
install dependencies by running:
```bash
pip install -r requirements.txt
```
This will install all of the required packages we selected within the `requirements.txt` file.

5. **Key Dependencies**

- [Flask](http://flask.pocoo.org/) is a lightweight backend microservices framework. Flask is required to handle requests and responses.
- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM.
-  [jose](https://python-jose.readthedocs.io/en/latest/) JavaScript Object Signing and Encryption for JWTs. Useful for encoding, decoding, and verifying JWTS.
- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests if we have.
- Flask-Migrate for creating and running schema migrations

## Running the server - Backend
First ensure you are working using your created virtual environment.
To run the server, execute:
```bash
flask run --reload
```
The `--reload` flag will detect file changes and restart the server automatically.
The server will running on [http://127.0.0.1:5000/](http://127.0.0.1:5000/) or [http://localhost:5000](http://localhost:5000/)

## Testing

To run the tests, run
```
python test_app.py
```

## API Reference
### Getting Started
- Base URL: At present this app can only be run locally and it hosted in Heroku. The local host at the default, [http://127.0.0.1:5000/](http://127.0.0.1:5000). The hosted version in Heroku is at [here](https://capstonevirtualtutor.herokuapp.com/)
- Authentication: This application requires authentication to perform various actions. Some of the endpoints require various permissions. Authentication and Authorization was implemented using [Auth0.com](Auth0.com).

#### Role-Based Access Control (RBAC)
 ##### **API permissions**
 - `get:subjects` 
 - `get:tutors_based_on_subject`
 - `get:appointments_tutor`    
 - `get:appointments_student`
 - `post:create_appointment`       
 - `patch:update_appointment`
 -  `delete:delete_appointment`  
 -  `post:create_tutor`
##### **Roles** 
- Manager:
	-  Can perform all the action.
- Tutor:
	- Has `get:subjects` , `get:tutors_based_on_subject`, `get:appointments_tutor` , `patch:update_appointment`, `delete:delete_appointment` permissions.
- Student:
	- Has `get:subjects` , `get:tutors_based_on_subject`, `get:appointments_student`, `post:create_appointment`, `delete:delete_appointment` permissions.


### Error Handling

Errors are returned as JSON objects in the following format:
```
{
	"success": False,
	"error": 404,
	"message": "resource not found"
}
```
The API will return three error types when requests fail:
-   400: Bad Request
-   401: Unauthorized
-   404: Resource Not Found
-   422: Unprocessable
-   500: Internal Server Error

### Endpoints

#### GET /subjects

- General: Returns a list of subjects, and success value.
- Sample: `curl http://127.0.0.1:5000/subjects`

```json
{
	"Subjects": {
		"1": "Mathematics",
		"2": "Science"
	},
	"success": true
}

```
#### GET /subjects/<int:subject_id>/tutors
- General:
- Returns a return a list of tutors, number of total tutors, current subject.
- Sample: `curl http://127.0.0.1:5000/subjects/1/tutors`
```json
{
"Subject": "Mathematics",
"Tutors": [
{
"Available Time": [
"2021-09-10 13:00:00",
"2021-09-11 13:00:00"
],
"Id": 1,
"Introduction": "I Love Teaching Math",
"Name": "Mohammed"
},
{
"Available Time": [
"2021-09-10 13:00:00",
"2021-09-11 13:00:00"
],
"Id": 3,
"Introduction": "I Love Teaching Math",
"Name": "Abdullah"
}
],
"success": true,
"Total_Tutor": 2
}
```
#### GET /tutor/<int:tutor_id>/appointments
- General:
- Returns a return a number of total appointments, number of total upcoming appointments, list of upcoming appointments.
- Requires  `get:appointments_tutor`  permission
- Sample: `curl http://127.0.0.1:5000/tutor/1/appointments`
```json
{
"Total Appointments": 2,
"Total of Upcoming Appointments": 1,
"Upcoming Appointments": [
{
"Appointment ID": 7,
"Duration in minutes": 40,
"Start Time": "Sat, 18 Sep 2021 13:00:00 GMT",
"Student ID": 2,
"Student name": "Sara",
"confirmation": "Confirmed"
}
],
"success": true
}
```

#### GET /student/<int:student_id>/appointments
- General:
- Returns a return a number of total appointments, number of total upcoming appointments, list of upcoming appointments.
- Requires  `get:appointments_student`  permission
- Sample: `curl http://127.0.0.1:5000/student/1/appointments`
```json
{
{
"Total Appointments": 2,
"Total of Upcoming Appointments": 1,
"Upcoming Appointments": [
{
"Appointment ID": 7,
"Duration in minutes": 40,
"Start Time": "Sat, 18 Sep 2021 13:00:00 GMT",
"Tutor ID": 2,
"Tutor name": "Mohammed",
"confirmation": "Confirmed"
}
],
"success": true
}
}
```
#### POST /tutor
- General:
- Creates a new tutor.
- Requires  `post:create_tutor`  permission.
- Return the details of the created tutor and success value.
```json
{
"Tutor": {
"Available Time": [
"2021-09-10 13:00:00",
"2021-09-11 13:00:00"
],
"Id": 18,
"Introduction": "'I Love Teaching Science",
"Name": "Sara"
},
"success": true
}
```
#### POST /student
- General:
- Creates a new student.
- Return the details of the created student and success value.
```json
{
"Student": {
"Age": 13,
"Email": "Fawaz@gmail.com",
"Grade": "Intermediate",
"Id": 26,
"Name": "Fawaz"
},
"success": true
}
```
#### POST /student/<int:student_id>/appointments/create
- General:
- Returns a return the detailed of booked appointment.
- Requires  `post:create_appointment'`  permission
```json
{
"Appointment": {
"Duration": 45,
"Id": 18,
"Start Time": "Sun, 12 Sep 2021 08:00:00 GMT",
"confirmation": false
},
"success": true
}
```
#### PATCH /appointments/edit/<int:appointment_id>
- General:
- The tutor update the appointment confirmation either confirmed or not
-  Returns a return the detailed of the appointment.
- Requires  `patch:update_appointment`  permission
```json
{
"Appointment Confirmation": "Confirmed",
"success": true
}
}
```
#### Delete /appointments/delete/<int:appointment_id>
- General:
-  Returns a return the deleted of the appointment id and success value.
- Requires  `delete:delete_appointment`  permission
```json
{
"deleted id": 18,
"success": true
}
}
```
