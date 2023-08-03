from api import db

class CountryModel(db.Model):
    __tablename__ = 'countries'

    CountryId = db.Column(db.Integer, primary_key=True, autoincrement=True)
    CountryName = db.Column(db.String(255))
    ContinentId = db.Column(db.Integer, db.ForeignKey('continents.ContinentId'))
    RegionId = db.Column(db.Integer, db.ForeignKey('regions.RegionId'))
    CreatedById = db.Column(db.Integer)
    CreateTMS = db.Column(db.DateTime)
    UpdateTMS = db.Column(db.DateTime)

    # Relationship
    datainformation = db.relationship('DataInformationModel', backref='country', lazy=True)