from flask import Flask

from app.config import Config
from app.extensions import db

# structure from https://www.digitalocean.com/community/tutorials/how-to-structure-a-large-flask-application-with-flask-blueprints-and-flask-sqlalchemy

def create_app(config_class=Config):
	app = Flask(__name__)
	app.config.from_object(config_class)

	# initialize flask extensions
	db.init_app(app)

	# register blueprints
	from app.main import bp as main_bp
	app.register_blueprint(main_bp)

	from app.dispatch import bp as disp_bp
	app.register_blueprint(disp_bp, url_prefix='/dispatch')

	from app.files import bp as files_bp
	app.register_blueprint(files_bp, url_prefix='/files')

	@app.route('/test/')
	def test():
		return True

	return app