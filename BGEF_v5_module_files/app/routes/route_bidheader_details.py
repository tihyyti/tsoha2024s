# from flask import Blueprint, render_template, redirect, url_for
# from __init__ import db
# import templates
#
from flask import Flask, Blueprint, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

bidheader_details_bp = Blueprint('bidheader_details', __name__)

@bidheader_details_bp.route('/bidheader/<int:bidheader_id>')
def bidheader_details(bidheader_id):
    conn = db
    cursor = None
    try:

        # cursor = conn.cursor()
        # query = "SELECT * FROM bidheader WHERE id = %d"
        # cursor.execute(query, (int(bidheader_id),))
        # bidheader = cursor.fetchone()

        query = "SELECT * FROM bidheader WHERE id = :id"
        result = db.session.execute(query, {'id': bidheader_id})
        bidheader = result.fetchall()

    except Exception as e:
        return render_template("error.html", notification=f"Error executing query: {e}")
    finally:
        if cursor:
            cursor.close()
        # if conn:
            # conn.close()

    if bidheader:
        return render_template('view_bidheader_details.html', bidheader=bidheader)
    else:
        return render_template("error.html", notification="BidHeader not found")

if __name__ == "__main__":
    app.run(debug=True)