#app/controllers/gear_row_controller.py

from flask import request, jsonify, Blueprint
from app.services.gear_row_service import GearRowService

summary_bp = Blueprint('gear_row', __name__)

@summary_bp.route('/create_gear_row', methods=['POST'])
def create_gear_row():
    data = request.json
    new_row = GearRowService.create_gear_row(data)
    return jsonify(new_row.to_dict()), 201

@summary_bp.route('/update_gear_row/<int:row_id>', methods=['PUT'])
def update_gear_row(row_id):
    data = request.json
    updated_row = GearRowService.update_gear_row(row_id, data)
    return jsonify(updated_row.to_dict()) if updated_row else ('', 404)

@summary_bp.route('/delete_gear_row/<int:row_id>', methods=['DELETE'])
def delete_gear_row(row_id):
    deleted_row = GearRowService.delete_gear_row(row_id)
    return jsonify(deleted_row.to_dict()) if deleted_row else ('', 404)