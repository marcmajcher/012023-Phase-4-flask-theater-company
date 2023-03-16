#!/usr/bin/env python3
# 📚 Review With Students:
    # REST
    # Status codes
    # Error handling 
# Set up:
    # cd into server and run the following in the terminal
    # export FLASK_APP=app.py
    # export FLASK_RUN_PORT=5000
    # flask db init
    # flask db revision --autogenerate -m'Create tables' 
    # flask db upgrade 
    # python seed.py
from flask import Flask, request, make_response, abort
from flask_migrate import Migrate

from flask_restful import Api, Resource

# 1.✅ Import NotFound from werkzeug.exceptions for error handling
from werkzeug.exceptions import NotFound



from models import db, Production, CastMember

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app)


api = Api(app)

class Productions(Resource):
    def get(self):
        production_list = [p.to_dict() for p in Production.query.all()]
        response = make_response(
            production_list,
            200,
        )

        return response

    def post(self):
        form_json = request.get_json()
        new_production = Production(
                title=form_json['title'],
                genre=form_json['genre'],
                budget=int(form_json['budget']),
                image=form_json['image'],
                director=form_json['director'],
                description=form_json['description']
            )

        db.session.add(new_production)
        db.session.commit()

        response_dict = new_production.to_dict()

        response = make_response(
            response_dict,
            201,
        )
        return response
api.add_resource(Productions, '/productions')


class ProductionByID(Resource):
    def get(self,id):
        production = Production.query.filter_by(id=id).first()
# 3.✅ If a production is not found raise the NotFound exception AND/OR use abort() to create a 404 with a customized error message
        if not production:
            abort(404, "The Production you were trying to update was not found.")

        production_dict = production.to_dict()
        response = make_response(
            production_dict,
            200
        )
        
        return response

# 4.✅ Patch
    # 4.1 Create a patch method that takes self and id
    # 4.2 Query the Production from the id
    # 4.3 If the production is not found raise the NotFound exception AND/OR use abort() to create a 404 with a customized error message
    # 4.4 Loop through the request json object and update the productions attributes. Note: Be cautions of the data types to avoid errors.
    # 4.5 add and commit the updated production 
    # 4.6 Create and return the response
    def patch(self, id):
        production = Production.query.filter_by(id=id).first()
        if not production:
            abort(404, "The Production you were trying to update was not found.")
        form_json = request.get_json()
        for key in form_json:
            setattr(production, key, form_json[key])

        db.session.add(production)
        db.session.commit()

        production_dict = production.to_dict()
        
        response = make_response(
            production_dict,
            200
        )
        return response
# 5.✅ Delete
    # 5.1 Create a delete method, pass it self and the id
    # 5.2 Query the Production 
    # 5.3 If the production is not found raise the NotFound exception AND/OR use abort() to create a 404 with a customized error message
    # 5.4 delete the production and commit 
    # 5.5 create a response with the status of 204 and return the response 
    def delete(self, id):
        production = Production.query.filter_by(id=id).first()
        if not production:
            raise abort(404, "The Production you were trying to delete was not found.")

        db.session.delete(production)
        db.session.commit()

        response = make_response('', 204)
        
        return response

   
api.add_resource(ProductionByID, '/productions/<int:id>')

# 2.✅ use the @app.errorhandler() decorator to handle Not Found
    # 2.1 Create the decorator and pass it NotFound
    # 2.2 Use make_response to create a response with a message and the status 404
    # 2.3 return t he response
@app.errorhandler(NotFound)
def handle_not_found(e):
    response = make_response(
        "Not Found: Sorry the resource you are looking for does not exist",
        404
    )

    return response

# To run the file as a script
# if __name__ == '__main__':
#     app.run(port=5000, debug=True)