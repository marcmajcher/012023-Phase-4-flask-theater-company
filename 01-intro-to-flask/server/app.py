#!/usr/bin/env python3

from flask import Flask, jsonify, make_response
from flask_migrate import Migrate
from models import db, Production

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)
db.init_app(app)

@app.before_request
def test():
    print("ASDFASDFADS")

@app.route('/')
def index():
    return "hey what's up!!!!!!!"

@app.route('/productions/<string:title>')
def production(title):
    production = Production.query.filter(Production.title == title).first()
    production_response = {
        "title": production.title,
        "genre": production.genre,
        "director": production.director
    }
    return make_response(
        jsonify(production_response),
        200
    )

# 17.✅ Use the before_request request hook, what this hook does is up to you. You could hit a breakpoint, print something to server console or anything else you can think of.

