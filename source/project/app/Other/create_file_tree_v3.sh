#!/bin/bash

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
touch project/app/views/{create_gear_bundle.html,update_gear_bundle.html,my_
html,delete_gear_bundle.html,user_management.html,system_logs.html,bid_appro

# Create CSS file
touch project/app/static/css/styles.css

# Create migration files
touch project/migrations/{env.py,script.py.mako,alembic.ini}

# Create test files
touch project/tests/{test_models.py,test_services.py,test_controllers.py}

# Print success message
echo "Module tree structure created successfully!"