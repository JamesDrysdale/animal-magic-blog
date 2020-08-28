from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


# Configuration
app = Flask(__name__)
app.config['SECRET_KEY'] = '1a394f30fa58662edd8941ed9f8c21e2'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

from animalmagicblog import routes # Import here to avoid circular import error 