from flask import Flask
from app.extensions import db
from app.routes import register_routes
 
def create_app():
	app = Flask(__name__)
 
	# database config
	app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:root@mysql:3306/mydb"
	app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
	app.config['SECRET_KEY'] = 'your_secret_key_here'

 
	db.init_app(app)
	with app.app_context():
		db.create_all()
 
	# register all routes
	register_routes(app)
	return app