from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    migrate.init_app(app, db)

    with app.app_context():
        # Import and register blueprints
        from routes.route_home import home_bp
        from routes.route_bidheaders import bidheaders_bp
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
        app.register_blueprint(bidheader_details_bp)
        app.register_blueprint(gear_details_bp)
        app.register_blueprint(gear_list_bp)
        app.register_blueprint(gearlist_grouped_by_bidgenre_bp)
        app.register_blueprint(image_metadata_bp)
        app.register_blueprint(image_update_bp)
        app.register_blueprint(image_create_bp)
        app.register_blueprint(image_delete_bp)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
