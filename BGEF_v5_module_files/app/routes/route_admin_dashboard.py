import templates
from middleware import admin_required

admin_dashboard_bp = Blueprint('admin_dashboard', __name__)

@admin_dashboard_bp.route('/admin/dashboard')
@admin_required
def admin_dashboard():
    return 'Admin Dashboard'
    return redirect(f"/teacher/{username}")