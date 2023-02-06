from flask import jsonify, request
from app.dispatch import bp

from app.models.file import File
from app.models.job import Job
from app.models.api import API
from app.extensions import db

def dispatch_fn():
	None

# POST dispatch requests
# request = {file_id, issuer_id, models=[{api_id, params:{param: value, param: value, ... }}, ... ]}
# returns = "hey"
@bp.route('/')
def dispatch():
	# ingest model run info
	file_id = request.json["file_id"]
	issuer_id = request.json["issuer_id"]
	model_runs = request.json["models"]

	file_doc = db.get_or_404(File, file_id)
	file_path = file_doc.file_path

	for r in model_runs:
		api_doc = db.get_or_404(API, r.api_id)

		# create job record
		new_job = Job(api_doc.id, file_doc.id, issuer_id)
		db.session.add(new_job)
		db.session.commit()

		# send dispatch (api url, file path, params)
		dispatch_fn(api_doc.url, file_path, r.params)

	
	return jsonify("hey")