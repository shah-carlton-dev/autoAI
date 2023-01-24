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
        return jsonify("File uploaded successfully.")
    else:
        return jsonify("Only CSV files are allowed. Found file: ", uploaded_file.filename)

@app.route('/getAllFiles', methods=['GET'])
@cross_origin(origin='*')
def get_all_files():
    all_files = File.query.all()
    files_list = []
    for file in all_files:
        files_list.append({"id": file.id, "title": file.title, "description": file.description, "model": file.model, "file_path": file.file_path, "timestamp": file.timestamp})
    return jsonify(files_list)


@app.route('/deleteFile/<file_id>', methods=['DELETE'])
@cross_origin(origin='*')
def delete_file(file_id): 
    delete_file = db.get_or_404(File, file_id)
    if os.path.exists(delete_file.file_path):
        os.remove(delete_file.file_path)
        db.session.delete(delete_file)
        db.session.commit()
    else:
        jsonify({'error','file not found'}), 404
    return "File Deleted Successfully", 200
if __name__ == "__main__":
    with app.app_context(): 
        db.create_all()
    app.run(debug=True)
