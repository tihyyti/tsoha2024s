from flask import Blueprint, render_template
from __init__ import db
import templates

gearlist_grouped_by_bidgenre_bp = Blueprint('gear_by_bidgenre', __name__)

@gearlist_grouped_by_bidgenre_bp.route('/gear_by_bidgenre')
def gear_by_bidgenre():
    conn = None
    cursor = None
    try:
        # Establish the connection
        conn = db
        cursor = conn.cursor()
        query = "SELECT * FROM vw_gear_by_genre"
        cursor.execute(query)
        gear_by_genre = cursor.fetchall()
    except Exception as e:
        return render_template("error.html", notification=f"Error executing query: {e}")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

    return render_template('view_gear_by_genre.html', gear_by_genre=gear_by_genre)

if __name__ == "__main__":
    from my_flask_app import create_app
    app = create_app()
    app.run(debug=True)
