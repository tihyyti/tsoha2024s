from flask import Blueprint, render_template, request, redirect, url_for, flash
from werkzeug.security import check_password_hash
from __init__ import db
import templates

user_login_bp = Blueprint('login', __name__)

@user_login_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = None
        cursor = None
        try:
            # Establish the connection
            conn = db
            cursor = conn.cursor()
            query = "SELECT id, password FROM users WHERE username = %s"
            cursor.execute(query, (username,))
            user_data = cursor.fetchone()
        except Exception as e:
            return render_template("error.html", notification=f"Error executing query: {e}")
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

        if user_data and check_password_hash(user_data[1], password):
            # Set session or JWT token for authentication
            # return redirect(url_for('dashboard'))
            return redirect(url_for('home'))
        else:
            flash('Invalid credentials. Please try again.')

    return render_template('login.html')

if __name__ == "__main__":
    from my_flask_app import create_app
    app = create_app()
    app.run(debug=True)
