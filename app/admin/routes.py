from flask import render_template, request, redirect, current_app
from . import admin_bp
from app.models import FormMessage
import hashlib


@admin_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # перевірка логіну та паролю
        if (username == current_app.config['LOGIN']
                and hashlib.md5(password.encode()).hexdigest() == current_app.config['PASSWORD_HASH']):
            host = current_app.config['HOST']
            return redirect(f'{host}/admin')
        else:
            return render_template('not_logged.html')

    # GET
    return render_template('login.html')


@admin_bp.route('/admin', methods=['GET', 'POST'])
def admin():
    messages = FormMessage.query.all()
    return render_template('dashboard.html', messages=messages)
