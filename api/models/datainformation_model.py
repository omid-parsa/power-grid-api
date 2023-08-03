from api import db

class DataInformationModel(db.Model):
    __tablename__ = 'datainformation'

    DataId = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Description = db.Column(db.Text)
    Link = db.Column(db.Text)
    isConfirmed = db.Column(db.Boolean)
    DataRangeStart = db.Column(db.DateTime)
    DataRangeEnd = db.Column(db.DateTime)
    Resolution = db.Column(db.Text)
    Precision = db.Column(db.Text)
    SizeOfData = db.Column(db.Text)
    CountryId = db.Column(db.Integer, db.ForeignKey('countries.CountryId'))
    CreatedById = db.Column(db.Integer)
    CreateTMS = db.Column(db.DateTime)
    UpdatedById = db.Column(db.Integer)
    UpdateTMS = db.Column(db.DateTime)