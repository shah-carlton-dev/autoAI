from flask import Blueprint

bp = Blueprint('dispatch', __name__)


from app.dispatch import routes