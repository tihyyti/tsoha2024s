
#CRUD and Fetch service functions for the BidHeader class

#Create BidHeader

from flask import request, jsonify

@app.route('/bidheader', methods=['POST'])
def create_bidheader():
    data = request.get_json()
    new_bidheader = BidHeader(
        user_id=data.get('user_id'),
        bidGenre_id=data.get('bidGenre_id'),
        bidTypeCode=data.get('bidTypeCode'),
        bidStatus=data.get('bidStatus'),
        bidContent_id=data.get('bidContent_id'),
        bidHeaderText=data['bidHeaderText'],
        bidExchange1_id=data.get('bidExchange1_id'),
        bidExchange2_id=data.get('bidExchange2_id'),
        bidExchange3_id=data.get('bidExchange3_id'),
        bidExchange4_id=data.get('bidExchange4_id'),
        bidExchange5_id=data.get('bidExchange5_id'),
        bidStartedTime=data['bidStartedTime'],
        bidEndingTime=data['bidEndingTime'],
        hdrEditedTime=data['hdrEditedTime']
    )
    db.session.add(new_bidheader)
    db.session.commit()
    return jsonify({'message': 'New bid header created!'}), 201

#Fetch All BidHeaders

@app.route('/bidheaders', methods=['GET'])
def get_all_bidheaders():
    bidheaders = BidHeader.query.all()
    output = []
    for bidheader in bidheaders:
        bidheader_data = {
            'id': bidheader.id,
            'user_id': bidheader.user_id,
            'bidGenre_id': bidheader.bidGenre_id,
            'bidTypeCode': bidheader.bidTypeCode,
            'bidStatus': bidheader.bidStatus,
            'bidContent_id': bidheader.bidContent_id,
            'bidHeaderText': bidheader.bidHeaderText,
            'bidExchange1_id': bidheader.bidExchange1_id,
            'bidExchange2_id': bidheader.bidExchange2_id,
            'bidExchange3_id': bidheader.bidExchange3_id,
            'bidExchange4_id': bidheader.bidExchange4_id,
            'bidExchange5_id': bidheader.bidExchange5_id,
            'bidStartedTime': bidheader.bidStartedTime,
            'bidEndingTime': bidheader.bidEndingTime,
            'hdrEditedTime': bidheader.hdrEditedTime
        }
        output.append(bidheader_data)
    return jsonify({'bidheaders': output})

#Fetch One BidHeader

@app.route('/bidheader/<bidheader_id>', methods=['GET'])
def get_one_bidheader(bidheader_id):
    bidheader = BidHeader.query.get(bidheader_id)
    if not bidheader:
        return jsonify({'message': 'Bid header not found!'}), 404

    bidheader_data = {
        'id': bidheader.id,
        'user_id': bidheader.user_id,
        'bidGenre_id': bidheader.bidGenre_id,
        'bidTypeCode': bidheader.bidTypeCode,
        'bidStatus': bidheader.bidStatus,
        'bidContent_id': bidheader.bidContent_id,
        'bidHeaderText': bidheader.bidHeaderText,
        'bidExchange1_id': bidheader.bidExchange1_id,
        'bidExchange2_id': bidheader.bidExchange2_id,
        'bidExchange3_id': bidheader.bidExchange3_id,
        'bidExchange4_id': bidheader.bidExchange4_id,
        'bidExchange5_id': bidheader.bidExchange5_id,
        'bidStartedTime': bidheader.bidStartedTime,
        'bidEndingTime': bidheader.bidEndingTime,
        'hdrEditedTime': bidheader.hdrEditedTime
    }
    return jsonify({'bidheader': bidheader_data})

#Update BidHeader

@app.route('/bidheader/<bidheader_id>', methods=['PUT'])
def update_bidheader(bidheader_id):
    data = request.get_json()
    bidheader = BidHeader.query.get(bidheader_id)
    if not bidheader:
        return jsonify({'message': 'Bid header not found!'}), 404

    bidheader.user_id = data.get('user_id', bidheader.user_id)
    bidheader.bidGenre_id = data.get('bidGenre_id', bidheader.bidGenre_id)
    bidheader.bidTypeCode = data.get('bidTypeCode', bidheader.bidTypeCode)
    bidheader.bidStatus = data.get('bidStatus', bidheader.bidStatus)
    bidheader.bidContent_id = data.get('bidContent_id', bidheader.bidContent_id)
    bidheader.bidHeaderText = data['bidHeaderText']
    bidheader.bidExchange1_id = data.get('bidExchange1_id', bidheader.bidExchange1_id)
    bidheader.bidExchange2_id = data.get('bidExchange2_id', bidheader.bidExchange2_id)
    bidheader.bidExchange3_id = data.get('bidExchange3_id', bidheader.bidExchange3_id)
    bidheader.bidExchange4_id = data.get('bidExchange4_id', bidheader.bidExchange4_id)
    bidheader.bidExchange5_id = data.get('bidExchange5_id', bidheader.bidExchange5_id)
    bidheader.bidStartedTime = data['bidStartedTime']
    bidheader.bidEndingTime = data['bidEndingTime']
    bidheader.hdrEditedTime = data['hdrEditedTime']

    db.session.commit()
    return jsonify({'message': 'Bid header updated!'})

#Delete BidHeader

@app.route('/bidheader/<bidheader_id>', methods=['DELETE'])
def delete_bidheader(bidheader_id):
    bidheader = BidHeader.query.get(bidheader_id)
    if not bidheader:
        return jsonify({'message': 'Bid header not found!'}), 404

    db.session.delete(bidheader)
    db.session.commit()
    return jsonify({'message': 'Bid header deleted!'})