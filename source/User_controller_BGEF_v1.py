"""Here’s how you can convert the provided Spring Boot controller into a Flask controller with Jinja2 templates for user input layout.


This setup includes:

A Flask controller with routes for creating, deleting, and viewing
users.
Jinja2 templates for creating a user, viewing a single user’s details,
and listing all users."""

from flask import Flask, render_template, request, redirect, url_for
from models import db, UserService

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@localhost/yourdatabase'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

user_service = UserService()

@app.route('/crtUser', methods=['GET', 'POST'])
def create_user():
    if request.method == 'POST':
        userName = request.form['userName']
        password = request.form['password']
        user_service.create_user(userName, password)
        return redirect(url_for('get_all_users'))
    return render_template('create_user.html')

@app.route('/delUser', methods=['GET'])
def delete_user():
    userId = request.args.get('userId')
    user_service.delete_user(userId)
    return redirect(url_for('get_all_users'))

@app.route('/oneUser', methods=['GET'])
def get_one_user():
    userId = request.args.get('userId')
    user = user_service.get_one_user(userId)
    return render_template('user.html', user=user)

@app.route('/allUsers', methods=['GET'])
def get_all_users():
    users = user_service.get_all_users()
    return render_template('users.html', users=users)

@app.route('/user/pieceOfNewsHeaders/<int:pieceOfNewsHeaderId>', methods=['POST'])
def assign_user_to_news_header(pieceOfNewsHeaderId):
    userId = request.form['userId']
    if pieceOfNewsHeaderId is None or userId is None:
        return redirect(url_for('get_all_users'))
    user_service.assign_news_header_to_user(userId, pieceOfNewsHeaderId)
    return redirect(url_for('get_all_users'))

@app.route('/user/newsGenres/<int:newsGenreId>', methods=['POST'])
def assign_user_to_news_genre(newsGenreId):
    userId = request.form['userId']
    if newsGenreId is None or userId is None:
        return redirect(url_for('get_all_users'))
    user_service.assign_news_genre_to_user(userId, newsGenreId)
    return redirect(url_for('get_all_users'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)


# Jinja2 templates for user input layout.

templates/create_user.html
HTML

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Create User</title>
</head>
<body>
    <h1>Create User</h1>
    <form action="{{ url_for('create_user') }}" method="post">
        <label for="userName">Username:</label>
        <input type="text" id="userName" name="userName" required>
        <br>
        <label for="password">Password:</label>
        <input type="password" id="password" name="password" required>
        <br>
        <button type="submit">Create</button>
    </form>
</body>
</html>
AI-generated code. Review and use carefully. More info on FAQ.
templates/user.html
HTML

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>User Details</title>
</head>
<body>
    <h1>User Details</h1>
    <p>Username: {{ user.userName }}</p>
    <p>Password: {{ user.password }}</p>
    <a href="{{ url_for('get_all_users') }}">Back to Users List</a>
</body>
</html>
AI-generated code. Review and use carefully. More info on FAQ.
templates/users.html
HTML

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Users List</title>
</head>
<body>
    <h1>Users List</h1>
    <ul>
        {% for user in users %}
            <li>{{ user.userName }} - <a href="{{ url_for('get_one_user', userId=user.id) }}">Details</a></li>
        {% endfor %}
    </ul>
    <a href="{{ url_for('create_user') }}">Create New User</a>
</body>
</html>