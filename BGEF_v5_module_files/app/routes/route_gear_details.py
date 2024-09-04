from flask import Blueprint, render_template
from __init__ import db
import templates

gear_details_bp = Blueprint('gear_details', __name__)

@gear_details_bp.route('/gear/<int:gear_id>')
def gear_details(gear_id):
    conn = None
    cursor = None
    try:
        # Establish the connection
        conn = db
        cursor = conn.cursor()
        query = "SELECT * FROM Gear WHERE id = %s"
        cursor.execute(query, (gear_id,))
        gear = cursor.fetchone()
    except Exception as e:
        return render_template("error.html", notification=f"Error executing query: {e}")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

    if gear:
        return render_template('view_gear_details.html', gear=gear)
    else:
        return render_template("error.html", notification="Gear not found")
