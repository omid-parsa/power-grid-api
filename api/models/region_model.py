from api import db

class RegionModel(db.Model):
    __tablename__ = 'regions'

    RegionId = db.Column(db.Integer, primary_key=True, autoincrement=True)
    RegionName = db.Column(db.String(255))
    ContinentId = db.Column(db.Integer, db.ForeignKey('continents.ContinentId'))
    CreatedById = db.Column(db.Integer)
    CreateTMS = db.Column(db.DateTime)
    UpdateTMS = db.Column(db.DateTime)

    # Relationship
    countries = db.relationship('CountryModel', backref='region', lazy=True)