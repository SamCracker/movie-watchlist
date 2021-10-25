from flask import Flask
from flask_restful import Api
from database.db import initialize_db
from resources.routes import initialize_routes
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from dotenv import load_dotenv

app = Flask(__name__)

# print(load_dotenv())
app.config["JWT_SECRET_KEY"] = "t1NP63m4wnBg6nyHYKfmc2TpCOGI4snn"

api = Api(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

# app.config['MONGODB_SETTINGS'] = {
#     'host': 'mongodb+srv://dbUser:1234@flask-api-movie.q561z.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'
# }

app.config['MONGODB_HOST'] = "mongodb+srv://dbUser:1234@flask-api-movie.q561z.mongodb.net/movies_api?retryWrites=true&w=majority"
app.config['JSON_AS_ASCII'] = False
app.config['SECRET_KEY'] = "key"
app.config['DEBUG'] = True
app.config['ENV'] = 'development'

print(app.config)

# Initializing Database
initialize_db(app)

# Initializing routes
initialize_routes(api)
# print(initialize_routes(api))
app.run()