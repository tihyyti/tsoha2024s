
#CRUD and Fetch service functions for the BidContent class

#Create BidContent

from flask import request, jsonify

@app.route('/bidcontent', methods=['POST'])
def create_bidcontent():
    data = request.get_json()
    new_bidcontent = BidContent(
        bidHeader_id=data.get('bidHeader_id'),
        bidContent=data['bidContent'],
        gear1_id=data.get('gear1_id'),
        gear2_id=data.get('gear2_id'),
        gear3_id=data.get('gear3_id'),
        gear4_id=data.get('gear4_id'),
        gear5_id=data.get('gear5_id'),
        gear6_id=data.get('gear6_id'),
        gear7_id=data.get('gear7_id'),
        gear8_id=data.get('gear8_id'),
        gear9_id=data.get('gear9_id'),
        gear10_id=data.get('gear10_id'),
        conEditedTime=data['conEditedTime'],
        bundleImage_id=data.get('bundleImage_id'),
        bundleSound_id=data.get('bundleSound_id')
    )
    db.session.add(new_bidcontent)
    db.session.commit()
    return jsonify({'message': 'New bid content created!'}), 201

#Fetch All BidContents

@app.route('/bidcontents', methods=['GET'])
def get_all_bidcontents():
    bidcontents = BidContent.query.all()
    output = []
    for bidcontent in bidcontents:
        bidcontent_data = {
            'id': bidcontent.id,
            'bidHeader_id': bidcontent.bidHeader_id,
            'bidContent': bidcontent.bidContent,
            'gear1_id': bidcontent.gear1_id,
            'gear2_id': bidcontent.gear2_id,
            'gear3_id': bidcontent.gear3_id,
            'gear4_id': bidcontent.gear4_id,
            'gear5_id': bidcontent.gear5_id,
            'gear6_id': bidcontent.gear6_id,
            'gear7_id': bidcontent.gear7_id,
            'gear8_id': bidcontent.gear8_id,
            'gear9_id': bidcontent.gear9_id,
            'gear10_id': bidcontent.gear10_id,
            'conEditedTime': bidcontent.conEditedTime,
            'bundleImage_id': bidcontent.bundleImage_id,
            'bundleSound_id': bidcontent.bundleSound_id
        }
        output.append(bidcontent_data)
    return jsonify({'bidcontents': output})

#Fetch One BidContent

@app.route('/bidcontent/<bidcontent_id>', methods=['GET'])
def get_one_bidcontent(bidcontent_id):
    bidcontent = BidContent.query.get(bidcontent_id)
    if not bidcontent:
        return jsonify({'message': 'Bid content not found!'}), 404

    bidcontent_data = {
        'id': bidcontent.id,
        'bidHeader_id': bidcontent.bidHeader_id,
        'bidContent': bidcontent.bidContent,
        'gear1_id': bidcontent.gear1_id,
        'gear2_id': bidcontent.gear2_id,
        'gear3_id': bidcontent.gear3_id,
        'gear4_id': bidcontent.gear4_id,
        'gear5_id': bidcontent.gear5_id,
        'gear6_id': bidcontent.gear6_id,
        'gear7_id': bidcontent.gear7_id,
        'gear8_id': bidcontent.gear8_id,
        'gear9_id': bidcontent.gear9_id,
        'gear10_id': bidcontent.gear10_id,
        'conEditedTime': bidcontent.conEditedTime,
        'bundleImage_id': bidcontent.bundleImage_id,
        'bundleSound_id': bidcontent.bundleSound_id
    }
    return jsonify({'bidcontent': bidcontent_data})

#Update BidContent

@app.route('/bidcontent/<bidcontent_id>', methods=['PUT'])
def update_bidcontent(bidcontent_id):
    data = request.get_json()
    bidcontent = BidContent.query.get(bidcontent_id)
    if not bidcontent:
        return jsonify({'message': 'Bid content not found!'}), 404

    bidcontent.bidHeader_id = data.get('bidHeader_id', bidcontent.bidHeader_id)
    bidcontent.bidContent = data['bidContent']
    bidcontent.gear1_id = data.get('gear1_id', bidcontent.gear1_id)
    bidcontent.gear2_id = data.get('gear2_id', bidcontent.gear2_id)
    bidcontent.gear3_id = data.get('gear3_id', bidcontent.gear3_id)
    bidcontent.gear4_id = data.get('gear4_id', bidcontent.gear4_id)
    bidcontent.gear5_id = data.get('gear5_id', bidcontent.gear5_id)
    bidcontent.gear6_id = data.get('gear6_id', bidcontent.gear6_id)
    bidcontent.gear7_id = data.get('gear7_id', bidcontent.gear7_id)
    bidcontent.gear8_id = data.get('gear8_id', bidcontent.gear8_id)
    bidcontent.gear9_id = data.get('gear9_id', bidcontent.gear9_id)
    bidcontent.gear10_id = data.get('gear10_id', bidcontent.gear10_id)
    bidcontent.conEditedTime = data['conEditedTime']
    bidcontent.bundleImage_id = data.get('bundleImage_id', bidcontent.bundleImage_id)
    bidcontent.bundleSound_id = data.get('bundleSound_id', bidcontent.bundleSound_id)

    db.session.commit()
    return jsonify({'message': 'Bid content updated!'})

#Delete BidContent

@app.route('/bidcontent/<bidcontent_id>', methods=['DELETE'])
def delete_bidcontent(bidcontent_id):
    bidcontent = BidContent.query.get(bidcontent_id)
    if not bidcontent:
        return jsonify({'message': 'Bid content not found!'}), 404

    db.session.delete(bidcontent)
    db.session.commit()
    return jsonify({'message': 'Bid content deleted!'})
