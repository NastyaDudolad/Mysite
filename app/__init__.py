from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.secret_key = '1234'
    #app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///base.db')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:Nastya07102009@localhost:5432/test2'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['LOGIN'] = os.getenv('LOGIN', 'admin')
    app.config['PASSWORD_HASH'] = os.getenv('PASSWORD_HASH', '21232f297a57a5a743894a0e4a801fc3')
    app.config['TOKEN'] = os.getenv('TOKEN')
    app.config['CHAT_ID'] = os.getenv('CHAT_ID')
    app.config['HOST'] = os.getenv('HOST', 'https://mysite-2-zzw9.onrender.com')

    db.init_app(app)

    with app.app_context():
        from app import models
        db.create_all()

    from .main import main_bp
    from .admin import admin_bp
    from .api import api_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(admin_bp)
    app.register_blueprint(api_bp)

    return app
