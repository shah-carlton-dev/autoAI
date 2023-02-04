from flask import jsonify
from app.dispatch import bp

@bp.route('/')
def dispatch():
	
    return jsonify("hey")