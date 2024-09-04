#!/bin/bash

# Create the main project_BGEFv4 directory
mkdir -p project_BGEFv4

# Create the app directory and subdirectories
mkdir -p project_BGEFv4/app/{static,templates,__init__.py,routes,models}

# Create the migrations directory and subdirectories
mkdir -p project_BGEFv4/migrations/versions

# Create the tests directory
mkdir -p project_BGEFv4/tests

# Create __init__.py files
#touch project_BGEFv4/app/__init__.py
#touch project_BGEFv4/app/services/__init__.py
touch project_BGEFv4/app/routes/__init__.py
touch project_BGEFv4/app/models/__init__.py
touch project_BGEFv4/tests/__init__.py

# Create main Python files
touch project_BGEFv4/app/models.py
touch project_BGEFv4/config.py
touch project_BGEFv4/manage.py
touch project_BGEFv4/run.py

Create HTML files
# # touch project_BGEFv4/app/views/{create_gear_bundle.html,update_gear_bundle.html,my_gear_bundles.html,delete_gear_bundle.html,user_management.html,system_logs.html,bid_approval.html}

# Create CSS file
#touch project_BGEFv4/app/static/css/styles.css

# Create migration files
touch project_BGEFv4/migrations/{env.py,script.py.mako,alembic.ini}

# Create test files
touch project_BGEFv4/tests/{test_models.py,test_services.py,test_controllers.py}

# Print success message
echo "Module tree structure created successfully!"