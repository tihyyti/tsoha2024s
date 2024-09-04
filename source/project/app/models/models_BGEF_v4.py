
#app/models.py

from . import db
from datetime import datetime

class UserManagement(db.Model):
    __tablename__ = 'user_management'
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    is_active = db.Column(db.Boolean, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)

     # Define any additional relationships or constraints here if needed

class BidContent(db.Model):
    __tablename__ = 'gear_bundle'
    id = db.Column(db.Integer, primary_key=True)
    dealStatus = Column(String)
    bundleName = db.Column(db.String(80), nullable=False)
    bundleGenre = Column(String)
    bundleContent = Column(String)
    price = db.Column(db.Float, nullable=False)
    user_id = Column(Integer)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow,
    onupdate=datetime.utcnow)

    # Define any additional relationships or constraints here if needed

class Gear(db.Model):
    __tablename__ = 'Gear'
    id = db.Column(db.Integer, primary_key=True)
    gearBrand = db.Column(db.String(30), nullable=False)
    gearCode = db.Column(db.Integer, default=None)
    gearStatus = db.Column(db.Integer, default=None)
    bidHeader_id = db.Column(db.Integer, db.ForeignKey('BidHeader.id'), default=None)
    gearName = db.Column(db.String(100), nullable=False)
    gearDetails = db.Column(db.Text, default=None)
    gearStory = db.Column(db.Text, default=None)
    amountOffered = db.Column(db.Integer, nullable=False)
    approxValue = db.Column(db.Float, default=0.00)
    user_id = db.Column(db.Integer, db.ForeignKey('User.id'), default=None)
    comments = db.Column(db.Text, default=None)
    editedTime = db.Column(db.DateTime, nullable=False)
    gearImage_id = db.Column(db.Integer, db.ForeignKey('ImageMetadata.id'), default=None)
    soundClip_id = db.Column(db.Integer, db.ForeignKey('SoundClipMetadata.id'), default=None)

    user = db.relationship('User', backref=db.backref('gears', lazy=True))
    bidHeader = db.relationship('BidHeader', backref=db.backref('gears', lazy=True))
    gearImage = db.relationship('ImageMetadata', foreign_keys=[gearImage_id])
    soundClip = db.relationship('SoundClipMetadata', foreign_keys=[soundClip_id]

class BidExchange(db.Model):
    __tablename__ = 'BidExchange'
    id = db.Column(db.Integer, primary_key=True)
    salesBidder_id = db.Column(db.Integer, db.ForeignKey('User.id'), nullable=False)
    salesBidHeader_id = db.Column(db.Integer, db.ForeignKey('BidHeader.id'), nullable=False)
    purchaseBidder_id = db.Column(db.Integer, db.ForeignKey('User.id'), nullable=False)
    purchaseBidHeader_id = db.Column(db.Integer, db.ForeignKey('BidHeader.id'), nullable=False)
    agreedDeal = db.Column(db.Boolean, default=False)
    dealTimestamp = db.Column(db.DateTime, nullable=False)

    salesBidder = db.relationship('User', foreign_keys=[salesBidder_id], backref=db.backref('salesBidExchanges', lazy=True))
    salesBidHeader = db.relationship('BidHeader', foreign_keys=[salesBidHeader_id], backref=db.backref('salesBidExchanges', lazy=True))
    purchaseBidder = db.relationship('User', foreign_keys=[purchaseBidder_id], backref=db.backref('purchaseBidExchanges', lazy=True))
    purchaseBidHeader = db.relationship('BidHeader', foreign_keys=[purchaseBidHeader_id], backref=db.backref('purchaseBidExchanges', lazy=True))

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

class SystemLogs(db.Model):
    __tablename__ = 'system_logs'
    log_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    username = db.Column(db.String(80))
    action = db.Column(db.String(255))
    timestamp = db.Column(db.DateTime)
    details = db.Column(db.Text)

     # Define any additional relationships or constraints here if needed
