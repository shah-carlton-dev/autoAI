import os

class _db_conn:
	PASSWORD = "Y&+B1rUdF%4~%U8e"
	PUBLIC_IP = "34.28.169.175"
	DBNAME = "prod"
	PROJECT_ID = "lucid-diode-377015"
	INSTANCE_NAME = "auto-ai-v1"
	CONN_NAME = "lucid-diode-377015:us-central1:auto-ai-v1"
	HOST = "127.0.0.1:5000"
	USER = "root"

class Config:
	BASEDIR = os.path.abspath(os.path.dirname(__file__))[:-3]

	SQLALCHEMY_TRACK_MODIFICATIONS = True
	# SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASEDIR, 'app.db')
	SQLALCHEMY_DATABASE_URI = f"mysql+mysqldb://{_db_conn.USER}:{_db_conn.PASSWORD}@{_db_conn.HOST_NAME}/{_db_conn.DBNAME}?unix_socket=/cloudsql/{_db_conn.PROJECT_ID}:{_db_conn.INSTANCE_NAME}"
	# SQLALCHEMY_DATABASE_URI = f"mysql+mysqlconnector://{_db_conn.USER}:{_db_conn.PASSWORD}@{_db_conn.HOST}/{_db_conn.DBNAME}?unix_socket=/cloudsql/{_db_conn.PROJECT_ID}:{_db_conn.INSTANCE_NAME}"

	UPLOAD_FOLDER = '/app/uploads'
	ALLOWED_EXTENSIONS = ['csv']
