
""""""
These classes will provide methods for common operations like creating, reading, updating, and deleting records.

This example includes service classes for Bidder and BidGenre with
methods to create, read, update, and delete records. You can create
similar service classes for BidHeader, BidContent, GearGroup, Gear,
and BidExchange.
""""""

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

# Service classes to interact with the models
class BidderService:
    @staticmethod
    def create_bidder(bidderName, password, admin=False):
        new_bidder = Bidder(bidderName=bidderName, password=password, admin=admin)
        db.session.add(new_bidder)
        db.session.commit()
        return new_bidder

    @staticmethod
    def get_bidder_by_id(bidder_id):
        return Bidder.query.get(bidder_id)

    @staticmethod
    def update_bidder(bidder_id, **kwargs):
        bidder = Bidder.query.get(bidder_id)
        for key, value in kwargs.items():
            setattr(bidder, key, value)
        db.session.commit()
        return bidder

    @staticmethod
    def delete_bidder(bidder_id):
        bidder = Bidder.query.get(bidder_id)
        db.session.delete(bidder)
        db.session.commit()

class BidGenreService:
    @staticmethod
    def create_bid_genre(bidGenre, bidder, bidGenreHeader):
        new_bid_genre = BidGenre(bidGenre=bidGenre, bidder=bidder, bidGenreHeader=bidGenreHeader)
        db.session.add(new_bid_genre)
        db.session.commit()
        return new_bid_genre

    @staticmethod
    def get_bid_genre_by_id(bid_genre_id):
        return BidGenre.query.get(bid_genre_id)

    @staticmethod
    def update_bid_genre(bid_genre_id, **kwargs):
        bid_genre = BidGenre.query.get(bid_genre_id)
        for key, value in kwargs.items():
            setattr(bid_genre, key, value)
        db.session.commit()
        return bid_genre

    @staticmethod
    def delete_bid_genre(bid_genre_id):
        bid_genre = BidGenre.query.get(bid_genre_id)
        db.session.delete(bid_genre)
        db.session.commit()

# Similar service classes can be created for BidHeader, BidContent, GearGroup, Gear, and BidExchange

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
