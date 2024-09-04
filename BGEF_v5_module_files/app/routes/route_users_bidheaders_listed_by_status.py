from flask import Blueprint, render_template, redirect, url_for
from __init__ import db
import templates

users_bidheaders_by_status_bp = Blueprint('user_bids_by_bidstatus', __name__)

# User's BidHeaders listed and grouped based on BidHeader status
@users_bidheaders_by_status_bp.route('/')
def user_bids_by_bidstatus():
    conn = None
    cursor = None
    try:
        # Establish the connection
        conn = db
        cursor = conn.cursor()
        query = "SELECT * FROM vw_user_bids_by_bidstatus"
        cursor.execute(query)
        user_bids_by_bidstatus = cursor.fetchall()
    except Exception as e:
        return render_template("error.html", notification=f"Error executing query: {e}")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

    return render_template('view_user_bidheaders_listed_by_status.html', user_bids_by_bidstatus=user_bids_by_bidstatus)

if __name__ == "__main__":
    from my_flask_app import create_app
    app = create_app()
    app.run(debug=True)
