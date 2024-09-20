
# Main Python Module (run.py)
# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# import db from __init__.py #ensures the User model can be registered with the database.

# Main Python Module (run.py)
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from __init__ import create_app, db

app = create_app()

#app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@localhost:5432/testdb'

# db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)

if __name__ == '__main__':
    app.run(debug=True)

# Routes:
# from routes.route_home import home_bp
# from routes.route_bidheaders import bidheaders_bp
# from routes.route_bidheader_details import bidheader_details_bp
# from routes.route_gear_details import gear_details_bp
# from routes.route_gear_list import gear_list_bp
# from routes.route_gearlist_grouped_by_bidgenre import gearlist_grouped_by_bidgenre_bp
# from routes.route_user_list_all import user_list_all_bp
# from routes.route_user_login import user_login_bp
# from routes.route_user_by_id import user_by_id_bp
# from routes.route_user import user_profile_bp
# from routes.route_user_registration import user_registration_bp
# from routes.route_users_bidheaders_listed_by_status import users_bidheaders_by_status_bp
# from routes.route_image_metadata import image_metadata_bp
# from routes.route_image_update import image_update_bp
# from routes.route_image_create import image_create_bp
# from routes.route_image_delete import image_delete_bp

#Registration of routes
# home_bp = Blueprint('home', __name__)
# user_by_id_bp = Blueprint('user_by_id', __name__)
# user_profile_bp = Blueprint('user_profile', __name__)
# user_login_bp = Blueprint('user_login', __name__)
# user_registration_bp = Blueprint('user_registration', __name__)
# user_list_all_bp = Blueprint('user_list_all', __name__)
# bid_headers_bp = Blueprint('bid_headers', __name__)
# bidheader_details_bp = Blueprint('bidheader_details', __name__)
# users_bidheaders_by_status_bp = Blueprint('users_bidheaders_by_status', __name__)
# gear_list_bp = Blueprint('gear_list', __name__)
# gearlist_grouped_by_bidgenre_bp = Blueprint('gearlist_grouped_by_bidgenre', __name__)
# gear_details_bp = Blueprint('gear_details', __name__)

# Register routes:
# app.register_blueprint(home_bp)#+
# app.register_blueprint(user_by_id_bp)#+
# app.register_blueprint(user_login_bp)#+
# app.register_blueprint(user_registration_bp)#+
# app.register_blueprint(user_profile_bp)#+
# app.register_blueprint(user_list_all_bp)#+
# app.register_blueprint(bidheaders_bp)#+
# app.register_blueprint(bidheader_details_bp)#+
# app.register_blueprint(gear_details_bp)#+
# app.register_blueprint(gear_list_bp)#+
# app.register_blueprint(gearlist_grouped_by_bidgenre_bp)#+
# app.register_blueprint(users_bidheaders_by_status_bp)#+
# app.register_blueprint(image_metadata_bp)#+
# app.register_blueprint(image_update_bp)#+
# app.register_blueprint(image_create_bp)#+
# app.register_blueprint(image_delete_bp)#+
#