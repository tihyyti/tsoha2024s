
#CRUD and Fetch service functions for the BidGenre class

#Create BidGenre

from flask import request, jsonify

@app.route('/bidgenre', methods=['POST'])
def create_bidgenre():
    data = request.get_json()
    new_bidgenre = BidGenre(
        bidGenreHeader=data['bidGenreHeader'],
        user_id=data.get('user_id'),
        lastBidHeader_id=data.get('lastBidHeader_id'),
        numberOfBids=data['numberOfBids']
    )
    db.session.add(new_bidgenre)
    db.session.commit()
    return jsonify({'message': 'New bid genre created!'}), 201

#Fetch All BidGenres

@app.route('/bidgenres', methods=['GET'])
def get_all_bidgenres():
    bidgenres = BidGenre.query.all()
    output = []
    for bidgenre in bidgenres:
        bidgenre_data = {
            'id': bidgenre.id,
            'bidGenreHeader': bidgenre.bidGenreHeader,
            'user_id': bidgenre.user_id,
            'lastBidHeader_id': bidgenre.lastBidHeader_id,
            'numberOfBids': bidgenre.numberOfBids
        }
        output.append(bidgenre_data)
    return jsonify({'bidgenres': output})

#Fetch One BidGenre

@app.route('/bidgenre/<bidgenre_id>', methods=['GET'])
def get_one_bidgenre(bidgenre_id):
    bidgenre = BidGenre.query.get(bidgenre_id)
    if not bidgenre:
        return jsonify({'message': 'Bid genre not found!'}), 404

    bidgenre_data = {
        'id': bidgenre.id,
        'bidGenreHeader': bidgenre.bidGenreHeader,
        'user_id': bidgenre.user_id,
        'lastBidHeader_id': bidgenre.lastBidHeader_id,
        'numberOfBids': bidgenre.numberOfBids
    }
    return jsonify({'bidgenre': bidgenre_data})

#Update BidGenre

@app.route('/bidgenre/<bidgenre_id>', methods=['PUT'])
def update_bidgenre(bidgenre_id):
    data = request.get_json()
    bidgenre = BidGenre.query.get(bidgenre_id)
    if not bidgenre:
        return jsonify({'message': 'Bid genre not found!'}), 404

    bidgenre.bidGenreHeader = data['bidGenreHeader']
    bidgenre.user_id = data.get('user_id')
    bidgenre.lastBidHeader_id = data.get('lastBidHeader_id')
    bidgenre.numberOfBids = data['numberOfBids']

    db.session.commit()
    return jsonify({'message': 'Bid genre updated!'})

#Delete BidGenre

@app.route('/bidgenre/<bidgenre_id>', methods=['DELETE'])
def delete_bidgenre(bidgenre_id):
    bidgenre = BidGenre.query.get(bidgenre_id)
    if not bidgenre:
        return jsonify({'message': 'Bid genre not found!'}), 404

    db.session.delete(bidgenre)
    db.session.commit()
    return jsonify({'message': 'Bid genre deleted!'})
