
#app/models.py

from . import db
from datetime import datetime

class GearBundle(db.Model):
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

class GearRow(db.Model):
    __tablename__ = 'gear_row'
    id = db.Column(db.Integer, primary_key=True)
    bundleID = db.Column(db.Integer, db.ForeignKey('gear_bundle.id'), nullable=False)
    # Row fields...
    gearGroup_id = Column(Integer)  # Adjust the data type as needed
    gearBrand = Column(String)
    gearCode = Column(Integer)
    gearStatus = Column(Integer)  # Adjust the data type as needed
    gearName = Column(String)
    gearStory = Column(String)
    origPurchasePrice = Column(Float)
    amountOffered = Column(Float)  # Adjust the data type as needed
    comments TEXT,
    user_id = Column(Integer)
    #gearImage_link = Column(String)  # Link to gear image (adjust data type as needed)
    #sound_link = Column(String)  # Link to sound sample (adjust data type as needed)
    gearImage_id INT,  -- Links to gear image metadata file
    soundClip_id INT, -- Links to gear sound sample metadata file
    lastEditedTime = Column(DateTime)

class UserManagement(db.Model):
    __tablename__ = 'user_management'
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    is_active = db.Column(db.Boolean, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)

     # Define any additional relationships or constraints here if needed

class SystemLogs(db.Model):
    __tablename__ = 'system_logs'
    log_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    username = db.Column(db.String(80))
    action = db.Column(db.String(255))
    timestamp = db.Column(db.DateTime)
    details = db.Column(db.Text)

     # Define any additional relationships or constraints here if needed

class BidApproval(db.Model): # update this
    __tablename__ = 'bid_approval'
    bid_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    userName = db.Column(db.String(80))
    content = db.Column(db.Text)
    sendTime = db.Column(db.DateTime)
    status = db.Column(db.String(20))

     # Define any additional relationships or constraints here if needed
