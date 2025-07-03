from flask import render_template, request
import config
from config import *
import hashlib
from app.models import Artist
from app.models import Service
import json
import requests

# tg_bot
url = f'https://api.telegram.org/bot{config.TOKEN}/'
def send_message(chat_id, text):
    response = requests.get((url + f'sendMessage?chat_id={config.CHAT_ID}&text={text}'))
    return response.json()
def get_chat_id(update):
    return update['message']['chat']['id']
def send_request_msg(update, msg_to_send):
    send_message(get_chat_id(update), msg_to_send)


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

    @app.route('/process_form', methods=['GET', 'POST'])
    def proccess_form():
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        tg_bot = request.form.get('Telegram bot')
        python_games = request.form.get('Python games')
        website = request.form.get('Website')
        construct_games = request.form.get('Construct games')
        error_msg = ''
        success = True

        if name == '' or message == '':
            operation_message = 'Name or message cannot be empty'
            success = False
        else:
            selected_options = ''
            joint = ' | '

            if tg_bot == '1':
                selected_options += 'tg_bot'
            if website == '1':
                if selected_options != '':
                    selected_options += joint
                selected_options += 'website'
            if construct_games == '1':
                if selected_options != '':
                    selected_options += joint
                selected_options += 'construct_games'
            if python_games == '1':
                if selected_options != '':
                    selected_options += joint
                selected_options += 'python_games'

            send_string = f'Someone made a request. Name: {name}, email: {email}, selected options: {selected_options}, '\
                f'message: {message}'
            send_message(config.my_chat_id, send_string)

            operation_message = 'We will connect you soon'

        data = {
            'success': success,
            'message': operation_message,
            'error': error_msg
        }

        return json.dumps(data)

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
