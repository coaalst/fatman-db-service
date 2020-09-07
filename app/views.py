from flask import request, jsonify, make_response
from app import app

import jwt, datetime, uuid, json
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps

# Models
from app.models import Entry

# DB
from app import db

# fetch all entries 
@app.route('/', methods=['GET'])
def entry_bundle(current_user):

    bundle = Entry.query.all()  
    return jsonify(bundle), 200

# Fetch entries in the last 30 days
@app.route('/month', methods=['GET'])
def fetch_data():

    bundle = Entry.query.all()  
    return jsonify(bundle), 200

# Post entry
@app.route('/', methods=['POST'])
def add_entry():
    
    data = request.get_json()
    entry = Entry(username=data['username'], humidity=data['humidity'],  temp=data['temp'],  fan_state=data['fan_state'],  pump_state=data['pump_state'],  light_state=data['Light_state'])
    db.session.add(entry) 
    db.session.commit()

    return jsonify({'message' : 'New entry created!'}), 201