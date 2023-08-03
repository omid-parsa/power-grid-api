from flask_restful import Resource
from flask import request
from api import db
from api.models.country_model import CountryModel

class CountryResource(Resource):
    def get(self, CountryId):
        country = CountryModel.query.filter_by(CountryId=CountryId).first()
        if country:
            return {
                'CountryId': country.CountryId,
                'CountryName': country.CountryName,
                'ContinentId': country.ContinentId,
                'RegionId': country.RegionId,
                'CreatedById': country.CreatedById,
                'CreateTMS': country.CreateTMS.isoformat() if country.CreateTMS else None,
                'UpdateTMS': country.UpdateTMS.isoformat() if country.UpdateTMS else None
            }
        else:
            return {'error': 'Country not found'}, 404

    def post(self):
        data = request.get_json()
        new_country = CountryModel(
            CountryName=data['CountryName'],
            ContinentId=data['ContinentId'],
            RegionId=data['RegionId'],
            CreatedById=data['CreatedById'],
            CreateTMS=data['CreateTMS'],
            UpdateTMS=data['UpdateTMS']
        )
        db.session.add(new_country)
        db.session.commit()

        return new_country.CountryId, 201

    def put(self, CountryId):
        data = request.get_json()
        country = CountryModel.query.filter_by(CountryId=CountryId).first()
        if country:
            country.CountryName = data['CountryName']
            country.ContinentId = data['ContinentId']
            country.RegionId = data['RegionId']
            country.CreatedById = data['CreatedById']
            country.CreateTMS = data['CreateTMS']
            country.UpdateTMS = data['UpdateTMS']
            db.session.commit()
            return country.CountryId, 200
        else:
            return {'error': 'Country not found'}, 404

    def delete(self, CountryId):
        country = CountryModel.query.filter_by(CountryId=CountryId).first()
        if country:
            db.session.delete(country)
            db.session.commit()
            return {'message': 'Country deleted'}, 200
        else:
            return {'error': 'Country not found'}, 404