from flask import jsonify, request
from app.dispatch import bp

# POST dispatch requests
# request = {file_id, issuer_id, models=[{model_id, {param: value, param: value, ... }}, ... ]}
# returns = "hey"
@bp.route('/')
def dispatch():
	# ingest model run info
	# create job record
	# send dispatch (api url, file path, params)

	file_id = request.json["file_id"]
	issuer_id = request.json["issuer_id"]
	model_runs = request.json["models"]
	for r in model_runs:
		None
	return jsonify("hey")