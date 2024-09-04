#app/__init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.config[os.getenv("FLASK_ENV", "development")]')

    db.init_app(app)
    Migrate(app, db)

    from .controllers import gear_bundle_controller, gear_row_controller, user_management_controller,
system_logs_controller, bid_approval_controller
    app.register_blueprint(gear_bundle_controller.summary_bp)
    app.register_blueprint(gear_row_controller.summary_bp)
    app.register_blueprint(user_management_controller.summary_bp)
    app.register_blueprint(system_logs_controller.summary_bp)
    app.register_blueprint(bid_approval_controller.summary_bp)

    return app