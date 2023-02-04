from flask import jsonify
from app.posts import bp

@bp.route('/')
def index():
    return jsonify("hey")

@bp.route('/categories/')
def categories():
    return jsonify("posts categories")