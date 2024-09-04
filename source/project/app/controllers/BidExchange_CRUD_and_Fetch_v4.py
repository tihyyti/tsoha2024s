
#CRUD and Fetch service functions for the BidExchange class

#Create BidExchange

from flask import request, jsonify

@app.route('/bidexchange', methods=['POST'])
def create_bidexchange():
    data = request.get_json()
    new_bidexchange = BidExchange(
        salesBidder_id=data['salesBidder_id'],
        salesBidHeader_id=data['salesBidHeader_id'],
        purchaseBidder_id=data['purchaseBidder_id'],
        purchaseBidHeader_id=data['purchaseBidHeader_id'],
        agreedDeal=data.get('agreedDeal', False),
        dealTimestamp=data['dealTimestamp']
    )
    db.session.add(new_bidexchange)
    db.session.commit()
    return jsonify({'message': 'New bid exchange created!'}), 201
AI-generated code. Review and use carefully. More info on FAQ.
Fetch All BidExchanges
Python

@app.route('/bidexchanges', methods=['GET'])
def get_all_bidexchanges():
    bidexchanges = BidExchange.query.all()
    output = []
    for bidexchange in bidexchanges:
        bidexchange_data = {
            'id': bidexchange.id,
            'salesBidder_id': bidexchange.salesBidder_id,
            'salesBidHeader_id': bidexchange.salesBidHeader_id,
            'purchaseBidder_id': bidexchange.purchaseBidder_id,
            'purchaseBidHeader_id': bidexchange.purchaseBidHeader_id,
            'agreedDeal': bidexchange.agreedDeal,
            'dealTimestamp': bidexchange.dealTimestamp
        }
        output.append(bidexchange_data)
    return jsonify({'bidexchanges': output})

#Fetch One BidExchange

@app.route('/bidexchange/<bidexchange_id>', methods=['GET'])
def get_one_bidexchange(bidexchange_id):
    bidexchange = BidExchange.query.get(bidexchange_id)
    if not bidexchange:
        return jsonify({'message': 'Bid exchange not found!'}), 404

    bidexchange_data = {
        'id': bidexchange.id,
        'salesBidder_id': bidexchange.salesBidder_id,
        'salesBidHeader_id': bidexchange.salesBidHeader_id,
        'purchaseBidder_id': bidexchange.purchaseBidder_id,
        'purchaseBidHeader_id': bidexchange.purchaseBidHeader_id,
        'agreedDeal': bidexchange.agreedDeal,
        'dealTimestamp': bidexchange.dealTimestamp
    }
    return jsonify({'bidexchange': bidexchange_data})

#Update BidExchange

@app.route('/bidexchange/<bidexchange_id>', methods=['PUT'])
def update_bidexchange(bidexchange_id):
    data = request.get_json()
    bidexchange = BidExchange.query.get(bidexchange_id)
    if not bidexchange:
        return jsonify({'message': 'Bid exchange not found!'}), 404

    bidexchange.salesBidder_id = data['salesBidder_id']
    bidexchange.salesBidHeader_id = data['salesBidHeader_id']
    bidexchange.purchaseBidder_id = data['purchaseBidder_id']
    bidexchange.purchaseBidHeader_id = data['purchaseBidHeader_id']
    bidexchange.agreedDeal = data.get('agreedDeal', bidexchange.agreedDeal)
    bidexchange.dealTimestamp = data['dealTimestamp']

    db.session.commit()
    return jsonify({'message': 'Bid exchange updated!'})

#Delete BidExchange


@app.route('/bidexchange/<bidexchange_id>', methods=['DELETE'])
def delete_bidexchange(bidexchange_id):
    bidexchange = BidExchange.query.get(bidexchange_id)
    if not bidexchange:
        return jsonify({'message': 'Bid exchange not found!'}), 404

    db.session.delete(bidexchange)
    db.session.commit()
    return jsonify({'message': 'Bid exchange deleted!'})
