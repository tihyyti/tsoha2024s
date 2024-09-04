
from flask import Blueprint, request, jsonify
from .services import BidHeaderService

#BidHeaderService

class BidHeaderService:
    @staticmethod
    def create_bid_header(initialBidder, bidGnre, bidHder, numberOfB
startedTime):
        new_bid_header = BidHeader(initialBidder=initialBidder,
bidGnre=bidGnre, bidHder=bidHder, numberOfBids=numberOfBids,
startedTime=startedTime)
        db.session.add(new_bid_header)
        db.session.commit()
        return new_bid_header

    @staticmethod
    def get_bid_header_by_id(bid_header_id):
        return BidHeader.query.get(bid_header_id)

    @staticmethod
    def update_bid_header(bid_header_id, **kwargs):
        bid_header = BidHeader.query.get(bid_header_id)
        for key, value in kwargs.items():
            setattr(bid_header, key, value)
        db.session.commit()
        return bid_header

    @staticmethod
    def delete_bid_header(bid_header_id):
        bid_header = BidHeader.query.get(bid_header_id)
        db.session.delete(bid_header)
        db.session.commit()

#BidContentService

class BidContentService:
    @staticmethod
    def create_bid_content(bidderID, bidHead, bidderName, bidContent
editedTime):
        new_bid_content = BidContent(bidderID=bidderID, bidHead=bidH
bidderName=bidderName, bidContent=bidContent,
editedTime=editedTime)
        db.session.add(new_bid_content)
        db.session.commit()
        return new_bid_content

    @staticmethod
    def get_bid_content_by_id(bid_content_id):
        return BidContent.query.get(bid_content_id)

    @staticmethod
    def update_bid_content(bid_content_id, **kwargs):
        bid_content = BidContent.query.get(bid_content_id)
        for key, value in kwargs.items():
            setattr(bid_content, key, value)
        db.session.commit()
        return bid_content

    @staticmethod
    def delete_bid_content(bid_content_id):
        bid_content = BidContent.query.get(bid_content_id)
        db.session.delete(bid_content)
        db.session.commit()

#GearGroupService

class GearGroupService:
    @staticmethod
    def create_gear_group(gearGroup, bidderID, gearGroupHeader):
        new_gear_group = GearGroup(gearGroup=gearGroup,
bidderID=bidderID, gearGroupHeader=gearGroupHeader)
        db.session.add(new_gear_group)
        db.session.commit()
        return new_gear_group

    @staticmethod
    def get_gear_group_by_id(gear_group_id):
        return GearGroup.query.get(gear_group_id)

    @staticmethod
    def update_gear_group(gear_group_id, **kwargs):
        gear_group = GearGroup.query.get(gear_group_id)
        for key, value in kwargs.items():
            setattr(gear_group, key, value)
        db.session.commit()
        return gear_group

    @staticmethod
    def delete_gear_group(gear_group_id):
        gear_group = GearGroup.query.get(gear_group_id)
        db.session.delete(gear_group)
        db.session.commit()

#GearService

class GearService:
    @staticmethod
    def create_gear(gearCode, gearStatus, bidderID, bidHead, gearNam
gearDetails, gearStory, amountOffered, origPrice, comments,
editedTime):
        new_gear = Gear(gearCode=gearCode, gearStatus=gearStatus,
bidderID=bidderID, bidHead=bidHead, gearName=gearName,
gearDetails=gearDetails, gearStory=gearStory,
amountOffered=amountOffered, origPrice=origPrice,
comments=comments, editedTime=editedTime)
        db.session.add(new_gear)
        db.session.commit()
        return new_gear

    @staticmethod
    def get_gear_by_id(gear_id):
        return Gear.query.get(gear_id)

    @staticmethod
    def update_gear(gear_id, **kwargs):
        gear = Gear.query.get(gear_id)
        for key, value in kwargs.items():
            setattr(gear, key, value)
        db.session.commit()
        return gear

    @staticmethod
    def delete_gear(gear_id):
        gear = Gear.query.get(gear_id)
        db.session.delete(gear)
        db.session.commit()

#BidExchangeService

class BidExchangeService:
    @staticmethod
    def create_bid_exchange(salesBidder, purchaseBidder,
equipmentOffer, equipmentRequested, agreedDeal, dealTimestamp):
        new_bid_exchange = BidExchange(salesBidder=salesBidder,
purchaseBidder=purchaseBidder, equipmentOffer=equipmentOffer
equipmentRequested=equipmentRequested, agreedDeal=agreedDeal
dealTimestamp=dealTimestamp)
        db.session.add(new_bid_exchange)
        db.session.commit()
        return new_bid_exchange

    @staticmethod
    def get_bid_exchange_by_id(bid_exchange_id):
        return BidExchange.query.get(bid_exchange_id)

    @staticmethod
    def update_bid_exchange(bid_exchange_id, **kwargs):
        bid_exchange = BidExchange.query.get(bid_exchange_id)
        for key, value in kwargs.items():
            setattr(bid_exchange, key, value)
        db.session.commit()
        return bid_exchange

    @staticmethod
    def delete_bid_exchange(bid_exchange_id):
        bid_exchange = BidExchange.query.get(bid_exchange_id)
        db.session.delete(bid_exchange)
        db.session.commit()
#-------------------------------------------------------------

#the controllers for the services.

#BidHeaderController

bid_header_bp = Blueprint('bid_header', __name__)

@bid_header_bp.route('/bid_header', methods=['POST'])
def create_bid_header():
    data = request.get_json()
    new_bid_header = BidHeaderService.create_bid_header(
        data['initialBidder'], data['bidGnre'], data['bidHder'],
        data['numberOfBids'], data['startedTime']
    )
    return jsonify(new_bid_header), 201

@bid_header_bp.route('/bid_header/<int:bid_header_id>', methods=['GET'])
def get_bid_header(bid_header_id):
    bid_header = BidHeaderService.get_bid_header_by_id(bid_header_id)
    return jsonify(bid_header)

@bid_header_bp.route('/bid_header/<int:bid_header_id>', methods=['PUT'])
def update_bid_header(bid_header_id):
    data = request.get_json()
    updated_bid_header = BidHeaderService.update_bid_header(bid_header_id, **data)
    return jsonify(updated_bid_header)

@bid_header_bp.route('/bid_header/<int:bid_header_id>', methods=['DELETE'])
def delete_bid_header(bid_header_id):
    BidHeaderService.delete_bid_header(bid_header_id)
    return '', 204

#BidContentController

from flask import Blueprint, request, jsonify
from .services import BidContentService

bid_content_bp = Blueprint('bid_content', __name__)

@bid_content_bp.route('/bid_content', methods=['POST'])
def create_bid_content():
    data = request.get_json()
    new_bid_content = BidContentService.create_bid_content(
        data['bidderID'], data['bidHead'], data['bidderName'],
        data['bidContent'], data['editedTime']
    )
    return jsonify(new_bid_content), 201

@bid_content_bp.route('/bid_content/<int:bid_content_id>', methods=['GET'])
def get_bid_content(bid_content_id):
    bid_content = BidContentService.get_bid_content_by_id(bid_content_id)
    return jsonify(bid_content)

@bid_content_bp.route('/bid_content/<int:bid_content_id>', methods=['PUT'])
def update_bid_content(bid_content_id):
    data = request.get_json()
    updated_bid_content = BidContentService.update_bid_content(bid_content_id, **data)
    return jsonify(updated_bid_content)

@bid_content_bp.route('/bid_content/<int:bid_content_id>', methods=['DELETE'])
def delete_bid_content(bid_content_id):
    BidContentService.delete_bid_content(bid_content_id)
    return '', 204
AI-generated code. Review and use carefully. More info on FAQ.
GearGroupController
Python

from flask import Blueprint, request, jsonify
from .services import GearGroupService

gear_group_bp = Blueprint('gear_group', __name__)

@gear_group_bp.route('/gear_group', methods=['POST'])
def create_gear_group():
    data = request.get_json()
    new_gear_group = GearGroupService.create_gear_group(
        data['gearGroup'], data['bidderID'], data['gearGroupHeader']
    )
    return jsonify(new_gear_group), 201

@gear_group_bp.route('/gear_group/<int:gear_group_id>', methods=['GET'])
def get_gear_group(gear_group_id):
    gear_group = GearGroupService.get_gear_group_by_id(gear_group_id)
    return jsonify(gear_group)

@gear_group_bp.route('/gear_group/<int:gear_group_id>', methods=['PUT'])
def update_gear_group(gear_group_id):
    data = request.get_json()
    updated_gear_group = GearGroupService.update_gear_group(gear_group_id, **data)
    return jsonify(updated_gear_group)

@gear_group_bp.route('/gear_group/<int:gear_group_id>', methods=['DELETE'])
def delete_gear_group(gear_group_id):
    GearGroupService.delete_gear_group(gear_group_id)
    return '', 204

#GearController

from flask import Blueprint, request, jsonify
from .services import GearService

gear_bp = Blueprint('gear', __name__)

@gear_bp.route('/gear', methods=['POST'])
def create_gear():
    data = request.get_json()
    new_gear = GearService.create_gear(
        data['gearCode'], data['gearStatus'], data['bidderID'],
        data['bidHead'], data['gearName'], data['gearDetails'],
        data['gearStory'], data['amountOffered'], data['origPrice'],
        data['comments'], data['editedTime']
    )
    return jsonify(new_gear), 201

@gear_bp.route('/gear/<int:gear_id>', methods=['GET'])
def get_gear(gear_id):
    gear = GearService.get_gear_by_id(gear_id)
    return jsonify(gear)

@gear_bp.route('/gear/<int:gear_id>', methods=['PUT'])
def update_gear(gear_id):
    data = request.get_json()
    updated_gear = GearService.update_gear(gear_id, **data)
    return jsonify(updated_gear)

@gear_bp.route('/gear/<int:gear_id>', methods=['DELETE'])
def delete_gear(gear_id):
    GearService.delete_gear(gear_id)
    return '', 204
#BidExchangeController


from flask import Blueprint, request, jsonify
from .services import BidExchangeService

bid_exchange_bp = Blueprint('bid_exchange', __name__)

@bid_exchange_bp.route('/bid_exchange', methods=['POST'])
def create_bid_exchange():
    data = request.get_json()
    new_bid_exchange = BidExchangeService.create_bid_exchange(
        data['salesBidder'], data['purchaseBidder'], data['equipmentOffer'],
        data['equipmentRequested'], data['agreedDeal'], data['dealTimestamp']
    )
    return jsonify(new_bid_exchange), 201

@bid_exchange_bp.route('/bid_exchange/<int:bid_exchange_id>', methods=['GET'])
def get_bid_exchange(bid_exchange_id):
    bid_exchange = BidExchangeService.get_bid_exchange_by_id(bid_exchange_id)
    return jsonify(bid_exchange)

@bid_exchange_bp.route('/bid_exchange/<int:bid_exchange_id>', methods=['PUT'])
def update_bid_exchange(bid_exchange_id):
    data = request.get_json()
    updated_bid_exchange = BidExchangeService.update_bid_exchange(bid_exchange_id, **data)
    return jsonify(updated_bid_exchange)

@bid_exchange_bp.route('/bid_exchange/<int:bid_exchange_id>', methods=['DELETE'])
def delete_bid_exchange(bid_exchange_id):
    BidExchangeService.delete_bid_exchange(bid_exchange_id)
    return '', 204


#HTML and CSS

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bid Management</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="container">
        <h1>Bid Management System</h1>
        <div id="bid-header-form">
            <h2>Create Bid Header</h2>
            <form>
                <label for="initialBidder">Initial Bidder:</label>
                <input type="text" id="initialBidder" name="initialBidder">
                <label for="bidGnre">Bid Genre:</label>
                <input type="text" id="bidGnre" name="bidGnre">
                <label for="bidHder">Bid Header:</label>
                <input type="text" id="bidHder" name="bidHder">
                <label for="numberOfBids">Number of Bids:</label>
                <input type="number" id="numberOfBids" name="numberOfBids">
                <label for="startedTime">Started Time:</label>
                <input type="datetime-local" id="startedTime" name="startedTime">
                <button type="submit">Create</button>
            </form>
        </div>
        <!-- Add similar forms for Bid Content, Gear Group, and Gear -->
    </div>
</body>
</html>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bid Exchange Management</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="container">
        <h1>Bid Exchange Management System</h1>
        <div id="bid-exchange-form">
            <h2>Create Bid Exchange</h2>
            <form>
                <label for="salesBidder">Sales Bidder:</label>
                <input type="text" id="salesBidder" name="salesBidder">
                <label for="purchaseBidder">Purchase Bidder:</label>
                <input type="text" id="purchaseBidder" name="purchaseBidder">
                <label for="equipmentOffer">Equipment Offer:</label>
                <input type="text" id="equipmentOffer" name="equipmentOffer">
                <label for="equipmentRequested">Equipment Requested:</label>
                <input type="text" id="equipmentRequested" name="equipmentRequested">
                <label for="agreedDeal">Agreed Deal:</label>
                <input type="text" id="agreedDeal" name="agreedDeal">
                <label for="dealTimestamp">Deal Timestamp:</label>
                <input type="datetime-local" id="dealTimestamp" name="dealTimestamp">
                <button type="submit">Create</button>
            </form>
        </div>
    </div>
</body>
</html>

#CSS

body {
    font-family: Arial, sans-serif;
    background-color: #f4f4f4;
    margin: 0;
    padding: 0;
}

.container {
    width: 80%;
    margin: auto;
    overflow: hidden;
}

h1, h2 {
    color: #333;
}

form {
    background: #fff;
    padding: 20px;
    margin: 20px 0;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

label {
    display: block;
    margin: 10px 0 5px;
}

input[type="text"], input[type="number"], input[type="datetime-local"] {
    width: 100%;
    padding: 10px;
    margin: 5px 0 20px;
    border: 1px solid #ccc;
    border-radius: 4px;
}

button {
    display: inline-block;
    padding: 10px 20px;
    font-size: 16px;
    cursor: pointer;
    background: #333;
    color: #fff;
    border: none;
    border-radius: 4px;
}

button:hover {
    background: #555;
}#CSS

body {
    font-family: Arial, sans-serif;
    background-color: #f4f4f4;
    margin: 0;
    padding: 0;
}

.container {
    width: 80%;
    margin: auto;
    overflow: hidden;
}

h1, h2 {
    color: #333;
}

form {
    background: #fff;
    padding: 20px;
    margin: 20px 0;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

label {
    display: block;
    margin: 10px 0 5px;
}

input[type="text"], input[type="datetime-local"] {
    width: 100%;
    padding: 10px;
    margin: 5px 0 20px;
    border: 1px solid #ccc;
    border-radius: 4px;
}

button {
    display: inline-block;
    padding: 10px 20px;
    font-size: 16px;
    cursor: pointer;
    background: #333;
    color: #fff;
    border: none;
    border-radius: 4px;
}

button:hover {
    background: #555;
}