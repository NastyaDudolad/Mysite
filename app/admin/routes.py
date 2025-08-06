from flask import Blueprint, render_template, request, redirect, url_for
from . import admin_bp
from app.models import FormMessage
import hashlib
from config import *

url_for

@admin_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # перевірка логіну та паролю
        if username == LOGIN and hashlib.md5(password.encode()).hexdigest() == PASSWORD_HASH:
            return redirect(f'{HOST}/admin')
        else:
            return render_template('not_logged.html')

    # GET
    return render_template('login.html')


@admin_bp.route('/admin', methods=['GET', 'POST'])
def admin():
    messages = FormMessage.query.all()
    return render_template('dashboard.html', messages=messages)
