from api import db

class ContinentModel(db.Model):
    __tablename__ = 'continents'

    ContinentId = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ContinentName = db.Column(db.String(255))
    CreatedById = db.Column(db.Integer)
    CreateTMS = db.Column(db.DateTime)
    UpdateTMS = db.Column(db.DateTime)

    # Relationship
    countries = db.relationship('CountryModel', backref='continent', lazy=True)
    regions = db.relationship('RegionModel', backref='continent', lazy=True)