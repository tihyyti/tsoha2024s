
#app/controllers/system_logs_controller.py

from flask import request, jsonify, Blueprint
from app.services.system_logs_service import SystemLogsService

summary_bp = Blueprint('system_logs', __name__)

@summary_bp.route('/system_logs', methods=['GET'])
def get_system_logs():
    logs = SystemLogsService.get_system_logs()
    return jsonify([log.to_dict() for log in logs])
