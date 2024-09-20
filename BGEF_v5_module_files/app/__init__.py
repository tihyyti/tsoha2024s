from flask import Flask
from flask_sqlalchemy import SQLAlchemy
#import psycopg2
from flask_migrate import Migrate
from config import Config
import logging
from jinja2 import Environment, FileSystemLoader
from datetime import datetime

# Configure logging
logging.basicConfig(filename='app.log', level=logging.DEBUG,
format='%(asctime)s %(levelname)s %(name)s %(message)s')
logger = logging.getLogger(__name__)

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    migrate.init_app(app, db)

    # Custom filter to format datetime
    def format_datetime(value, format="%Y-%m-%d %H:%M"):
        if value is None:
            return ""
        return datetime.strptime(value, "%Y-%m-%dT%H:%M:%S").strftime(format)

    # Register the custom filter
    app.jinja_env.filters['datetime'] = format_datetime
    print("Custom datetime filter registered")

    with app.app_context():
        # Import and register blueprints
        from routes.route_home import home_bp
        from routes.route_bidheaders import bidheaders_bp
        from routes.route_users_bidheaders_listed_by_status import users_bidheaders_by_status_bp
        from routes.route_bidheader_details import bidheader_details_bp
        from routes.route_gear_details import gear_details_bp
        from routes.route_gear_list import gear_list_bp
        from routes.route_gearlist_grouped_by_bidgenre import gearlist_grouped_by_bidgenre_bp
        from routes.route_user_list_all import user_list_all_bp
        from routes.route_user_login import user_login_bp
        from routes.route_user_by_id import user_by_id_bp
        from routes.route_user import user_profile_bp
        from routes.route_user_registration import user_registration_bp
        from routes.route_image_metadata import image_metadata_bp
        from routes.route_image_update import image_update_bp
        from routes.route_image_create import image_create_bp
        from routes.route_image_delete import image_delete_bp

        # Register blueprints
        app.register_blueprint(home_bp)
        app.register_blueprint(user_by_id_bp)
        app.register_blueprint(user_login_bp)
        app.register_blueprint(user_registration_bp)
        app.register_blueprint(user_profile_bp)
        app.register_blueprint(user_list_all_bp)
        app.register_blueprint(bidheaders_bp)
        app.register_blueprint(users_bidheaders_by_status_bp)
        app.register_blueprint(bidheader_details_bp)
        app.register_blueprint(gear_details_bp)
        app.register_blueprint(gear_list_bp)
        app.register_blueprint(gearlist_grouped_by_bidgenre_bp)
        app.register_blueprint(image_metadata_bp)
        app.register_blueprint(image_update_bp)
        app.register_blueprint(image_create_bp)
        app.register_blueprint(image_delete_bp)

    return app