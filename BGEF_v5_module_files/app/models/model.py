from flask import Flask
#from flask_sqlalchemy import SQLAlchemy

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@localhost/dbBGEF_v5'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#db = SQLAlchemy(app)
from __init__ import db

class ImageMetadata(db.Model):
    __tablename__ = 'ImageMetadata'
    id = db.Column(db.Integer, primary_key=True)
    imageName = db.Column(db.String(100), nullable=False)
    AxSize = db.Column(db.String(10), nullable=False)
    resolution = db.Column(db.String(20), nullable=False)
    image_url = db.Column(db.String(255), nullable=False)

class SoundClipMetadata(db.Model):
    __tablename__ = 'SoundClipMetadata'
    id = db.Column(db.Integer, primary_key=True)
    clipName = db.Column(db.String(100), nullable=False)
    format = db.Column(db.String(10), nullable=False)
    quality = db.Column(db.String(30), nullable=False)
    clipLengthInSeconds = db.Column(db.Float, nullable=False)
    isStereo = db.Column(db.Boolean, nullable=False)
    sample_url = db.Column(db.String(255), nullable=False)

class Client(db.Model):
    __tablename__ = 'Client'
    id = db.Column(db.Integer, primary_key=True)
    userName = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(25))
    email = db.Column(db.String(50))
    secondaryEmail = db.Column(db.String(50))
    userIcon_id = db.Column(db.Integer, db.ForeignKey('ImageMetadata.id'))
    roleName = db.Column(db.String(50), nullable=False, unique=True)
    registeredUser = db.Column(db.Boolean, default=False)
    sellerRole = db.Column(db.Boolean, default=False)
    buyerRole = db.Column(db.Boolean, default=False)
    adminRole = db.Column(db.Boolean, default=False)
    blocked = db.Column(db.Boolean, default=False)

class BidGenre(db.Model):
    __tablename__ = 'BidGenre'
    id = db.Column(db.Integer, primary_key=True)
    bidGenreHeader = db.Column(db.String(100), nullable=False, unique=True)

class BidExchange(db.Model):
    __tablename__ = 'BidExchange'
    id = db.Column(db.Integer, primary_key=True)
    salesBidder_id = db.Column(db.Integer, db.ForeignKey('Client.id'), nullable=False)
    salesBidHeader_id = db.Column(db.Integer, db.ForeignKey('BidHeader.id'), nullable=False)
    purchaseBidder_id = db.Column(db.Integer, db.ForeignKey('Client.id'), nullable=False)
    purchaseBidHeader_id = db.Column(db.Integer, db.ForeignKey('BidHeader.id'), nullable=False)
    agreedDeal = db.Column(db.Boolean, default=False)
    otherConditions = db.Column(db.Text)
    addOnValue = db.Column(db.Float, default=0.00)
    dealTimestamp = db.Column(db.TIMESTAMP, nullable=False)

class Gear(db.Model):
    __tablename__ = 'Gear'
    id = db.Column(db.Integer, primary_key=True)
    gearBrand = db.Column(db.String(30), nullable=False)
    gearCode = db.Column(db.Integer)
    gearStatus = db.Column(db.Integer)
    bidHeader_id = db.Column(db.Integer, db.ForeignKey('BidHeader.id'))
    gearName = db.Column(db.String(100), nullable=False)
    gearDetails = db.Column(db.Text)
    gearStory = db.Column(db.Text)
    amountOffered = db.Column(db.Integer, nullable=False)
    approxValue = db.Column(db.Float, default=0.00)
    user_id = db.Column(db.Integer, db.ForeignKey('Client.id'))
    comments = db.Column(db.Text)
    createdTime = db.Column(db.TIMESTAMP, nullable=False)
    editedTime = db.Column(db.TIMESTAMP, nullable=False)
    gearImage_id = db.Column(db.Integer, db.ForeignKey('ImageMetadata.id'))
    soundClip_id = db.Column(db.Integer, db.ForeignKey('SoundClipMetadata.id'))

class BidHeader(db.Model):
    __tablename__ = 'BidHeader'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('Client.id'))
    bidGenre_id = db.Column(db.Integer, db.ForeignKey('BidGenre.id'))
    bidTypeCode = db.Column(db.Integer)
    bidStatus = db.Column(db.Integer)
    bidexchange_id = db.Column(db.Integer, db.ForeignKey('BidExchange.id'))
    bidHeaderText = db.Column(db.String(100), nullable=False, unique=True)
    bidContent = db.Column(db.String(300), nullable=False)
    gear1_id = db.Column(db.Integer, db.ForeignKey('Gear.id'))
    gear2_id = db.Column(db.Integer, db.ForeignKey('Gear.id'))
    gear3_id = db.Column(db.Integer, db.ForeignKey('Gear.id'))
    gear4_id = db.Column(db.Integer, db.ForeignKey('Gear.id'))
    gear5_id = db.Column(db.Integer, db.ForeignKey('Gear.id'))
    gear6_id = db.Column(db.Integer, db.ForeignKey('Gear.id'))
    gear7_id = db.Column(db.Integer, db.ForeignKey('Gear.id'))
    gear8_id = db.Column(db.Integer, db.ForeignKey('Gear.id'))
    gear9_id = db.Column(db.Integer, db.ForeignKey('Gear.id'))
    gear10_id = db.Column(db.Integer, db.ForeignKey('Gear.id'))
    bundleImage_id = db.Column(db.Integer, db.ForeignKey('ImageMetadata.id'))
    bundleSound_id = db.Column(db.Integer, db.ForeignKey('SoundClipMetadata.id'))
    hdrEditedTime = db.Column(db.TIMESTAMP, nullable=False)
    conEditedTime = db.Column(db.TIMESTAMP, nullable=False)
    bidStartingTime = db.Column(db.TIMESTAMP, nullable=False)
    bidEndingTime = db.Column(db.TIMESTAMP, nullable=False)
    bidCreatedTime = db.Column(db.TIMESTAMP, nullable=False)

if __name__ == '__main__':
    # with app.app_context():

