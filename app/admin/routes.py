from flask import render_template, request, redirect, current_app, session
from . import admin_bp
from app.models import FormMessage
import hashlib


@admin_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # перевірка логіну та паролю
        if (username == current_app.config['LOGIN'] and password == 'admin'):
            session['user'] = username
        else:
            return render_template('not_logged.html')

    # GET
    return render_template('login.html')


@admin_bp.route('/admin', methods=['GET', 'POST'])
def admin():
    messages = FormMessage.query.all()

    if 'user' in session:
        return render_template('dashboard.html', messages=messages)

    return render_template('login.html')
