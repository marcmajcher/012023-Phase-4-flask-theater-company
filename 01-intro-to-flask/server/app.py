#!/usr/bin/env python3
# 📚 Review With Students:
    # Review request-response cycle
    # Review Web Servers and WSGI/Werkzeug
# 1.✅ - navigate to models.py
# 2.✅ Imports
	# `Flask` from `flask`
	# `Migrate` from `flask_migrate`
	# db and `Production` from `models`


# 3.✅ Initialize the app
    # Add `app = Flask(__name__)`
    # Configure the database by adding`app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'`
    # and `app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False` 
    # Set the Migrations with `migrate = Migrate(app, db)`
    # Finally initialize the application with `db.init_app(app)`

 # 4. ✅ Migrate 
	# cd into the server folder
	# run in terminal
		# export FLASK_APP=app.py
		# export FLASK_RUN_PORT=5555
		# flask db init
		# flask db revision --autogenerate -m'Create tables productions'
    # Review the Database to verify your table migrated correctly
# 5. ✅ Navigate to seed.rb

# 13.✅ Routes
    # Create your a route
    # `@app.route('/')
    #  def index():
    #    return '<h1>Hello World!</h1>'`

# 14.✅ run the server with `flask run` and verify your route in the browser at `http://localhost:5000/`

# 15.✅ Create a dynamic rout
# `@app.route('/productions/<string:title>')
#  def production(title):
#     return f'<h1>{title}</h1>'`


# 16.✅ Update this route to find a production by it's title and send it to our browser
    # Before continuing, import jsonify and make_response from Flask at the top of the file.
    # 📚 Review With Students: status codes
    # make_response will allow us to make a response object with the response body and status code.
    # jsonify will convert our query into json

    # `@app.route('/productions/<string:title>')
    # def production(title):
    #     production = Production.query.filter(Production.title == title).first()
    #     production_response = {
    #         "title":production.title,
    #         "genre":production.genre,
    #         "director": production.director
    #         }
    #     response = make_response(
    #         jsonify(production_response),
    #         200
    #     )`


    


# Note: If you'd like to run the application as a script instead of using `flask run` uncomment the line bellow and run `python app.py`
# if __name__ == '__main__':
#     app.run(port=5000, debug=True)