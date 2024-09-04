from flask import Blueprint, render_template
from __init__ import db
import templates

gear_list_bp = Blueprint('gear_list', __name__)

@gear_list_bp.route('/gears')
def gear_list():
    conn = None
    cursor = None
    try:
        # Establish the connection
        conn = db
        cursor = conn.cursor()
        query = "SELECT * FROM Gear"
        cursor.execute(query)
        gears = cursor.fetchall()
    except Exception as e:
        return render_template("error.html", notification=f"Error executing query: {e}")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

    return render_template('view_gear_list.html', gears=gears)

if __name__ == "__main__":
    from my_flask_app import create_app
    app = create_app()
    app.run(debug=True)
