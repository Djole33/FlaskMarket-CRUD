from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
app.config['SECRET_KEY'] ='f5b8f1a510651e0bd41d6794'
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = "login_page"
login_manager.login_message_category = "info"
@login_manager.user_loader
def load_user(user_id):
    from .models import User
    return User.query.get(int(user_id))

app.app_context().push()

from market import routes
