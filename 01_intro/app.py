# set up flask app configuration, create routes, return responses, take information from our requests

# set up imports
from flask import Flask, make_response, jsonify  # importing an instance of flask class

# this will be our WSGI (Web Server Gateway Interface )

from flask_migrate import Migrate  # for migration of table

from models import db, Coffee  # import sql  alchemy

# database Coffee class

# create instances of Flask class
app = Flask(__name__)  # for Flask to know where to look for


# configuration
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# migrate the Coffee model
migrate = Migrate(app, db)

# connect the db to the app
db.init_app(app)


# navigate to seed
# create dynamic routes
#  ROUTS
@app.route("/")
def index():
    return "<h1> Hello World!</h1>"


@app.route("/the-most-expensive-coffee")
def get_the_most_exspensive_coffee():
    # query to find most expensive coffee

    coffee = Coffee.query.order_by(Coffee.price.desc()).first()
    print(coffee)
    cup = {
        "name": coffee.name,
        "description": coffee.description,
        "price": coffee.price,
    }

    return make_response(jsonify(cup), 200)


# dinamic routes
@app.route("/coffees/<string:name>")
def coffee(name):
    sql = Coffee.query.filter_by(name=name).first()
    print(sql)
    coffee = {
        "name": sql.name,
        "description": sql.description,
        "price": sql.price,
    }
    return make_response(jsonify(coffee))


# in terminal
# $flask db init
# $flask db migrate
# $flask db upgrade

# we should see something like below when we run the command above
# INFO  [alembic.runtime.migration] Context impl SQLiteImpl.
# INFO  [alembic.runtime.migration] Will assume non-transactional DDL.
# INFO  [alembic.autogenerate.compare] Detected added table 'coffees'
#   Generating /Users/greem/Dev/22-Flatiron-teach/greem-practice/lecture-041023-11132
#   3/111323-Phase-4-Flask/01_intro_to_flask_sqlalchemy/migrations/versions/cd621237e
#   4a0_.py ...  done


if __name__ == "__main__":
    app.run(port=5555, debug=True)
