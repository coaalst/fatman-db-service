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

    def __init__(self, humidity, temp, fan_state, pump_state, light_state):
        self.humidity = humidity
        self.temp = temp
        self.fan_state = fan_state
        self.pump_state = pump_state
        self.light_state = light_state

    def __repr__(self):
        return '<User %r>' % self.name

    def serialize(self):
        return {
            'id': self.id,
            'humidity': self.humidity,
            'temp': self.temp,
            'date': self.date,
            'fan_state': self.fan_state,
            'pump_state': self.pump_state,
            'light_state': self.light_state
            }

db.create_all()