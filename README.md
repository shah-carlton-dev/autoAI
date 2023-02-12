# autoAI
 
to create local db - run below in flask shell after starting flask app
from app.models.api import API
from app.models.org import Org
from app.models.user import User
from app.models.file import File
from app.models.job import Job
db.drop_all()
db.create_all()

see link on how to install dependencies for mysql -
https://stackoverflow.com/questions/25865270/how-to-install-python-mysqldb-module-using-pip