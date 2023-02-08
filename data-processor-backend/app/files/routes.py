import os
import uuid
from datetime import datetime
from glob import glob

from flask import jsonify, request, send_file
from app.files import bp
from flask_cors import cross_origin
from werkzeug.utils import secure_filename

from app.models.file import File
from app.extensions import db
from app.config import Config
from app.utils import allowed_file

# POST new file
# request = multipart form with file
# returns = {message:"information about the request outcome", status:<http code>}
@bp.route('/upload', methods=['POST'])
@cross_origin(origin='*')
def upload_file():
	title = request.form.get('title')
	description = request.form.get('description')
	uploaded_file = request.files.getlist('filepond')[0]
	print(request.form.get('filepond'))
	
	if uploaded_file and allowed_file(uploaded_file.filename):
		file_name = secure_filename(uploaded_file.filename)
		file_name, file_extension = os.path.splitext(file_name)
		file_name += f'_{datetime.now().strftime("%Y-%m-%d_%H:%M:%S")}'
		file_name += file_extension
		file_path = os.path.join(Config.UPLOAD_FOLDER, file_name)
		uploaded_file.save(Config.BASEDIR + file_path)

		new_file = File(title, description, file_path, file_name, datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
		db.session.add(new_file)
		db.session.commit()
		return jsonify({"message": "File uploaded successfully.", "status": 200})
	else:
		return {"message": f"Only CSV files are allowed. Found file: {uploaded_file.filename}", "status": 400}, 400

# GET all files on page
# request = {page, per_page}
# returns = {files_list: [list of docs on page], meta: {meta data about page list}}
@bp.route('/getAll', methods=['GET'])
@cross_origin(origin='*')
def get_all():
	page = request.args.get('page')
	per_page = request.args.get('per_page')
	file_page = File.query.paginate(page=page, per_page=per_page)
	files_list = []
	for file in file_page:
		files_list.append({
			"id": file.id,
			"title": file.title,
			"description": file.description,
			"model": file.model,
			"file_path": file.file_path,
			"file_name":file.file_name,
			"timestamp": file.timestamp})
	meta = ({
		"page": file_page.page,
		"total": file_page.total,
		"pages": file_page.pages,
		"has_prev": file_page.has_prev,
		"has_next": file_page.has_next})
	return jsonify({"files": files_list, "meta": meta})

# DELETE file
# request = {file_id, page, per_page}
# returns = {success: true/false, files_list: [list of docs on page], meta: {meta data about page list}}
@bp.route('/delete', methods=['DELETE'])
@cross_origin(origin='*')
def delete_file():
	file_id = request.json["file_id"]
	page = request.json["page"]
	per_page = request.json["per_page"]
	success = True
	delete_file = db.get_or_404(File, file_id)
	if os.path.exists('../'+delete_file.file_path):
		os.remove('../'+delete_file.file_path)
		db.session.delete(delete_file)
		db.session.commit()
	else:
		success = False
	file_page = File.query.paginate(page=page, per_page=per_page)
	files_list = []
	for file in file_page:
		files_list.append({
			"id": file.id,
			"title": file.title,
			"description": file.description,
			"model": file.model,
			"file_path": file.file_path,
			"file_name":file.file_name,
			"timestamp": file.timestamp})
	meta = ({
		"page": file_page.page,
		"total": file_page.total,
		"pages": file_page.pages,
		"has_prev": file_page.has_prev,
		"has_next": file_page.has_next})
	paginated = {"files": files_list, "meta": meta}
	return jsonify({"success": success, "files": paginated['files'], "meta": paginated['meta']})

# DELETE all files
# request = no body
# returns = {success: true/false, files_deleted: deleted file count}
@bp.route('/deleteAll', methods=['DELETE'])
@cross_origin(origin='*')
def delete_all_files():
	files = glob('../'+Config.UPLOAD_FOLDER+"/*")
	for fl in files:
		os.remove(fl)
	delete = File.query.delete()
	db.session.commit()
	return jsonify({"success": True, "files_deleted": delete})

# GET file for download
# request = {file_id}
# returns = file for download OR {message:"information about the request outcome", status:<http code>, file:file_id received}
@bp.route('/download', methods=['GET'])
@cross_origin(origin='*')
def download_file():
	file_id = request.json["file_id"]
	file_doc = db.get_or_404(File, file_id)
	print(file_doc)
	if (file_doc is not None) and (os.path.exists('../'+file_doc.file_path)):
		return send_file("../uploads/"+file_doc.file_name, download_name=file_doc.title,as_attachment=True)
	else:
		return {"status": 404, "message":"file not found", "file":file_id}, 404