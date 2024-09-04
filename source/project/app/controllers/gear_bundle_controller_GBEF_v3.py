"""Generate now a proposal of  all the modules arranger in a file-tree-format, which could be used as an input for a interpreter and builder. Make also all scripts, which are needed to successfully complete the buiding process. Propose also possible changes in the import-part instructions for each script in the tree, which all participate the building process in this case.

A proposal for the modules arranged in a file-tree format, along with the necessary scripts and changes in the import instructions.
These updates should ensure that all the controllers and UIs are aligned with the proposed database improvements.

File Tree Structure
project/
│
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── services/python3
│   │   ├── __init__.py
│   │   ├── gear_bundle_service.py
│   │   ├── gear_row_service.py
│   │   ├── user_management_service.py
│   │   ├── system_logs_service.py
│   │   ├── bid_approval_service.py
│   ├── controllers/
│   │   ├── __init__.py
│   │   ├── gear_bundle_controller.py
│   │   ├── gear_row_controller.py
│   │   ├── user_management_controller.py
│   │   ├── system_logs_controller.py
│   │   ├── bid_approval_controller.py
│   ├── views/
│   │   ├── __init__.py
│   │   ├── create_gear_bundle.html
│   │   ├── update_gear_bundle.html
│   │   ├── my_gear_bundles.html
│   │   ├── delete_gear_bundle.html
│   │   ├── user_management.html
│   │   ├── system_logs.html
│   │   ├── bid_approval.html
│   │   ├── styles.css
│   ├── templates/
│   │   ├── base.html
│   ├──#!/bin/bash

# Create the main project directory
mkdir -p project

# Create the app directory and subdirectories
mkdir -p project/app/{services,controllers,views,templates,static/css}

# Create the migrations directory and subdirectories
mkdir -p project/migrations/versions

# Create the tests directory
mkdir -p project/tests

# Create __init__.py files
touch project/app/__init__.py
touch project/app/services/__init__.py
touch project/app/controllers/__init__.py
touch project/app/views/__init__.py
touch project/tests/__init__.py

# Create main Python files
touch project/app/models.py
touch project/config.py
touch project/manage.py
touch project/run.py

# Create HTML files
touch project/app/views/{create_gear_bundle.html,update_gear_bundle.html,my_gear_bundles.html,delete_gear_bundle.html,user_management.html,system_logs.html,bid_approval.html}

# Create CSS file
touch project/app/static/css/styles.css

# Create migration files
touch project/migrations/{env.py,script.py.mako,alembic.ini}

# Create test files
touch project/tests/{test_models.py,test_services.py,test_controllers.py}

# Print success message
echo "Module tree structure created successfully!"
│      #!/bin/bash

# Create the main project directory
mkdir -p project

# Create the app directory and subdirectories
mkdir -p project/app/{services,controllers,views,templates,static/css}

# Create the migrations directory and subdirectories
mkdir -p project/migrations/versions

# Create the tests directory
mkdir -p project/tests

# Create __init__.py files
touch project/app/__init__.py
touch project/app/services/__init__.py
touch project/app/controllers/__init__.py
touch project/app/views/__init__.py
touch project/tests/__init__.py

# Create main Python files
touch project/app/models.py
touch project/config.py
touch project/manage.py
touch project/run.py

# Create HTML files
touch project/app/views/{create_gear_bundle.html,update_gear_bundle.html,my_gear_bundles.html,delete_gear_bundle.html,user_management.html,system_logs.html,bid_approval.html}

# Create CSS file
touch project/app/static/css/styles.css

# Create migration files
touch project/migrations/{env.py,script.py.mako,alembic.ini}

# Create test files
touch project/tests/{test_models.py,test_services.py,test_controllers.py}

# Print success message
echo "Module tree structure created successfully!"
│      #!/bin/bash

# Create the main project directory
mkdir -p project

# Create the app directory and subdirectories
mkdir -p project/app/{services,controllers,views,templates,static/css}

# Create the migrations directory and subdirectories
mkdir -p project/migrations/versions

# Create the tests directory
mkdir -p project/tests

# Create __init__.py files
touch project/app/__init__.py
touch project/app/services/__init__.py
touch project/app/controllers/__init__.py
touch project/app/views/__init__.py
touch project/tests/__init__.py

# Create main Python files
touch project/app/models.py
touch project/config.py
touch project/manage.py
touch project/run.py

# Create HTML files
touch project/app/views/{create_gear_bundle.html,update_gear_bundle.html,my_gear_bundles.html,delete_gear_bundle.html,user_management.html,system_logs.html,bid_approval.html}

# Create CSS file
touch project/app/static/css/styles.css

# Create migration files
touch project/migrations/{env.py,script.py.mako,alembic.ini}

# Create test files
touch project/tests/{test_models.py,test_services.py,test_controllers.py}

# Print success message
echo "Module tree structure created successfully!"
│
├── migrations/
│   ├── versions/
│   ├── env.py
│   ├── script.py.mako
│   ├── alembic.ini
│
├── tests/
│   ├── __init__.py
│   ├── test_models.py
│   ├── test_services.py
│   ├── test_controllers.py
│
├── config.py
├── manage.py
├── requirements.txt
├── run.p
"""
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app import create_app, db

app = create_app()
migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()

#run.py

from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)

#config.py

import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY', 'mysecretkey')

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}

#Changes in Import Instructions
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

    from .controllers import gear_bundle_controller, gear_row_controller, user_management_controller, system_logs_controller, bid_approval_controller
    app.register_blueprint(gear_bundle_controller.summary_bp)
    app.register_blueprint(gear_row_controller.summary_bp)
    app.register_blueprint(user_management_controller.summary_bp)
    app.register_blueprint(system_logs_controller.summary_bp)
    app.register_blueprint(bid_approval_controller.summary_bp)

    return app

#app/models.py

from . import db
from datetime import datetime

class GearBundle(db.Model):
    __tablename__ = 'gear_bundle'
    id = db.Column(db.Integer, primary_key=True)
    bundleName = db.Column(db.String(80), nullable=False)
    price = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)

class GearRow(db.Model):
    __tablename__ = 'gear_row'
    id = db.Column(db.Integer, primary_key=True)
    bundleID = db.Column(db.Integer, db.ForeignKey('gear_bundle.id'), nullable=False)
    # Other fields...

class UserManagement(db.Model):
    __tablename__ = 'user_management'
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    is_active = db.Column(db.Boolean, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)

class SystemLogs(db.Model):
    __tablename__ = 'system_logs'
    log_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    username = db.Column(db.String(80))
    action = db.Column(db.String(255))
    timestamp = db.Column(db.DateTime)
    details = db.Column(db.Text)

class BidApproval(db.Model):
    __tablename__ = 'bid_approval'
    bid_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    userName = db.Column(db.String(80))
    content = db.Column(db.Text)
    sendTime = db.Column(db.DateTime)
    status = db.Column(db.String(20))

#app/services/__init__.py
#This file can be left empty or used to initialize the services package
#app/services/gear_bundle_service.py

from datetime import datetime
from app.models import db, GearBundle

class GearBundleService:
    @staticmethod
    def create_gear_bundle(data):
        new_bundle = GearBundle(
            bundleName=data['bundleName'],
            price=data['price'],
            created_at=datetime.utcnow()
        )
        db.session.add(new_bundle)
        db.session.commit()
        return new_bundle

    @staticmethod
    def update_gear_bundle(bundle_id, data):
        bundle = GearBundle.query.get(bundle_id)
        if bundle:
            bundle.bundleName = data.get('bundleName', bundle.bundleName)
            bundle.price = data.get('price', bundle.price)
            bundle.updated_at = datetime.utcnow()
            db.session.commit()
        return bundle

    @staticmethod
    def delete_gear_bundle(bundle_id):
        bundle = GearBundle.query.get(bundle_id)
        if bundle:
            db.session.delete(bundle)
            db.session.commit()
        return bundle

    @staticmethod
    def get_my_gear_bundles():
        return GearBundle.query.all()

#app/services/gear_row_service.py

from app.models import db, GearRow

class GearRowService:
    @staticmethod
    def create_gear_row(data):
        new_row = GearRow(
            bundleID=data['bundleID'],
            # Other fields...
        )
        db.session.add(new_row)
        db.session.commit()
        return new_row

    @staticmethod
    def update_gear_row(row_id, data):
        row = GearRow.query.get(row_id)
        if row:
            row.bundleID = data.get('bundleID', row.bundleID)
            # Update other fields...
            db.session.commit()
        return row

    @staticmethod
    def delete_gear_row(row_id):
        row = GearRow.query.get(row_id)
        if row:
            db.session.delete(row)
            db.session.commit()
        return row

#app/services/user_management_service.py

from app.models import db, UserManagement

class UserManagementService:
    @staticmethod
    def get_all_users():
        return UserManagement.query.all()

    @staticmethod
    def update_user(user_id, data):
        user = UserManagement.query.get(user_id)
        if user:
            user.username = data.get('username', user.username)
            user.email = data.get('email', user.email)
            user.is_active = data.get('is_active', user.is_active)
            db.session.commit()
        return user

#app/services/system_logs_service.py

from app.models import db, SystemLogs

class SystemLogsService:
    @staticmethod
    def get_system_logs():
        return SystemLogs.query.all()

#app/services/bid_approval_service.py

from app.models import db, BidApproval

class BidApprovalService:
    @staticmethod
    def get_pending_bids():
        return BidApproval.query.all()

    @staticmethod
    def update_bid_status(bid_id, status):
        bid = BidApproval.query.get(bid_id)
        if bid:
            bid.status = status
            db.session.commit()
        return bid

#app/controllers/__init__.py
# This file can be left empty or used to initialize the controllers package

#app/controllers/gear_bundle_controller.py

from flask import request, jsonify, Blueprint
from app.services.gear_bundle_service import GearBundleService

summary_bp = Blueprint('gear_bundle', __name__)

@summary_bp.route('/create_gear_bundle', methods=['POST'])
def create_gear_bundle():
    data = request.json
    new_bundle = GearBundleService.create_gear_bundle(data)
    return jsonify(new_bundle.to_dict()), 201

@summary_bp.route('/update_gear_bundle/<int:bundle_id>', methods=['PUT'])
def update_gear_bundle(bundle_id):
    data = request.json
    updated_bundle = GearBundleService.update_gear_bundle(bundle_id, data)
    return jsonify(updated_bundle.to_dict()) if updated_bundle else ('', 404)

@summary_bp.route('/delete_gear_bundle/<int:bundle_id>', methods=['DELETE'])
def delete_gear_bundle(bundle_id):
    deleted_bundle = GearBundleService.delete_gear_bundle(bundle_id)
    return jsonify(deleted_bundle.to_dict()) if deleted_bundle else ('', 404)

@summary_bp.route('/my_gear_bundles', methods=['GET'])
def get_my_gear_bundles():
    bundles = GearBundleService.get_my_gear_bundles()
    return jsonify([bundle.to_dict() for bundle in bundles])

#app/controllers/gear_row_controller.py

from flask import request, jsonify, Blueprint
from app.services.gear_row_service import GearRowService

summary_bp = Blueprint('gear_row', __name__)

@summary_bp.route('/create_gear_row', methods=['POST'])
def create_gear_row():
    data = request.json
    new_row = GearRowService.create_gear_row(data)
    return jsonify(new_row.to_dict()), 201

@summary_bp.route('/update_gear_row/<int:row_id>', methods=['PUT'])
def update_gear_row(row_id):
    data = request.json
    updated_row = GearRowService.update_gear_row(row_id, data)
    return jsonify(updated_row.to_dict()) if updated_row else ('', 404)

@summary_bp.route('/delete_gear_row/<int:row_id>', methods=['DELETE'])
def delete_gear_row(row_id):
    deleted_row = GearRowService.delete_gear_row(row_id)
    return jsonify(deleted_row.to_dict()) if deleted_row else ('', 404)

#app/controllers/user_management_controller.py

from flask import request, jsonify, Blueprint
from app.services.user_management_service import UserManagementService

summary_bp = Blueprint('user_management', __name__)

@summary_bp.route('/users', methods=['GET'])
def get_all_users():
    users = UserManagementService.get_all_users()
    return jsonify([user.to_dict() for user in users])

@summary_bp.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.json
    user = UserManagementService.update_user(user_id, data)
    return jsonify(user.to_dict()) if user else ('', 404)

#app/controllers/system_logs_controller.py

from flask import request, jsonify, Blueprint
from app.services.system_logs_service import SystemLogsService

summary_bp = Blueprint('system_logs', __name__)

@summary_bp.route('/system_logs', methods=['GET'])
def get_system_logs():
    logs = SystemLogsService.get_system_logs()
    return jsonify([log.to_dict() for log in logs])

#app/controllers/bid_approval_controller.py

from flask import request, jsonify, Blueprint
from app.services.bid_approval_service import BidApprovalService

summary_bp = Blueprint('bid_approval', __name__)

@summary_bp.route('/pending_bids', methods=['GET'])
def get_pending_bids():
    bids = BidApprovalService.get_pending_bids()
    return jsonify([bid.to_dict() for bid in bids])

@summary_bp.route('/pending_bids/<int:bid_id>', methods=['PUT'])
def update_bid_status(bid_id):
    data = request.json
    status = data.get('status')
    bid = BidApprovalService.update_bid_status(bid_id, status)
    return jsonify(bid.to_dict()) if bid else ('', 404)

#HTML and CSS
#app/views/create_gear_bundle.html

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Create Gear Bundle</title>
    <link rel="stylesheet" href="/static/css/styles.css">
</head>
<body>
    <div class="container">
        <h1>Create Gear Bundle</h1>
        <form id="create-gear-bundle-form">
            <label for="bundleName">Bundle Name:</label>
            <input type="text" id="bundleName" name="bundleName" required>
            <label for="price">Price (€):</label>
            <input type="number" id="price" name="price" required>
            <button type="submit">Create Bundle</button>
        </form>
    </div>
    <script>
        document.getElementById('create-gear-bundle-form').addEventListener('submit', function(event) {
            event.preventDefault();
            const formData = new FormData(event.target);
            const data = Object.fromEntries(formData.entries());
            fetch('/create_gear_bundle', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(data)
            })
            .then(response => response.json())
            .then(data => {
                alert('Gear bundle created successfully!');
                event.target.reset();
            });
        });
    </script>
</body>
</html>

#app/views/update_gear_bundle.html

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Update Gear Bundle</title>
    <link rel="stylesheet" href="/static/css/styles.css">
</head>
<body>
    <div class="container">
        <h1>Update Gear Bundle</h1>
        <form id="update-gear-bundle-form">
            <label for="bundleId">Bundle ID:</label>
            <input type="number" id="bundleId" name="bundleId" required>
            <label for="bundleName">Bundle Name:</label>
            <input type="text" id="bundleName" name="bundleName">
            <label for="price">Price (€):</label>
            <input type="number" id="price" name="price">
            <button type="submit">Update Bundle</button>
        </form>
    </div>
    <script>
        document.getElementById('update-gear-bundle-form').addEventListener('submit', function(event) {
            event.preventDefault();
            const formData = new FormData(event.target);
            const data = Object.fromEntries(formData.entries());
            const bundleId = data.bundleId;
            delete data.bundleId;
            fetch(`/update_gear_bundle/${bundleId}`, {
                method: 'PUT',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(data)
            })
            .then(response => response.json())
            .then(data => {
                alert('Gear bundle updated successfully!');
                event.target.reset();
            });
        });
    </script>
</body>
</html>

#app/views/my_gear_bundles.html


<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Gear Bundles</title>
    <link rel="stylesheet" href="/static/css/styles.css">
</head>
<body>
    <div class="container">
        <h1>My Gear Bundles</h1>
        <table>
            <thead>
                <tr>
                    <th>Bundle ID</th>
                    <th>Bundle Name</th>
                    <th>Price (€)</th>
                    <th>Total Items</th>
                </tr>
            </thead>
            <tbody id="my-gear-bundles">
                <!-- Data will be populated here -->
            </tbody>
        </table>
    </div>
    <script>
        fetch('/my_gear_bundles')
            .then(response => response.json())
            .then(data => {
                const tableBody = document.getElementById('my-gear-bundles');
                data.forEach(item => {
                    const row = document.createElement('tr');
                    row.innerHTML = `
                        <td>${item.bundle_id}</td>
                        <td>${item.bundleName}</td>
                        <td>${item.price}</td>
                        <td>${item.total_items}</td>
                    `;
                    tableBody.appendChild(row);
                });
            });
    </script>
</body>
</html>

#app/views/delete_gear_bundles.html

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Delete Gear Bundle</title>
    <link rel="stylesheet" href="/static/css/styles.css">
</head>
<body
    <div class="container">
        <h1>Delete Gear Bundle</h1>
        <form id="delete-gear-bundle-form">
            <label for="bundleId">Bundle ID:</label>
            <input type="number" id="bundleId" name="bundleId" required>
            <button type="submit">Delete Bundle</button>
        </form>
    </div>
    <script>
        document.getElementById('delete-gear-bundle-form').addEventListener('submit', function(event) {
            event.preventDefault();
            const formData = new FormData(event.target);
            const bundleId = formData.get('bundleId');
            fetch(`/delete_gear_bundle/${bundleId}`, {
                method: 'DELETE'
            })
            .then(response => response.json())
            .then(data => {
                alert('Gear bundle deleted successfully!');
                event.target.reset();
            });
        });
    </script>
</body>
</html>

#CSS (styles.css)

body {
    font-family: Arial, sans-serif;
    background-color: #f4f4f4;
    margin: 0;
    padding: 0;
}

.container {
    width: 80%;
    margin: auto;
    overflow: hidden;
}

h1 {
    color: #333;
    text-align: center;
    margin-top: 20px;
}

form {
    display: flex;
    flex-direction: column;
    gap: 10px;
    margin: 20px 0;
}

label {
    font-weight: bold;
}

input, button {
    padding: 10px;
    font-size: 16px;
}

button {
    background-color: #5cb85c;
    color: white;
    border: none;
    cursor: pointer;
}

button:hover {
    background-color: #4cae4c;
}

table {
    width: 100%;
    border-collapse: collapse;
    margin: 20px 0;
}

table, th, td {
    border: 1px solid #ddd;
}

th, td {
    padding: 10px;
    text-align: left;
}

th {
    background-color: #f2f2f2;
    font-weight: bold;
}

tr:nth-child(even) {
    background-color: #f9f9f9;
}

tr:hover {
    background-color: #f1f1f1;
}
