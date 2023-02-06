from app.extensions import db

class API(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(80))
	description = db.Column(db.String(120))
	key = db.Column(db.String(120), nullable=False)
	owner_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
	url = db.Column(db.String(120))
	endpoint = db.Column(db.String(120))
	notes = db.Column(db.String(120))
	billing = db.Column(db.String(120))

	def __init__(self, name, description, key, owner_id, url, endpoint, notes, billing):
		self.name = name
		self.description = description
		self.key = key
		self.owner_id = owner_id
		self.url = url
		self.endpoint = endpoint
		self.notes = notes
		self.billing = billing

	def __repr__(self):
		return f"api: {self.name} - url: {self.url}"