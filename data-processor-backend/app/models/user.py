from app.extensions import db

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(80))
	org_id = db.Column(db.Integer, db.ForeignKey('org.id'), nullable=True)
	org_level = db.Column(db.String(120), nullable=True)
	pswd = db.Column(db.String(80), nullable=False)

	def __init__(self, name, org_id, org_level, pswd):
		self.name = name
		self.org_id = org_id
		self.org_level = org_level
		self.pswd = pswd

	def __repr__(self):
		return f"name: {self.name}"