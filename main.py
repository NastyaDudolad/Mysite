from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from app.models import Artist
from config import *
import hashlib

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///base.db'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False

db = SQLAlchemy()
db.init_app(app)


# text = 'admin'
# hash_object = hashlib.md5(text.encode())
# print(hash_object.hexdigest())

def init_routes(app):
    @app.route('/music')
    def music():
        with app.app_context():
            artists = Artist.query.all()
            print(artists)
        return render_template('index.html', artists=artists)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # проверка логина и пароля
        if username == LOGIN and hashlib.md5(password.encode()).hexdigest() == PASSWORD_HASH:
            return render_template('dashboard.html')
        else:
            return render_template('not_logged.html')
    return render_template('login.html')


if __name__ == '__main__':
    app.run(port=80)
