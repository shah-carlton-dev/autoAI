import os
from datetime import datetime

from flask import jsonify, request
from app.jobs import bp
from flask_cors import cross_origin

from app.models.job import Job
from app.models.file import File
from app.extensions import db

# POST new job
# request = json - {api_id, file_id, user_id}
# returns = {message:"information about the request outcome", status:<http code>}
@bp.route('/create', methods=['POST'])
@cross_origin(origin='*')
def create_job():
	api_id = request.json["api_id"]
	file_id = request.json["file_id"]
	user_id = request.json["user_id"]
	if api_id and file_id and user_id:
		new_job = Job(api_id = api_id, file_id = file_id, user_id = user_id)
		db.session.add(new_job)
		db.session.commit()
		return jsonify({"message": "Job created successfully.", "status": 200})
	else:
		return jsonify({"message": f"missing input - check that api, file, and user IDs are valid", "status": 400})
	
def dispatch_fn():
	None

# POST dispatch requests
# request = {file_id, issuer_id, models=[{api_id, params:{param: value, param: value, ... }}, ... ]}
# returns = "hey"
@bp.route('/dispatch')
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
		new_job = Job(apid_id = api_doc.id, file_id = file_doc.id, user_id = issuer_id)
		db.session.add(new_job)
		db.session.flush()

		# send dispatch (job_id, api url, file path, params)
		dispatch_fn(new_job.id, api_doc.url, file_path, r.params)
		
		db.session.commit()

	
	return jsonify("hey")
