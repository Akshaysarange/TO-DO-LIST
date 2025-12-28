# iss file mee haam sab modules rakhenge and iss ko as package use karenge

from flask import Flask #Flask ko import kiya
from flask_sqlalchemy import SQLAlchemy #Database ko import kiya

db = SQLAlchemy() #db variable mee SQLAlchemy ko save kiya

def create_app(): # function banaya
    app = Flask(__name__) #ye mera main page hoga ye mee flask ko bata raha hu

    app.config['SECRET_KEY'] = 'your-secret-key' #session ke liye secret key
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db' #DB ki file
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app) #app and DB ko connect karne ke liye

    from app.routes.auth import auth_bp
    from app.routes.tasks import tasks_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(tasks_bp)

    return app