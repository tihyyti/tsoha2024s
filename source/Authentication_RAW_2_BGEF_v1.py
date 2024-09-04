
CREATE TABLE Bidder
(
    id SERIAL NOT NULL PRIMARY KEY,
    bidderName VARCHAR(30) NOT NULL UNIQUE,
    password VARCHAR(20) DEFAULT NULL,
    admin BOOLEAN DEFAULT FALSE
);
"""
Bidder Table:
Stores information about bidders.
Columns: id, bidderName, password, and admin.
The bidderName is unique.
You can enhance the Bidder table as needed.

BidGenre Table:
Represents bid genres (categories).
Columns: id, bidGenre, bidder, and bidGenreHeader.
The bidder column references the Bidder table.
You can customize the genre definitions.

BidHeader Table:
Contains bid headers (individual bids).
Columns: id, initialBidder, bidGnre, bidHder, numberOfBids, and startedTime.
References to Bidder and BidGenre tables.
bidHder is unique.

BidContent Table:
Stores bid content (details of each bid).
Columns: id, bidderID, bidHead, bidderName, bidContent, and editedTime.
References to BidHeader table.

GearGroup Table:
Represents gear groups.
Columns: id, gearGroup, bidderID, and gearGroupHeader.
References to Bidder table.

Gear Table:
Contains gear information.
Columns: id, gearCode, gearStatus, bidderID, bidHead, gearName, gearDetails, gearStory, amountOffered, origPrice, comments, and editedTime.
References to Bidder and BidHeader tables.

BidExchange Table:
Facilitates equipment exchanges between bidders.
Columns: id, salesBidder, purchaseBidder, equipmentOffer, equipmentRequested, agreedDeal, and dealTimestamp.
References to Bidder table.

Views:
BidGenreList aggregates bid genre data.
BidList summarizes bid header information.
Remember to adjust column definitions and relationships based on your specific requirements.
Let’s break down the steps to add the Bidder authentication feature using Flask, SQLAlchemy, and create an HTML/CSS-based UI.
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///your_database.db'

db = SQLAlchemy(app)
id = db.Column(db.Integer, primary_key=True)
bidderName = db.Column(db.String(30), unique=True, nullable=False)
password = db.Column(db.String(20))
admin = db.Column(db.Boolean, default=False)

#Authentication Service:
#Implement functions to register new bidders, log in, and validate credentials.
#Flask-Login is used for session management.

#Controller Routes for registration, login, and logout:
@app.route('/register', methods=['GET', 'POST'])
def register():
    # Handle registration form submission
    # Create a new Bidder instance and add it to the database
    # Redirect to login page

@app.route('/login', methods=['GET', 'POST'])
def login():
    # Handle login form submission
    # Validate credentials and set session variables
    # Redirect to login page or display error message

@app.route('/logout')
def logout():
    # Clear session variables and redirect to login page

#HTML/CSS UI:
#Create HTML templates for registration, login pages.
#Used Flask-WTF for form handling.

#CSS (override Bootstrap classes)
#registration form:

<!-- templates/register.html -->
<form method="POST">
    <input type="text" name="bidderName" placeholder="Username" required>
    <input type="password" name="password" placeholder="Password" required>
    <input type="submit" value="Register">
</form>

#Database Migrations:
#Use Flask-Migrate to manage database schema changes.
#Run flask db init, flask db migrate, and flask db upgrade to create and apply migrations

import os, logging

# Flask modules
from flask               import render_template, request, url_for, redirect, send_from_directory
from flask_login         import login_user, logout_user, current_user, login_required
from werkzeug.exceptions import HTTPException, NotFound, abort
from jinja2              import TemplateNotFound

# App modules
from app        import app, lm, db, bc
from app.models import Users
from app.forms  import LoginForm, RegisterForm

# provide login manager with load_user callback
@lm.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))

# Logout user
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

# Register a new user
@app.route('/register', methods=['GET', 'POST'])
def register():

    # declare the Registration Form
    form = RegisterForm(request.form)

    msg     = None
    success = False

    if request.method == 'GET':

        return render_template( 'register.html', form=form, msg=msg )

    # check if both http method is POST and form is valid on submit
    if form.validate_on_submit():

        # assign form data to variables
        username = request.form.get('username', '', type=str)
        password = request.form.get('password', '', type=str)
        email    = request.form.get('email'   , '', type=str)

        # filter User out of database through username
        user = Users.query.filter_by(user=username).first()

        # filter User out of database through username
        user_by_email = Users.query.filter_by(email=email).first()

        if user or user_by_email:
            msg = 'Error: User exists!'

        else:

            pw_hash = bc.generate_password_hash(password)

            user = Users(username, email, pw_hash)

            user.save()

            msg     = 'User created, please <a href="' + url_for('login') + '">login</a>'
            success = True

    else:
        msg = 'Input error'

    return render_template( 'register.html', form=form, msg=msg, success=success )

# Authenticate user
@app.route('/login', methods=['GET', 'POST'])
def login():

    # Declare the login form
    form = LoginForm(request.form)

    # Flask message injected into the page, in case of any errors
    msg = None

    # check if both http method is POST and form is valid on submit
    if form.validate_on_submit():

        # assign form data to variables
        username = request.form.get('username', '', type=str)
        password = request.form.get('password', '', type=str)

        # filter User out of database through username
        user = Users.query.filter_by(user=username).first()

        if user:

            if bc.check_password_hash(user.password, password):
                login_user(user)
                return redirect(url_for('index'))
            else:
                msg = "Wrong password. Please try again."
        else:
            msg = "Unknown user"

    return render_template( 'login.html', form=form, msg=msg )

# App main route + generic routing
@app.route('/', defaults={'path': 'index'})
@app.route('/<path>')
def index(path):

    #if not current_user.is_authenticated:
    #    return redirect(url_for('login'))

    try:

        return render_template( 'index.html' )

    except TemplateNotFound:
        return render_template('page-404.html'), 404

    except:
        return render_template('page-500.html'), 500

# Return sitemap
@app.route('/sitemap.xml')
def sitemap():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'sitemap.xml')
#----------------------------------------------------

# Python modules
import os
import logging

# Flask modules
from flask import render_template, request, url_for, redirect, send_from_directory
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.exceptions import HTTPException, NotFound, abort
from jinja2 import TemplateNotFound

# App modules
from app import app, lm, db, bc
from app.models import Bidder  # Import the Bidder model
from app.forms import LoginForm, RegisterForm

# Provide login manager with load_user callback
@lm.user_loader
def load_user(user_id):
    return Bidder.query.get(int(user_id) if user_id else None)

# Logout user
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

# Register a new user
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)  # Declare the Registration Form

    msg = None
    success = False

    if request.method == 'GET':
        return render_template('register.html', form=form, msg=msg)

    if form.validate_on_submit():
        username = request.form.get('username', '', type=str)
        password = request.form.get('password', '', type=str)
        email = request.form.get('email', '', type=str)

        user = Bidder.query.filter_by(bidderName=username).first()
        user_by_email = Bidder.query.filter_by(email=email).first()

        if user or user_by_email:
            msg = 'Error: User exists!'
        else:
            pw_hash = bc.generate_password_hash(password)
            new_bidder = Bidder(bidderName=username, email=email, password=pw_hash)
            db.session.add(new_bidder)
            db.session.commit()
            msg = 'User created, please <a href="' + url_for('login') + '">login</a>'
            success = True
    else:
        msg = 'Input error'

    return render_template('register.html', form=form, msg=msg, success=success)

# Authenticate user
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)  # Declare the login form
    msg = None

    if form.validate_on_submit():
        username = request.form.get('username', '', type=str)
        password = request.form.get('password', '', type=str)

        user = Bidder.query.filter_by(bidderName=username).first()

        if user:
            if bc.check_password_hash(user.password, password):
                login_user(user)
                return redirect(url_for('index'))
            else:
                msg = "Wrong password. Please try again."
        else:
            msg = "Unknown user"

    return render_template('login.html', form=form, msg=msg)

# App main route + generic routing
@app.route('/', defaults={'path': 'index'})
@app.route('/<path>')
def index(path):
    try:
        return render_template('index.html')
    except TemplateNotFound:
        return render_template('page-404.html'), 404
    except:
        return render_template('page-500.html'), 500

# Return sitemap
@app.route('/sitemap.xml')
def sitemap():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'sitemap.xml')
  