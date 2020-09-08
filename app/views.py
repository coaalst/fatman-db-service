from flask import request, jsonify
from app import app

import json
from datetime import datetime, timedelta

# Models
from app.models import Entry

# DB
from app import db

# fetch all entries 
@app.route('/', methods=['GET'])
def entry_bundle():

    bundle = Entry.query.all()
    response = [e.serialize() for e in bundle]  
    return jsonify(response), 200

# Fetch entries in the last 30 days
@app.route('/month', methods=['GET'])
def fetch_data():

    filter_30_days = datetime.now() - timedelta(days = 30)
    bundle = Entry.query.filter(Entry.date >= filter_30_days).all()
    response = [e.serialize() for e in bundle]  
    return jsonify(response), 200

# Post entry
@app.route('/', methods=['POST'])
def add_entry():
    
    data = request.get_json()
    entry = Entry(humidity=data['humidity'],  temp=data['temp'],  fan_state=data['fan_state'],  pump_state=data['pump_state'],  light_state=data['light_state'])
    db.session.add(entry) 
    db.session.commit()

    return jsonify({'message' : 'New entry created!'}), 201