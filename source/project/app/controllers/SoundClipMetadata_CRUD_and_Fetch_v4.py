
#CRUD and Fetch service functions for the SoundClipMetadata class

#Create SoundClipMetadata

from flask import request, jsonify

@app.route('/soundclipmetadata', methods=['POST'])
def create_soundclipmetadata():
    data = request.get_json()
    new_soundclipmetadata = SoundClipMetadata(
        clipName=data['clipName'],
        format=data['format'],
        quality=data['quality'],
        clipLengthInSeconds=data['clipLengthInSeconds'],
        isStereo=data['isStereo'],
        sample_url=data['sample_url']
    )
    db.session.add(new_soundclipmetadata)
    db.session.commit()
    return jsonify({'message': 'New sound clip metadata created!'}), 201

#Fetch All SoundClipMetadata

@app.route('/soundclipmetadatas', methods=['GET'])
def get_all_soundclipmetadatas():
    soundclipmetadatas = SoundClipMetadata.query.all()
    output = []
    for soundclipmetadata in soundclipmetadatas:
        soundclipmetadata_data = {
            'id': soundclipmetadata.id,
            'clipName': soundclipmetadata.clipName,
            'format': soundclipmetadata.format,
            'quality': soundclipmetadata.quality,
            'clipLengthInSeconds': soundclipmetadata.clipLengthInSeconds,
            'isStereo': soundclipmetadata.isStereo,
            'sample_url': soundclipmetadata.sample_url
        }
        output.append(soundclipmetadata_data)
    return jsonify({'soundclipmetadatas': output})

#Fetch One SoundClipMetadata

@app.route('/soundclipmetadata/<soundclipmetadata_id>', methods=['GET'])
def get_one_soundclipmetadata(soundclipmetadata_id):
    soundclipmetadata = SoundClipMetadata.query.get(soundclipmetadata_id)
    if not soundclipmetadata:
        return jsonify({'message': 'Sound clip metadata not found!'}), 404

    soundclipmetadata_data = {
        'id': soundclipmetadata.id,
        'clipName': soundclipmetadata.clipName,
        'format': soundclipmetadata.format,
        'quality': soundclipmetadata.quality,
        'clipLengthInSeconds': soundclipmetadata.clipLengthInSeconds,
        'isStereo': soundclipmetadata.isStereo,
        'sample_url': soundclipmetadata.sample_url
    }
    return jsonify({'soundclipmetadata': soundclipmetadata_data})

#Update SoundClipMetadata

@app.route('/soundclipmetadata/<soundclipmetadata_id>', methods=['PUT'])
def update_soundclipmetadata(soundclipmetadata_id):
    data = request.get_json()
    soundclipmetadata = SoundClipMetadata.query.get(soundclipmetadata_id)
    if not soundclipmetadata:
        return jsonify({'message': 'Sound clip metadata not found!'}), 404

    soundclipmetadata.clipName = data['clipName']
    soundclipmetadata.format = data['format']
    soundclipmetadata.quality = data['quality']
    soundclipmetadata.clipLengthInSeconds = data['clipLengthInSeconds']
    soundclipmetadata.isStereo = data['isStereo']
    soundclipmetadata.sample_url = data['sample_url']

    db.session.commit()
    return jsonify({'message': 'Sound clip metadata updated!'})

#Delete SoundClipMetadata

@app.route('/soundclipmetadata/<soundclipmetadata_id>', methods=['DELETE'])
def delete_soundclipmetadata(soundclipmetadata_id):
    soundclipmetadata = SoundClipMetadata.query.get(soundclipmetadata_id)
    if not soundclipmetadata:
        return jsonify({'message': 'Sound clip metadata not found!'}), 404

    db.session.delete(soundclipmetadata)
    db.session.commit()
    return jsonify({'message': 'Sound clip metadata deleted!'})
