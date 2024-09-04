from flask import Blueprint, render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash
from __init__ import db
import templates

# Registration
user_registration_bp = Blueprint('register', __name__)

@user_registration_bp.route('/user_reg', methods=['GET', 'POST'])
def user_reg():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        hashed_password = generate_password_hash(password, method='sha256')

        conn = None
        cursor = None
        try:
            # Establish the connection
            conn = db
            cursor = conn.cursor()
            query = "INSERT INTO users (username, email, password) VALUES (%s, %s, %s)"
            cursor.execute(query, (username, email, hashed_password))
            conn.commit()
            flash('User registered successfully!', 'success')
            return redirect(url_for('login'))
        except Exception as e:
            return render_template("error.html", notification=f"Error executing query: {e}")
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()
    else:
        return render_template('view_user_registration.html')

if __name__ == "__main__":
    from my_flask_app import create_app
    app = create_app()
    app.run(debug=True)
