from api import db

class UserModel(db.Model):
  __tablename__ = 'users'

  UserId = db.Column(db.Integer, primary_key=True, autoincrement=True)
  ExternalId = db.Column(db.Text)
  Name = db.Column(db.Text)
  CreateTMS = db.Column(db.DateTime)
  UpdateTMS = db.Column(db.DateTime)

  def __init__(self, ExternalId, Name, CreateTMS, UpdateTMS):
    self.ExternalId = ExternalId
    self.Name = Name
    self.CreateTMS = CreateTMS
    self.UpdateTMS = UpdateTMS