from flask import Blueprint, render_template, redirect, url_for, request
from __init__ import db
import templates

image_delete_bp = Blueprint('image_delete', __name__)

@image_delete_bp.route('/image_delete/<int:image_id>', methods=['POST'])
def image_delete(image_id):
    conn = None
    cursor = None
    try:
        # Establish the connection
        conn = db
        cursor = conn.cursor()
        cursor.execute('DELETE FROM ImageMetadata WHERE id = %s', (image_id,))
        conn.commit()
    except Exception as e:
        return render_template("error.html", notification=f"Error executing query: {e}")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

    return redirect(url_for('index'))

if __name__ == "__main__":
    from my_flask_app import create_app
    app = create_app()
    app.run(debug=True)
