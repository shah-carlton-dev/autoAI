import os
import sys
from datetime import datetime
from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin
app = Flask(__name__)

CORS(app)

app.config['UPLOAD_FOLDER'] = 'data-processor-backend/uploads'
app.config['ALLOWED_EXTENSIONS'] = ['csv']
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

# create class File which sets table requirements
class File(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    description = db.Column(db.String(120))
    model = db.Column(db.String(120))
    file_path = db.Column(db.String(120))
    timestamp = db.Column(db.String(120))

    def __init__(self, title, description, model, file_path, timestamp):
        self.title = title
        self.description = description
        self.model = model
        self.file_path = file_path
        self.timestamp = timestamp


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']

# POST new file 
# request = multipart form with file
# returns = {msg:"information about the rquest outcome", status:<http code>}
@app.route('/uploadFile', methods=['POST'])
@cross_origin(origin='*')
def upload_file():
    title = request.form.get('title')
    description = request.form.get('description')
    model = request.form.get('model')
    uploaded_file = request.files['file']
    if uploaded_file and allowed_file(uploaded_file.filename):
        filename = secure_filename(uploaded_file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file_name, file_extension = os.path.splitext(file_path)
        uploaded_file.save(file_name+'_'+timestamp+file_extension)
        file_path = file_name+'_'+timestamp+file_extension
        new_file = File(title, description, model, file_path, timestamp)
        db.session.add(new_file)
        db.session.commit()
        return jsonify({"msg": "File uploaded successfully.", "status":200})
    else:
        return jsonify({"msg":f"Only CSV files are allowed. Found file: {uploaded_file.filename}","status": 400})

# helper fn - paginate files
# params = page (pg number), per_page (size of each page)
# returns = files list of page and meta data
def paginate_helper(page, per_page):
    file_page = File.query.paginate(page=page, per_page=per_page)
    files_list = []
    for file in file_page:
        files_list.append({
            "id": file.id, 
            "title": file.title, 
            "description": file.description,
            "model": file.model, 
            "file_path": file.file_path, 
            "timestamp": file.timestamp})
    meta = ({
        "page":file_page.page, 
        "total":file_page.total, 
        "pages":file_page.pages, 
        "has_prev":file_page.has_prev, 
        "has_next":file_page.has_next})
    return {"files": files_list, "meta": meta}

# DET all files on page
# request = {page, per_page} 
# returns = {files_list: [list of docs on page], meta: {meta data about page list}}
@app.route('/getAllFiles', methods=['GET'])
@cross_origin(origin='*')
def get_all_files():
    page = request.args.get('page')
    per_page = request.args.get('per_page')
    return jsonify(paginate_helper(page, per_page))

# DELETE file 
# request = {file_id, page, per_page} 
# returns = {success: true/false, files_list: [list of docs on page], meta: {meta data about page list}}
@app.route('/deleteFile', methods=['DELETE'])
@cross_origin(origin='*')
def delete_file():
    file_id = request.args.get('file_id')
    page = request.args.get('page')
    per_page = request.args.get('per_page')
    success = True
    delete_file = db.get_or_404(File, file_id)
    if os.path.exists(delete_file.file_path):
        os.remove(delete_file.file_path)
        db.session.delete(delete_file)
        db.session.commit()
    else:
        success = False
    paginated = paginate_helper(page, per_page)
    return jsonify({"success":success, "files": paginated['files'], "meta": paginated['meta']})

# DELETE all - remove uploads and create new

# GET a file for download


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)