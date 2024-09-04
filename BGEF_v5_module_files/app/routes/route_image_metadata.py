from flask import Blueprint, render_template, request, redirect, url_for
from __init__ import db
import templates

image_metadata_bp = Blueprint('image_metadata', __name__)

@image_metadata_bp.route('/image_metadata/<int:image_id>', methods=['GET', 'POST'])
def image_metadata(image_id):
    conn = None
    cursor = None
    try:
        # Establish the connection
        conn = db
        cursor = conn.cursor()
        if request.method == 'POST':
            imageName = request.form['imageName']
            AxSize = request.form['AxSize']
            resolution = request.form['resolution']
            image_url = request.form['image_url']
            cursor.execute(
                "UPDATE ImageMetadata SET imageName = %s, AxSize = %s, resolution = %s, image_url = %s WHERE id = %s",
                (imageName, AxSize, resolution, image_url, image_id)
            )
            conn.commit()
            return redirect(url_for('index'))
        else:
            cursor.execute('SELECT * FROM ImageMetadata WHERE id = %s', (image_id,))
            image = cursor.fetchone()
    except Exception as e:
        return render_template("error.html", notification=f"Error executing query: {e}")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

    return render_template('image_metadata.html', image=image)

if __name__ == "__main__":
    from my_flask_app import create_app
    app = create_app()
    app.run(debug=True)
