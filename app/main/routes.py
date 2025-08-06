from flask import Blueprint, render_template
from app.models import Service
from . import main_bp

@main_bp.route('/')
def home():
    import datetime
    year = datetime.datetime.now()
    year = year.strftime("%Y")
    services = Service.query.all()
    return render_template('index.html', services=services, current_year=year)
