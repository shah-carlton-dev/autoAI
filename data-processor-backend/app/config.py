import os

class Config:
	BASEDIR = os.path.abspath(os.path.dirname(__file__))[:-3]
	SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASEDIR, 'app.db')
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	
	# instance: auto-ai-v1
	# pw: Y&+B1rUdF%4~%U8e
	# conn string: lucid-diode-377015:us-central1:auto-ai-v1
	
	UPLOAD_FOLDER = '/app/uploads'
	ALLOWED_EXTENSIONS = ['csv']
