
from flask import Blueprint, render_template
# import psycopg2
# from psycopg2 import sql
from __init__ import db
import templates

image_update_bp = Blueprint('image_update', __name__)

# image update
@image_update_bp.route('/image_update/<int:image_id>')
def image_update(image_id):
    conn = db
    cur = conn.cursor()
    cur.execute('SELECT * FROM ImageMetadata WHERE id = %s',(image_id))
    image = cur.fetchone()
    if request.method == 'POST':
        imageName = request.form['imageName']
        AxSize = request.form['AxSize']
        resolution = request.form['resolution']
        image_url = request.form['image_url']
        cur.execute("UPDATE ImageMetadata SET imageName = %s, AxSize = %s, resolution = %s,image_url = %s WHERE image_id = %s", (imageName, AxSize, resolution, image_url, image_id))
        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for('index'))
    cur.close()
    conn.close()
    return render_template('image_update.html', image=image)
