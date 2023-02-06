import os
from datetime import datetime

from flask import jsonify, request
from app.jobs import bp
from flask_cors import cross_origin

from app.models.job import Job
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
		timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
		status = "started"
		new_job = Job(api_id, file_id, user_id, status, timestamp)
		db.session.add(new_job)
		db.session.commit()
		return jsonify({"message": "Job created successfully.", "status": 200})
	else:
		return jsonify({"message": f"missing input - check that api, file, and user IDs are valid", "status": 400})