import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
	SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, '../app.db')
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	
	# instance: auto-ai-v1
	# pw: Y&+B1rUdF%4~%U8e
	# conn string: lucid-diode-377015:us-central1:auto-ai-v1
	
	UPLOAD_FOLDER = 'data-processor-backend/uploads'
	ALLOWED_EXTENSIONS = ['csv']
