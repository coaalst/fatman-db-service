from app import db
from datetime import datetime

class Entry(db.Model):
    __tablename__ = 'entries'
    id = db.Column(db.Integer, primary_key = True)
    humidity = db.Column(db.String(255))
    temp = db.Column(db.String(255))
    date = db.Column(db.DateTime, nullable=False,
        default=datetime.utcnow)
    fan_state = db.Column(db.Boolean)
    pump_state = db.Column(db.Boolean)
    light_state = db.Column(db.Boolean)

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.name