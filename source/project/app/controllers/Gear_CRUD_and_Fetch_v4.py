
#CRUD and Fetch service functions for the Gear class

#Create Gear

from flask import request, jsonify

@app.route('/gear', methods=['POST'])
def create_gear():
    data = request.get_json()
    new_gear = Gear(
        gearBrand=data['gearBrand'],
        gearCode=data.get('gearCode'),
        gearStatus=data.get('gearStatus'),
        bidHeader_id=data.get('bidHeader_id'),
        gearName=data['gearName'],
        gearDetails=data.get('gearDetails'),
        gearStory=data.get('gearStory'),
        amountOffered=data['amountOffered'],
        approxValue=data.get('approxValue', 0.00),
        user_id=data.get('user_id'),
        comments=data.get('comments'),
        editedTime=data['editedTime'],
        gearImage_id=data.get('gearImage_id'),
        soundClip_id=data.get('soundClip_id')
    )
    db.session.add(new_gear)
    db.session.commit()
    return jsonify({'message': 'New gear created!'}), 201

#Fetch All Gears

@app.route('/gears', methods=['GET'])
def get_all_gears():
    gears = Gear.query.all()
    output = []
    for gear in gears:
        gear_data = {
            'id': gear.id,
            'gearBrand': gear.gearBrand,
            'gearCode': gear.gearCode,
            'gearStatus': gear.gearStatus,
            'bidHeader_id': gear.bidHeader_id,
            'gearName': gear.gearName,
            'gearDetails': gear.gearDetails,
            'gearStory': gear.gearStory,
            'amountOffered': gear.amountOffered,
            'approxValue': gear.approxValue,
            'user_id': gear.user_id,
            'comments': gear.comments,
            'editedTime': gear.editedTime,
            'gearImage_id': gear.gearImage_id,
            'soundClip_id': gear.soundClip_id
        }
        output.append(gear_data)
    return jsonify({'gears': output})

#Fetch One Gear

@app.route('/gear/<gear_id>', methods=['GET'])
def get_one_gear(gear_id):
    gear = Gear.query.get(gear_id)
    if not gear:
        return jsonify({'message': 'Gear not found!'}), 404

    gear_data = {
        'id': gear.id,
        'gearBrand': gear.gearBrand,
        'gearCode': gear.gearCode,
        'gearStatus': gear.gearStatus,
        'bidHeader_id': gear.bidHeader_id,
        'gearName': gear.gearName,
        'gearDetails': gear.gearDetails,
        'gearStory': gear.gearStory,
        'amountOffered': gear.amountOffered,
        'approxValue': gear.approxValue,
        'user_id': gear.user_id,
        'comments': gear.comments,
        'editedTime': gear.editedTime,
        'gearImage_id': gear.gearImage_id,
        'soundClip_id': gear.soundClip_id
    }
    return jsonify({'gear': gear_data})

#Update Gear

@app.route('/gear/<gear_id>', methods=['PUT'])
def update_gear(gear_id):
    data = request.get_json()
    gear = Gear.query.get(gear_id)
    if not gear:
        return jsonify({'message': 'Gear not found!'}), 404

    gear.gearBrand = data['gearBrand']
    gear.gearCode = data.get('gearCode', gear.gearCode)
    gear.gearStatus = data.get('gearStatus', gear.gearStatus)
    gear.bidHeader_id = data.get('bidHeader_id', gear.bidHeader_id)
    gear.gearName = data['gearName']
    gear.gearDetails = data.get('gearDetails', gear.gearDetails)
    gear.gearStory = data.get('gearStory', gear.gearStory)
    gear.amountOffered = data['amountOffered']
    gear.approxValue = data.get('approxValue', gear.approxValue)
    gear.user_id = data.get('user_id', gear.user_id)
    gear.comments = data.get('comments', gear.comments)
    gear.editedTime = data['editedTime']
    gear.gearImage_id = data.get('gearImage_id', gear.gearImage_id)
    gear.soundClip_id = data.get('soundClip_id', gear.soundClip_id)

    db.session.commit()
    return jsonify({'message': 'Gear updated!'})

#Delete Gear

@app.route('/gear/<gear_id>', methods=['DELETE'])
def delete_gear(gear_id):
    gear = Gear.query.get(gear_id)
    if not gear:
        return jsonify({'message': 'Gear not found!'}), 404

    db.session.delete(gear)
    db.session.commit()
    return jsonify({'message': 'Gear deleted!'})
