from flask import Blueprint, render_template
from __init__ import db
import templates

bidheaders_bp = Blueprint('bidheaders_list', __name__)

@bidheaders_bp.route('/bidheaders')
def bidheaders_list():
    conn = None
    cursor = None
    try:
        # Establish the connection
        conn = db
        cursor = conn.cursor()
        query = "SELECT * FROM vw_bid_headers"
        cursor.execute(query)
        bid_headers = cursor.fetchall()
    except Exception as e:
        return render_template("error.html", notification=f"Error executing query: {e}")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

    return render_template('view_bid_headers_list.html', bid_headers=bid_headers)

if __name__ == "__main__":
    from my_flask_app import create_app
    app = create_app()
    app.run(debug=True)
