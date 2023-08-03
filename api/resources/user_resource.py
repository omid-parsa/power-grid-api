from flask_restful import Resource, reqparse
from api.models.user_model import UserModel
from datetime import datetime
from api import db

parser = reqparse.RequestParser()
parser.add_argument('ExternalId', required=True, help='ExternalId cannot be blank!')
parser.add_argument('Name', required=True, help='Name cannot be blank!')

class UserResource(Resource):
    def get(self, UserId):
        user = UserModel.query.filter_by(UserId=UserId).first()
        if user:
            return {
                'UserId': user.UserId, 
                'ExternalId': user.ExternalId, 
                'Name': user.Name, 
                'CreateTMS': user.CreateTMS.isoformat() if user.CreateTMS else None,
                'UpdateTMS': user.UpdateTMS.isoformat() if user.UpdateTMS else None
            }
        else:
            return {'error': 'user not found'}, 404

    def post(self):
        data = parser.parse_args()
        user = UserModel(data['ExternalId'], data['Name'], datetime.utcnow(), datetime.utcnow())
        db.session.add(user)
        db.session.commit()
        return {'message': 'New user added', 'user': {
                'UserId': user.UserId, 
                'ExternalId': user.ExternalId, 
                'Name': user.Name, 
                'CreateTMS': user.CreateTMS.isoformat() if user.CreateTMS else None,
                'UpdateTMS': user.UpdateTMS.isoformat() if user.UpdateTMS else None
            }}, 201

    def put(self, UserId):
        data = parser.parse_args()
        user = UserModel.query.filter_by(UserId=UserId).first()
        if user:
            user.ExternalId = data['ExternalId']
            user.Name = data['Name']
            user.UpdateTMS = datetime.utcnow()
            db.session.commit()
            return {'message': 'User updated', 'user': {
                'UserId': user.UserId, 
                'ExternalId': user.ExternalId, 
                'Name': user.Name, 
                'CreateTMS': user.CreateTMS.isoformat() if user.CreateTMS else None,
                'UpdateTMS': user.UpdateTMS.isoformat() if user.UpdateTMS else None
            }}, 200
        else:
            return {'error': 'user not found'}, 404

    def delete(self, UserId):
        user = UserModel.query.filter_by(UserId=UserId).first()
        if user:
            db.session.delete(user)
            db.session.commit()
            return {'message': 'User deleted'}, 200
        else:
            return {'error': 'user not found'}, 404