from flask_restful import Resource
from flask import request
from api import db
from api.models.datainformation_model import DataInformationModel

class DataInformationResource(Resource):
    def get(self, DataId):
        datainformation = DataInformationModel.query.filter_by(DataId=DataId).first()
        if datainformation:
            return {
                'DataId': datainformation.DataId,
                'Description': datainformation.Description,
                'Link': datainformation.Link,
                'isConfirmed': datainformation.isConfirmed,
                'DataRangeStart': datainformation.DataRangeStart.isoformat() if datainformation.DataRangeStart else None,
                'DataRangeEnd': datainformation.DataRangeEnd.isoformat() if datainformation.DataRangeEnd else None,
                'Resolution': datainformation.Resolution,
                'Precision': datainformation.Precision,
                'SizeOfData': datainformation.SizeOfData,
                'CountryId': datainformation.CountryId,
                'CreatedById': datainformation.CreatedById,
                'CreateTMS': datainformation.CreateTMS.isoformat() if datainformation.CreateTMS else None,
                'UpdatedById': datainformation.UpdatedById,
                'UpdateTMS': datainformation.UpdateTMS.isoformat() if datainformation.UpdateTMS else None
            }
        else:
            return {'error': 'Data information not found'}, 404

    def post(self):
        data = request.get_json()
        new_datainformation = DataInformationModel(
            Description=data['Description'],
            Link=data['Link'],
            isConfirmed=data['isConfirmed'],
            DataRangeStart=data['DataRangeStart'],
            DataRangeEnd=data['DataRangeEnd'],
            Resolution=data['Resolution'],
            Precision=data['Precision'],
            SizeOfData=data['SizeOfData'],
            CountryId=data['CountryId'],
            CreatedById=data['CreatedById'],
            CreateTMS=data['CreateTMS'],
            UpdatedById=data['UpdatedById'],
            UpdateTMS=data['UpdateTMS']
        )
        db.session.add(new_datainformation)
        db.session.commit()

        return new_datainformation.DataId, 201

    def put(self, DataId):
        data = request.get_json()
        datainformation = DataInformationModel.query.filter_by(DataId=DataId).first()
        if datainformation:
            datainformation.Description = data['Description']
            datainformation.Link = data['Link']
            datainformation.isConfirmed = data['isConfirmed']
            datainformation.DataRangeStart = data['DataRangeStart']
            datainformation.DataRangeEnd = data['DataRangeEnd']
            datainformation.Resolution = data['Resolution']
            datainformation.Precision = data['Precision']
            datainformation.SizeOfData = data['SizeOfData']
            datainformation.CountryId = data['CountryId']
            datainformation.CreatedById = data['CreatedById']
            datainformation.CreateTMS = data['CreateTMS']
            datainformation.UpdatedById = data['UpdatedById']
            datainformation.UpdateTMS = data['UpdateTMS']
            db.session.commit()
            return datainformation.DataId, 200
        else:
            return {'error': 'Data information not found'}, 404

    def delete(self, DataId):
        datainformation = DataInformationModel.query.filter_by(DataId=DataId).first()
        if datainformation:
            db.session.delete(datainformation)
            db.session.commit()
            return {'message': 'Data information deleted'}, 200
        else:
            return {'error': 'Data information not found'}, 404
