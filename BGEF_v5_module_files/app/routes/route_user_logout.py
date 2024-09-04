
# Registration
from flask import Flask, request, redirect, url_for, render_template, flash, Blueprint
from werkzeug.security import generate_password_hash, check_password_hash
import templates

user_logout_bp = Blueprint('logout', __name__)

@user_logout_bp.route('/logout', methods=['GET', 'POST'])
def logout():
    try:
      user.logout()
      return redirect("/login")
    except:
      return redirect("/login")
        else:
            flash('Invalid credentials. Please try again.', 'danger')
    return render_template('login.html')