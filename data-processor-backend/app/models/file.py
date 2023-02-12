from app.extensions import db

class File(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(80))
	description = db.Column(db.String(120))
	file_path = db.Column(db.String(120))
	file_name = db.Column(db.String(120))
	timestamp = db.Column(db.String(120))
	owner_id = db.Column(db.Integer, db.ForeignKey('user.id'))
	# owner = db.relationship('User', backref='User', lazy=True, uselist=False)

	def __init__(self, title, description, model, file_path, file_name, timestamp):
		self.title = title
		self.description = description
		self.model = model
		self.file_path = file_path
		self.file_name = file_name
		self.timestamp = timestamp

	def __repr__(self):
		return f"filename: {self.title} - filepath: {self.file_path}"