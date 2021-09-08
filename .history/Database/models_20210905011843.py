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
# Models.
#----------------------------------------------------------------------------#
