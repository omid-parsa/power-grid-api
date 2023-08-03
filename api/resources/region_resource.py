from flask_restful import Resource
from flask import request
from api import db
from api.models.region_model import RegionModel

class RegionResource(Resource):
    def get(self, RegionId):
        region = RegionModel.query.filter_by(RegionId=RegionId).first()
        if region:
            return {
                'RegionId': region.RegionId,
                'RegionName': region.RegionName,
                'ContinentId': region.ContinentId,
                'CreatedById': region.CreatedById,
                'CreateTMS': region.CreateTMS.isoformat() if region.CreateTMS else None,
                'UpdateTMS': region.UpdateTMS.isoformat() if region.UpdateTMS else None
            }
        else:
            return {'error': 'Region not found'}, 404

    def post(self):
        data = request.get_json()
        new_region = RegionModel(
            RegionName=data['RegionName'],
            ContinentId=data['ContinentId'],
            CreatedById=data['CreatedById'],
            CreateTMS=data['CreateTMS'],
            UpdateTMS=data['UpdateTMS']
        )
        db.session.add(new_region)
        db.session.commit()

        return new_region.RegionId, 201

    def put(self, RegionId):
        data = request.get_json()
        region = RegionModel.query.filter_by(RegionId=RegionId).first()
        if region:
            region.RegionName = data['RegionName']
            region.ContinentId = data['ContinentId'],
            region.CreatedById = data['CreatedById'],
            region.CreateTMS = data['CreateTMS'],
            region.UpdateTMS = data['UpdateTMS']
            db.session.commit()
            return region.RegionId, 200
        else:
            return {'error': 'Region not found'}, 404

    def delete(self, RegionId):
        region = RegionModel.query.filter_by(RegionId=RegionId).first()
        if region:
            db.session.delete(region)
            db.session.commit()
            return {'message': 'Region deleted'}, 200
        else:
            return {'error': 'Region not found'}, 404