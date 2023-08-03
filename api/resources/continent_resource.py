from flask_restful import Resource
from flask import request
from api import db
from api.models.continent_model import ContinentModel

class ContinentResource(Resource):
    def get(self, ContinentId):
        continent = ContinentModel.query.filter_by(ContinentId=ContinentId).first()
        if continent:
            return {
                'ContinentId': continent.ContinentId,
                'ContinentName': continent.ContinentName,
                'CreatedById': continent.CreatedById,
                'CreateTMS': continent.CreateTMS.isoformat() if continent.CreateTMS else None,
                'UpdateTMS': continent.UpdateTMS.isoformat() if continent.UpdateTMS else None
            }
        else:
            return {'error': 'Continent not found'}, 404

    def post(self):
        data = request.get_json()
        new_continent = ContinentModel(
            ContinentName=data['ContinentName'],
            CreatedById=data['CreatedById'],
            CreateTMS=data['CreateTMS'],
            UpdateTMS=data['UpdateTMS']
        )
        db.session.add(new_continent)
        db.session.commit()

        return new_continent.ContinentId, 201

    def put(self, ContinentId):
        data = request.get_json()
        continent = ContinentModel.query.filter_by(ContinentId=ContinentId).first()
        if continent:
            continent.ContinentName = data['ContinentName']
            continent.CreatedById = data['CreatedById']
            continent.CreateTMS = data['CreateTMS']
            continent.UpdateTMS = data['UpdateTMS']
            db.session.commit()
            return continent.ContinentId, 200
        else:
            return {'error': 'Continent not found'}, 404

    def delete(self, ContinentId):
        continent = ContinentModel.query.filter_by(ContinentId=ContinentId).first()
        if continent:
            db.session.delete(continent)
            db.session.commit()
            return {'message': 'Continent deleted'}, 200
        else:
            return {'error': 'Continent not found'}, 404