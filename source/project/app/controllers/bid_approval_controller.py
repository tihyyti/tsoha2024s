
#app/controllers/bid_approval_controller.py

from flask import request, jsonify, Blueprint
from app.services.bid_approval_service import BidApprovalService

summary_bp = Blueprint('bid_approval', __name__)

@summary_bp.route('/pending_bids', methods=['GET'])
def get_pending_bids():
    bids = BidApprovalService.get_pending_bids()
    return jsonify([bid.to_dict() for bid in bids])

@summary_bp.route('/pending_bids/<int:bid_id>', methods=['PUT'])
def update_bid_status(bid_id):
    data = request.json
    status = data.get('status')
    bid = BidApprovalService.update_bid_status(bid_id, status)
    return jsonify(bid.to_dict()) if bid else ('', 404)
