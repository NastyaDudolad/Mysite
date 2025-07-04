from app import db

class FormMessage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=True)
    selected_option = db.Column(db.String(255), nullable=True)
    message = db.Column(db.Text, nullable=True)



