#Create User CRUD and FETCH

from flask import request, jsonify
from werkzeug.security import generate_password_hash

#Create User

@app.route('/user', methods=['POST'])
def create_user():
    data = request.get_json()
    hashed_password = generate_password_hash(data['password'], method='sha256')
    new_user = User(
        userName=data['userName'],
        password=hashed_password,
        email=data.get('email'),
        secondaryEmail=data.get('secondaryEmail'),
        userIcon_Url=data.get('userIcon_Url'),
        role_id=data['role_id'],
        blocked=data.get('blocked', False),
        latestBidHeader_id=data.get('latestBidHeader_id')
    )
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'New user created!'}), 201

#Fetch All Users

@app.route('/users', methods=['GET'])
def get_all_users():
    users = User.query.all()
    output = []
    for user in users:
        user_data = {
            'id': user.id,
            'userName': user.userName,
            'email': user.email,
            'secondaryEmail': user.secondaryEmail,
            'userIcon_Url': user.userIcon_Url,
            'role_id': user.role_id,
            'blocked': user.blocked,
            'latestBidHeader_id': user.latestBidHeader_id
        }
        output.append(user_data)
    return jsonify({'users': output})

#Fetch One User

@app.route('/user/<user_id>', methods=['GET'])
def get_one_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({'message': 'User not found!'}), 404

    user_data = {
        'id': user.id,
        'userName': user.userName,
        'email': user.email,
        'secondaryEmail': user.secondaryEmail,
        'userIcon_Url': user.userIcon_Url,
        'role_id': user.role_id,
        'blocked': user.blocked,
        'latestBidHeader_id': user.latestBidHeader_id
    }
    return jsonify({'user': user_data})

#Update User

@app.route('/user/<user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    user = User.query.get(user_id)
    if not user:
        return jsonify({'message': 'User not found!'}), 404

    user.userName = data['userName']
    if 'password' in data:
        user.password = generate_password_hash(data['password'], method='sha256')
    user.email = data.get('email')
    user.secondaryEmail = data.get('secondaryEmail')
    user.userIcon_Url = data.get('userIcon_Url')
    user.role_id = data['role_id']
    user.blocked = data.get('blocked', user.blocked)
    user.latestBidHeader_id = data.get('latestBidHeader_id')

    db.session.commit()
    return jsonify({'message': 'User updated!'})

#Delete User

@app.route('/user/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({'message': 'User not found!'}), 404

    db.session.delete(user)
    db.session.commit()
    return jsonify({'message': 'User deleted!'})