
#app/controllers/user_management_controller.py

from flask import request, jsonify, Blueprint
from app.services.user_management_service import UserManagementService

summary_bp = Blueprint('user_management', __name__)

@summary_bp.route('/users', methods=['GET'])
def get_all_users():
    users = UserManagementService.get_all_users()
    return jsonify([user.to_dict() for user in users])

@summary_bp.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.json
    user = UserManagementService.update_user(user_id, data)
    return jsonify(user.to_dict()) if user else ('', 404)