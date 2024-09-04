"""pip install Flask Flask-SQLAlchemy

Next, create your Flask application and define the models based on your schema:

This code sets up your Flask application, configures SQLAlchemy, and defines the models based
on your provided schema. You can run this script to create the database and tables.
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@localhost/yourdatabase'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Bidder(db.Model):
    __tablename__ = 'bidder'
    id = db.Column(db.Integer, primary_key=True)
    bidderName = db.Column(db.String(30), unique=True, nullable=False)
    password = db.Column(db.Text, nullable=True)
    admin = db.Column(db.Boolean, default=False)

class BidGenre(db.Model):
    __tablename__ = 'bidgenre'
    id = db.Column(db.Integer, primary_key=True)
    bidGenre = db.Column(db.Integer)
    bidder = db.Column(db.Integer, db.ForeignKey('bidder.id'))
    bidGenreHeader = db.Column(db.String(100), unique=True, nullable=False)

class BidHeader(db.Model):
    __tablename__ = 'bidheader'
    id = db.Column(db.Integer, primary_key=True)
    initialBidder = db.Column(db.Integer, db.ForeignKey('bidder.id'))
    bidGnre = db.Column(db.Integer, db.ForeignKey('bidgenre.id'))
    bidHder = db.Column(db.String(100), unique=True, nullable=False)
    numberOfBids = db.Column(db.Integer, nullable=False)
    startedTime = db.Column(db.DateTime, default=db.func.current_timestamp())

class BidContent(db.Model):
    __tablename__ = 'bidcontent'
    id = db.Column(db.Integer, primary_key=True)
    bidderID = db.Column(db.Integer, db.ForeignKey('bidder.id'))
    bidHead = db.Column(db.Integer, db.ForeignKey('bidheader.id'))
    bidderName = db.Column(db.String(30), nullable=False)
    bidContent = db.Column(db.Text, nullable=False)
    editedTime = db.Column(db.DateTime, default=db.func.current_timestamp())

class GearGroup(db.Model):
    __tablename__ = 'geargroup'
    id = db.Column(db.Integer, primary_key=True)
    gearGroup = db.Column(db.Integer)
    bidderID = db.Column(db.Integer, db.ForeignKey('bidder.id'))
    gearGroupHeader = db.Column(db.String(100), unique=True, nullable=False)

class Gear(db.Model):
    __tablename__ = 'gear'
    id = db.Column(db.Integer, primary_key=True)
    gearCode = db.Column(db.Integer)
    gearStatus = db.Column(db.Integer)
    bidderID = db.Column(db.Integer, db.ForeignKey('bidder.id'))
    bidHead = db.Column(db.Integer, db.ForeignKey('bidheader.id'))
    gearName = db.Column(db.String(100), nullable=False)
    gearDetails = db.Column(db.Text, nullable=False)
    gearStory = db.Column(db.Text, nullable=False)
    amountOffered = db.Column(db.Integer, nullable=False)
    origPrice = db.Column(db.Integer, nullable=False)
    comments = db.Column(db.Text, nullable=False)
    editedTime = db.Column(db.DateTime, default=db.func.current_timestamp())

class BidExchange(db.Model):
    __tablename__ = 'bidexchange'
    id = db.Column(db.Integer, primary_key=True)
    salesBidder = db.Column(db.Integer, db.ForeignKey('bidder.id'), nullable=False)
    purchaseBidder = db.Column(db.Integer, db.ForeignKey('bidder.id'), nullable=False)
    equipmentOffer = db.Column(db.String(100), nullable=False)
    equipmentRequested = db.Column(db.String(100), nullable=False)
    agreedDeal = db.Column(db.Boolean, default=False)
    dealTimestamp = db.Column(db.DateTime, default=db.func.current_timestamp())

# Create the database and tables
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
