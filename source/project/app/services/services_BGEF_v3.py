
#app/services/gear_bundle_service.py

from datetime import datetime
from app.models import db, GearBundle

class GearBundleService:
    @staticmethod
    def create_gear_bundle(data):
        new_bundle = GearBundle(
            bundleName=data['bundleName'],
            price=data['price'],
            created_at=datetime.utcnow()
        )
        db.session.add(new_bundle)
        db.session.commit()
        return new_bundle

    @staticmethod
    def update_gear_bundle(bundle_id, data):
        bundle = GearBundle.query.get(bundle_id)
        if bundle:
            bundle.bundleName = data.get('bundleName', bundle.bundleName)
            bundle.price = data.get('price', bundle.price)
            bundle.updated_at = datetime.utcnow()
            db.session.commit()
        return bundle

    @staticmethod
    def delete_gear_bundle(bundle_id):
        bundle = GearBundle.query.get(bundle_id)
        if bundle:
            db.session.delete(bundle)
            db.session.commit()
        return bundle

    @staticmethod
    def get_my_gear_bundles():
        return GearBundle.query.all()

#app/services/gear_row_service.py

from app.models import db, GearRow

class GearRowService:
    @staticmethod
    def create_gear_row(data):
        new_row = GearRow(
            bundleID=data['bundleID'],
            # Other fields...
        )
        db.session.add(new_row)
        db.session.commit()
        return new_row

    @staticmethod
    def update_gear_row(row_id, data):
        row = GearRow.query.get(row_id)
        if row:
            row.bundleID = data.get('bundleID', row.bundleID)
            # Update other fields...
            db.session.commit()
        return row

    @staticmethod
    def delete_gear_row(row_id):
        row = GearRow.query.get(row_id)
        if row:
            db.session.delete(row)
            db.session.commit()
        return row

#app/services/user_management_service.py

from app.models import db, UserManagement

class UserManagementService:
    @staticmethod
    def get_all_users():
        return UserManagement.query.all()

    @staticmethod
    def update_user(user_id, data):
        user = UserManagement.query.get(user_id)
        if user:
            user.username = data.get('username', user.username)
            user.email = data.get('email', user.email)
            user.is_active = data.get('is_active', user.is_active)
            db.session.commit()
        return user

#app/services/system_logs_service.py

from app.models import db, SystemLogs

class SystemLogsService:
    @staticmethod
    def get_system_logs():
        return SystemLogs.query.all()

#app/services/bid_approval_service.py

from app.models import db, BidApproval

class BidApprovalService:
    @staticmethod
    def get_pending_bids():
        return BidApproval.query.all()

    @staticmethod
    def update_bid_status(bid_id, status):
        bid = BidApproval.query.get(bid_id)
        if bid:
            bid.status = status
            db.session.commit()
        return bid
