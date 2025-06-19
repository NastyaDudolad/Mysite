from app import db

class Service(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    image_src = db.Column(db.String(200), nullable=True)
    icon_class = db.Column(db.String(100), nullable=True)
    link = db.Column(db.String(200), nullable=True)


