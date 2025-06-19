from flask import render_template, request
from config import *
import hashlib
from app.models import Artist
from app.models import Service
import json


def init_routes(app):
    @app.route('/music')
    def music():
        with app.app_context():
            artists = Artist.query.all()
            for artist in artists:
                artist.image_src = '/static/images/' + artist.image_src
            print(artists)
        return render_template('music.html', artists=artists)

    @app.route('/')
    def home():
        services = Service.query.all()
        return render_template('index.html', services=services)

    @app.route('/proccess_form', methods=['POST'])
    def proccess_form():
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        data = {
            'name': name,
            'name': name,
            'name': name,
        }
        return json.dump(data)

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']
            # перевірка логіну та паролю
            if username == LOGIN and hashlib.md5(password.encode()).hexdigest() == PASSWORD_HASH:
                return render_template('dashboard.html')
            else:
                return render_template('not_logged.html')
        return render_template('login.html')
