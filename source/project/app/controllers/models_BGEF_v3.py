
#app/models.py

from . import db
from datetime import datetime

class GearBundle(db.Model):
    __tablename__ = 'gear_bundle'
    id = db.Column(db.Integer, primary_key=True)
    bundleName = db.Column(db.String(80), nullable=False)
    price = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)

class GearRow(db.Model):
    __tablename__ = 'gear_row'
    id = db.Column(db.Integer, primary_key=True)
    bundleID = db.Column(db.Integer, db.ForeignKey('gear_bundle.id'), nullable=False)
    # Other fields...

class UserManagement(db.Model):
    __tablename__ = 'user_management'
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    is_active = db.Column(db.Boolean, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)

class SystemLogs(db.Model):
    __tablename__ = 'system_logs'
    log_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    username = db.Column(db.String(80))
    action = db.Column(db.String(255))
    timestamp = db.Column(db.DateTime)
    details = db.Column(db.Text)

class BidApproval(db.Model):
    __tablename__ = 'bid_approval'
    bid_id = db.Column(db.Integer, primary_key=True)
    bidder_id = db.Column(db.Integer)
    bidderName = db.Column(db.String(80))
    content = db.Column(db.Text)
    sendTime = db.Column(db.DateTime)
    status = db.Column(db.String(20))