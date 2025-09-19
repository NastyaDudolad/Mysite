from flask import render_template, request, redirect, current_app, session, url_for
from . import admin_bp
from app.models import FormMessage
from app.models import User
import hashlib


@admin_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()

        if user and user.check_password(password):
            session['user'] = user.username
            session['role'] = user.role
            return redirect(url_for('admin.admin'))
        else:
            return render_template('not_logged.html')

    return render_template('login.html')


@admin_bp.route('/admin', methods=['GET', 'POST'])
def admin():
    messages = FormMessage.query.all()

    if 'user' not in session:
        return redirect(url_for('admin.login'))

    username = session['user']
    role = session['user']

    if session['role'] == 'manager':
        pass

    if session['role'] == 'admin':
        pass

    return render_template('dashboard.html', messages=messages, username=username, role=role)
