#!/usr/bin/env python3
# 📚 Review With Students:
    # Review what an API is
    # Discuss MVC architecture and reinforce patterns/best practices
    # Introduce the concept of REST and how to use it to inform route names
    # Serialization 
    # PostMan
# Set up:
    # cd into server and run the following in the terminal
    # export FLASK_APP=app.py
    # export FLASK_RUN_PORT=5000
    # flask db init
    # flask db revision --autogenerate -m'Create tables' 
    # flask db upgrade 
    # python seed.py

from flask import Flask, request, make_response, jsonify
from flask_migrate import Migrate
# 1.✅ Import Api and Resource from flask_restful
    # Take a moment to explain what these two classes do at a high level. 
from flask_restful import Api, Resource


from models import db, Production, CrewMember

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#Note: `app.json.compact = False` Configures JSON responses to print on indented lines
app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app)

# 2.✅ Initialize the Api
    #`api = Api(app)`


# 3.✅ Create a Production class that inherits from Resource

    # 4.✅ Create a GET all route
        # After building the route run the server and test it in the browser
    # def get(self):
    #     productions = []
    #     for production in Production.query.all():
    #         production_dict = {
    #             "title": production.title,
    #             "genre": production.genre,
    #             "budget": production.budget,
    #             "image": production.image,
    #             "director": production.director,
    #             "description": production.description,
    #             "ongoing": production.ongoing,
                
    #         }
    #         productions.append(production_dict)

    #     response = make_response(
    #         jsonify(productions),
    #         200
    #     )

    #     return response
# 6.✅ Serialization
    # This is great, but there's a cleaner way to do this with Serialization that will allow us to easily add our associations as well.
    # Navigate to models.py

 # 9.✅ User our serializer to format our response to be cleaner
    # def get(self):
     
    #     production_list = [p.to_dict() for p in Production.query.all()]

    #     response = make_response(
    #         production_list,
    #         200,
    #     )

    #     return response
  

    # 10.✅ Create a POST route
        # Prepare a POST request in Postman under the Body tab select form-data and fill out the body of a production request. 
        # Create the POST route 
        # 📚 Review With Students: request object
        # def post(self):
        # new_production = Production(
        #     title=request.form['title'],
        #     genre=request.form['genre'],
        #     budget=int(request.form['budget']),
        #     image=request.form['image'],
        #     director=request.form['director'],
        #     description=request.form['description'],
        #     ongoing=bool(request.form['ongoing']),
        # )

        # db.session.add(new_production)
        # db.session.commit()

        # response_dict = new_production.to_dict()

        # response = make_response(
        #     response_dict,
        #     201,
        # )
        # return response


# 5.✅ add Productions to our api resource
    # api.add_resource(Productions, '/productions')
    # run the server and test the GET all route in the browser.

 # 10.✅ Create a GET one route
     # Build a class called ProductionByID that inherits from Resource.
    # create our get method and pass it the id along with self. 
    # Make a query for our production by the id and build a response to send to the browser.
    # class ProductionByID(Resource):
    # def get(self,id):
    #     production = Production.query.filter_by(id=id).first().to_dict()

    #     response = make_response(
    #         production,
    #         200
    #     )
        
    #     return response


 # 11.✅ Add the new route to our api resource
    # api.add_resource(ProductionByID, '/productions/<int:id>')
