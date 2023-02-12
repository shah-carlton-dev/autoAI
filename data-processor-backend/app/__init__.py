from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

from app.config import Config
from app.extensions import db
from app.models.api import API
from app.models.file import File
from app.models.job import Job
from app.models.org import Org
from app.models.user import User

# structure from https://www.digitalocean.com/community/tutorials/how-to-structure-a-large-flask-application-with-flask-blueprints-and-flask-sqlalchemy
def create_app(config=Config):
	app = Flask(__name__)
	app.config.from_object(config)

	# initialize flask extensions
	db.init_app(app)
	if len(db.metadata.tables.keys()) == 0:
		with app.app_context():
			db.create_all()

	# register blueprints
	from app.main import bp as main_bp
	app.register_blueprint(main_bp)

	from app.files import bp as files_bp
	app.register_blueprint(files_bp, url_prefix='/files')

	from app.jobs import bp as jobs_bp
	app.register_blueprint(jobs_bp, url_prefix='/jobs')

	@app.route('/test/')
	def test():
		return jsonify(True)

	return app
	