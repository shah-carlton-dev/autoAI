from app.extensions import db

class Job(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	api_id = db.Column(db.Integer, db.ForeignKey('org.id'), nullable=False)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
	file_id = db.Column(db.Integer, db.ForeignKey('file.id'), nullable=False)
	status = db.Column(db.String(80), nullable=True)
	timestamp = db.Column(db.String(80), nullable=True)

	def __init__(self, api_id, user_id, file_id, status, timestamp):
		self.api_id = api_id
		self.user_id = user_id
		self.file_id = file_id
		self.status = status
		self.timestamp = timestamp

	def __repr__(self):
		return f"job: {self.id} - status: {self.status}"