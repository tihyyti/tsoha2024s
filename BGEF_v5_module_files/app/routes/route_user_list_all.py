from flask import Blueprint, render_template
from __init__ import db
import templates

# Define routes for the user-related list all-functionality:
user_list_all_bp = Blueprint('user_list', __name__)

@user_list_all_bp.route('/users')
def user_list():
    conn = None
    cursor = None
    try:
        # Establish the connection
        conn = db
        cursor = conn.cursor()
        query = "SELECT * FROM vw_users"
        cursor.execute(query)
        users = cursor.fetchall()
    except Exception as e:
        return render_template("error.html", notification=f"Error executing query: {e}")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

    return render_template('view_user_list.html', users=users)

if __name__ == "__main__":
    from my_flask_app import create_app
    app = create_app()
    app.run(debug=True)
