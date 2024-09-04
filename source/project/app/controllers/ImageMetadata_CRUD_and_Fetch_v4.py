
#CRUD and Fetch service functions for the ImageMetadata class

#Create ImageMetadata

from flask import request, jsonify

@app.route('/imagemetadata', methods=['POST'])
def create_imagemetadata():
    data = request.get_json()
    new_imagemetadata = ImageMetadata(
        imageName=data['imageName'],
        AxSize=data['AxSize'],
        resolution=data['resolution'],
        image_url=data['image_url']
    )
    db.session.add(new_imagemetadata)
    db.session.commit()
    return jsonify({'message': 'New image metadata created!'}), 201

#Fetch All ImageMetadata

@app.route('/imagemetadatas', methods=['GET'])
def get_all_imagemetadatas():
    imagemetadatas = ImageMetadata.query.all()
    output = []
    for imagemetadata in imagemetadatas:
        imagemetadata_data = {
            'id': imagemetadata.id,
            'imageName': imagemetadata.imageName,
            'AxSize': imagemetadata.AxSize,
            'resolution': imagemetadata.resolution,
            'image_url': imagemetadata.image_url
        }
        output.append(imagemetadata_data)
    return jsonify({'imagemetadatas': output})

#Fetch One ImageMetadata

@app.route('/imagemetadata/<imagemetadata_id>', methods=['GET'])
def get_one_imagemetadata(imagemetadata_id):
    imagemetadata = ImageMetadata.query.get(imagemetadata_id)
    if not imagemetadata:
        return jsonify({'message': 'Image metadata not found!'}), 404

    imagemetadata_data = {
        'id': imagemetadata.id,
        'imageName': imagemetadata.imageName,
        'AxSize': imagemetadata.AxSize,
        'resolution': imagemetadata.resolution,
        'image_url': imagemetadata.image_url
    }
    return jsonify({'imagemetadata': imagemetadata_data})

#Update ImageMetadata

@app.route('/imagemetadata/<imagemetadata_id>', methods=['PUT'])
def update_imagemetadata(imagemetadata_id):
    data = request.get_json()
    imagemetadata = ImageMetadata.query.get(imagemetadata_id)
    if not imagemetadata:
        return jsonify({'message': 'Image metadata not found!'}), 404

    imagemetadata.imageName = data['imageName']
    imagemetadata.AxSize = data['AxSize']
    imagemetadata.resolution = data['resolution']
    imagemetadata.image_url = data['image_url']

    db.session.commit()
    return jsonify({'message': 'Image metadata updated!'})

#Delete ImageMetadata

@app.route('/imagemetadata/<imagemetadata_id>', methods=['DELETE'])
def delete_imagemetadata(imagemetadata_id):
    imagemetadata = ImageMetadata.query.get(imagemetadata_id)
    if not imagemetadata:
        return jsonify({'message': 'Image metadata not found!'}), 404

    db.session.delete(imagemetadata)
    db.session.commit()
    return jsonify({'message': 'Image metadata deleted!'})
