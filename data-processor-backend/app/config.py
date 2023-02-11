import os

class _db_conn:
	PASSWORD = "Y&+B1rUdF%4~%U8e"
	PUBLIC_IP = "34.28.169.175"
	DBNAME = "prod"
	PROJECT_ID = "lucid-diode-377015"
	INSTANCE_NAME = "auto-ai-v1"

class Config:
	BASEDIR = os.path.abspath(os.path.dirname(__file__))[:-3]

	SQLALCHEMY_TRACK_MODIFICATIONS = False
	# SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASEDIR, 'app.db')
	SQLALCHEMY_DATABASE_URI = f"mysql+mysqldb://root@/{_db_conn.DBNAME}?unix_socket=/cloudsql/{_db_conn.PROJECT_ID}:{_db_conn.INSTANCE_NAME}"
	
	UPLOAD_FOLDER = '/app/uploads'
	ALLOWED_EXTENSIONS = ['csv']
