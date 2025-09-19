from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.secret_key = os.getenv('KEY', '1234')

    # строка подключения к БД
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:Nastya07102009@localhost:5432/test2'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    with app.app_context():
        from app.models.user import User
        db.drop_all()
        db.create_all()
        create_default_users(User)

    # подключение blueprints
    from .main import main_bp
    from .admin import admin_bp
    from .api import api_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(admin_bp)
    app.register_blueprint(api_bp)

    return app


def create_default_users(User):
    if not User.query.filter_by(username="admin").first():
        admin = User(username="admin", role="admin")
        admin.set_password("admin")
        db.session.add(admin)

    if not User.query.filter_by(username="manager").first():
        manager = User(username="manager", role="manager")
        manager.set_password("manager123")
        db.session.add(manager)

    db.session.commit()
