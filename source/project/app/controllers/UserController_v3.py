
#Flask Controller

from flask import Blueprint, request, jsonify
from .services import UserService

user_bp = Blueprint('user', __name__)

@user_bp.route('/user', methods=['POST'])
def create_user():
    data = request.get_json()
    new_user = UserService.create_user(data['userName'], data['password'])
    return jsonify(new_user), 201

@user_bp.route('/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = UserService.get_user_by_id(user_id)
    return jsonify(user)

@user_bp.route('/user/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    updated_user = UserService.update_user(user_id, **data)
    return jsonify(updated_user)

@user_bp.route('/user/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    UserService.delete_user(user_id)
    return '', 204
