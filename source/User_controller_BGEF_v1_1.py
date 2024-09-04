"""
Let’s convert the Spring Boot UserController into a Flask application with Jinja2 templates for the UI. Below, I’ll provide an example of how you can structure your Flask application and create the corresponding HTML templates:
Remember to adapt this example to your specific project requirements, add more routes for other
services, and create additional templates as needed. You can also enhance the templates with CSS
styling and additional HTML elements.
"""
Flask Application Setup:
Create a Python file (e.g., app.py) for your Flask application.
Initialize the Flask app and configure SQLAlchemy (if needed).
Define Routes (Endpoints):
Create routes for creating users, deleting users, retrieving a single user, and retrieving all users.
Implement the corresponding logic for each route.
Create Jinja2 Templates:
Create HTML templates (e.g., user.html, users.html) to render user-related information.
Below is a simplified example of how you can structure your Flask application:

from  flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@localhost/yourdatabase'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define your SQLAlchemy User model (similar to Spring Boot User entity)
# ...
# Create routes for user services

@app.route('/users', methods=['GET'])
def get_all_users():
    # Retrieve all users from the database
    # ...

    # Render the users.html template with the user data
    return render_template('users.html', users=users)

@app.route('/user/<int:user_id>', methods=['GET'])
def get_one_user(user_id):
    # Retrieve a single user by user_id from the database
    # ...

    # Render the user.html template with the user data
    return render_template('user.html', user=user)

# Define other routes for creating, deleting, and assigning users similarly

if __name__ == '__main__':
    app.run(debug=True)
"""
Create Jinja2 Templates:
Create templates directory in your project folder.
Inside the templates directory, create user.html and users.html templates.
Use Jinja2 syntax to display user-related information in these templates.

"""
<!DOCTYPE html>
<html>
<head>
    <title>User Details</title>
</head>
<body>
    <h1>User Details</h1>
    <p>User ID: {{ user.id }}</p>
    <p>User Name: {{ user.name }}</p>
    <!-- Add other user details as needed -->
</body>
</html>


<!DOCTYPE html>
<html>
<head>
    <title>All Users</title>
</head>
<body>
    <h1>All Users</h1>
    <ul>
        {% for user in users %}
            <li>User ID: {{ user.id }}, User Name: {{ user.name }}</li>
        {% endfor %}
    </ul>
</body>
</html>
