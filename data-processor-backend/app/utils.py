from app.config import Config

# check if file extension in list of acceptable formats
def allowed_file(filename):
	return ('.' in filename) and \
		   filename.rsplit('.', 1)[1] in Config.ALLOWED_EXTENSIONS