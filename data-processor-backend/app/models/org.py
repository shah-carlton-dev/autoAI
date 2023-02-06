from app.extensions import db

class Org(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(80), nullable=False)
	industry = db.Column(db.String(80), nullable=True)

	def __init__(self, name, industry):
		self.name = name
		self.industry = industry

	def __repr__(self):
		return f"org: {self.name} - industry: {self.industry}"