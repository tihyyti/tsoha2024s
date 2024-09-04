
from flask import Blueprint, render_template
# import psycopg2
# from psycopg2 import sql
from __init__ import db
import templates

user_by_id_bp = Blueprint('get_user_by_id', __name__)

@user_by_id_bp.route('/user_by_id', methods=['GET', 'POST'])
def get_user_by_id(user_id):
    conn = db
    if conn:
        cursor = conn.cursor()
        int_user_id = int(user_id)
        query = "SELECT * FROM Client WHERE id = %s"
        cursor.execute(query, (int_user_id,))
        user_data = cursor.fetchone()
        cursor.close()
        conn.close()
        if user_data:
            render_template("view_user.html", user=user_data)
    else:
        return render_template("error.html", notification="User not found")
        return redirect(f"/")

if __name__ == "__main__":
    app.run(debug=True)