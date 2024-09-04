# middleware.py
from functools import wraps
from flask import session, redirect, url_for
import templates

admin_dashboard_bp = Blueprint('decorated_function', __name__)

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get('user_role') != 'admin':
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function