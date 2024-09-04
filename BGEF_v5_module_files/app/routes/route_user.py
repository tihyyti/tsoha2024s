
from flask import Blueprint, render_template
from routes.route_user_by_id import get_user_by_id
from __init__ import db
import templates

# Define routes for the user-related functionality (e.g., user profile):
user_profile_bp = Blueprint('user_profile', __name__)

@user_profile_bp.route('/user/user_id')
def user_profile(user_id):
    db = get_db_connection()
    user = db.session.get("user_id",0)
    db.session.close()
    db.close()
    if user:
        return render_template("view_user.html", user=user)
    else:
        return "User not found"
