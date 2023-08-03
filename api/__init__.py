from flask import Flask
from flask_restful import Api
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')

api = Api(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

def initialize_models():
    from api.models import user_model

initialize_models()

# Import resources and models after the creation of db object to avoid circular imports
def initialize_routes():
    from api.resources import user_resource
    from api.resources.file_process_resources import file_process_resource
    from api.resources import continent_resource
    from api.resources import country_resource
    from api.resources import region_resource
    from api.resources import datainformation_resource

    # Add resources to the API
    api.add_resource(user_resource.UserResource, '/user/<int:UserId>')
    api.add_resource(file_process_resource.FileProcessingResource, '/process_file')
    api.add_resource(continent_resource.ContinentResource, '/continent/<int:ContinentId>')
    api.add_resource(country_resource.CountryResource, '/country/<int:CountryId>')
    api.add_resource(region_resource.RegionResource, '/region/<int:RegionId>')
    api.add_resource(datainformation_resource.DataInformationResource, '/datainformation/<int:DataId>')

initialize_routes()