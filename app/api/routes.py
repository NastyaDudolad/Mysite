from flask import request
from . import api_bp
from app.models import FormMessage
import json
from config import *
from app import db
import requests

# tg_bot
url = f'https://api.telegram.org/bot{TOKEN}/'
def send_message(chat_id, text):
    response = requests.get((url + f'sendMessage?chat_id={CHAT_ID}&text={text}'))
    return response.json()

def append_option(selected, option):
    if selected:
        selected += ' | '
    selected += option
    return selected

@api_bp.route('/process_form', methods=['GET', 'POST'])
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

        if tg_bot == '1':
            selected_options = append_option(selected_options, 'tg_bot')
        if website == '1':
            selected_options = append_option(selected_options, 'website')
        if construct_games == '1':
            selected_options = append_option(selected_options, 'construct_games')
        if python_games == '1':
            selected_options = append_option(selected_options, 'python_games')

        send_string = f'Someone made a request. Name: {name}, email: {email}, selected options: {selected_options}, ' \
                      f'message: {message}'
        send_message(CHAT_ID, send_string)

        new_msg = FormMessage(name=name, email=email, selected_option=selected_options, message=message)
        db.session.add(new_msg)
        db.session.commit()
        operation_message = 'We will connect you soon'

    data = {
        'success': success,
        'message': operation_message,
        'error': error_msg
    }

    return json.dumps(data)

@api_bp.route('/form_messages/<int:id>', methods=['DELETE'])
def delete_form_message(id):
    error_msg = ''
    operation_message = ''

    message_to_delete = db.session.query(FormMessage).get(id)

    if message_to_delete is None:
        error_msg = 'No record'
        success = False
    else:
        db.session.delete(message_to_delete)
        db.session.commit()
        success = True
        operation_message = 'Record was deleted succefully'

    data = {
        'success': success,
        'message': operation_message,
        'error': error_msg
    }

    return json.dumps(data)
