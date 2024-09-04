from flask import Flask
from flask_sqlalchemy import SQLAlchemy
#
# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@localhost/dbname'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)
#
class ImageMetadata(db.Model):
    __tablename__ = 'ImageMetadata'
    id = db.Column(db.Integer, primary_key=True)
    imageName = db.Column(db.String(100), nullable=False)
    AxSize = db.Column(db.String(10), nullable=False)
    resolution = db.Column(db.String(20), nullable=False)
    image_url = db.Column(db.String(255), nullable=False)

class SoundClipMetadata(db.Model):
    __tablename__ = 'SoundClipMetadata'
    id = db.Column(db.Integer, primary_key=True)
    clipName = db.Column(db.String(100), nullable=False)
    format = db.Column(db.String(10), nullable=False)
    quality = db.Column(db.String(30), nullable=False)
    clipLengthInSeconds = db.Column(db.Float, nullable=False)
    isStereo = db.Column(db.Boolean, nullable=False)
    sample_url = db.Column(db.String(255), nullable=False)

class Client(db.Model):
    __tablename__ = 'Client'
    id = db.Column(db.Integer, primary_key=True)
    userName = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(25))
    email = db.Column(db.String(50))
    secondaryEmail = db.Column(db.String(50))
    userIcon_id = db.Column(db.Integer, db.ForeignKey('ImageMetadata.id'))
    roleName = db.Column(db.String(50), nullable=False, unique=True)
    registeredUser = db.Column(db.Boolean, default=False)
    sellerRole = db.Column(db.Boolean, default=False)
    buyerRole = db.Column(db.Boolean, default=False)
    adminRole = db.Column(db.Boolean, default=False)
    blocked = db.Column(db.Boolean, default=False)

class BidGenre(db.Model):
    __tablename__ = 'BidGenre'
    id = db.Column(db.Integer, primary_key=True)
    bidGenreHeader = db.Column(db.String(100), nullable=False, unique=True)

class BidExchange(db.Model):
    __tablename__ = 'BidExchange'
    id = db.Column(db.Integer, primary_key=True)
    salesBidder_id = db.Column(db.Integer, db.ForeignKey('Client.id'), nullable=False)
    salesBidHeader_id = db.Column(db.Integer, db.ForeignKey('BidHeader.id'), nullable=False)
    purchaseBidder_id = db.Column(db.Integer, db.ForeignKey('Client.id'), nullable=False)
    purchaseBidHeader_id = db.Column(db.Integer, db.ForeignKey('BidHeader.id'), nullable=False)
    agreedDeal = db.Column(db.Boolean, default=False)
    otherConditions = db.Column(db.Text)
    addOnValue = db.Column(db.Float, default=0.00)
    dealTimestamp = db.Column(db.TIMESTAMP, nullable=False)

class Gear(db.Model):
    __tablename__ = 'Gear'
    id = db.Column(db.Integer, primary_key=True)
    gearBrand = db.Column(db.String(30), nullable=False)
    gearCode = db.Column(db.Integer)
    gearStatus = db.Column(db.Integer)
    bidHeader_id = db.Column(db.Integer, db.ForeignKey('BidHeader.id'))
    gearName = db.Column(db.String(100), nullable=False)
    gearDetails = db.Column(db.Text)
    gearStory = db.Column(db.Text)
    amountOffered = db.Column(db.Integer, nullable=False)
    approxValue = db.Column(db.Float, default=0.00)
    user_id = db.Column(db.Integer, db.ForeignKey('Client.id'))
    comments = db.Column(db.Text)
    createdTime = db.Column(db.TIMESTAMP, nullable=False)
    editedTime = db.Column(db.TIMESTAMP, nullable=False)
    gearImage_id = db.Column(db.Integer, db.ForeignKey('ImageMetadata.id'))
    soundClip_id = db.Column(db.Integer, db.ForeignKey('SoundClipMetadata.id'))

class BidHeader(db.Model):
    __tablename__ = 'BidHeader'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('Client.id'))
    bidGenre_id = db.Column(db.Integer, db.ForeignKey('BidGenre.id'))
    bidTypeCode = db.Column(db.Integer)
    bidStatus = db.Column(db.Integer)
    bidexchange_id = db.Column(db.Integer, db.ForeignKey('BidExchange.id'))
    bidHeaderText = db.Column(db.String(100), nullable=False, unique=True)
    bidContent = db.Column(db.String(300), nullable=False)
    gear1_id = db.Column(db.Integer, db.ForeignKey('Gear.id'))
    gear2_id = db.Column(db.Integer, db.ForeignKey('Gear.id'))
    gear3_id = db.Column(db.Integer, db.ForeignKey('Gear.id'))
    gear4_id = db.Column(db.Integer, db.ForeignKey('Gear.id'))
    gear5_id = db.Column(db.Integer, db.ForeignKey('Gear.id'))
    gear6_id = db.Column(db.Integer, db.ForeignKey('Gear.id'))
    gear7_id = db.Column(db.Integer, db.ForeignKey('Gear.id'))
    gear8_id = db.Column(db.Integer, db.ForeignKey('Gear.id'))
    gear9_id = db.Column(db.Integer, db.ForeignKey('Gear.id'))
    gear10_id = db.Column(db.Integer, db.ForeignKey('Gear.id'))
    bundleImage_id = db.Column(db.Integer, db.ForeignKey('ImageMetadata.id'))
    bundleSound_id = db.Column(db.Integer, db.ForeignKey('SoundClipMetadata.id'))
    hdrEditedTime = db.Column(db.TIMESTAMP, nullable=False)
    conEditedTime = db.Column(db.TIMESTAMP, nullable=False)
    bidStartingTime = db.Column(db.TIMESTAMP, nullable=False)
    bidEndingTime = db.Column(db.TIMESTAMP, nullable=False)
    bidCreatedTime = db.Column(db.TIMESTAMP, nullable=False)

if __name__ == '__main__':
    # with app.app_context():
        # db.create_all()
#
# The CRUD-kontrollers without using any ORM.  Instead SQL-query-statements and connection to db is #used. Also Jinja2 UI-templates and Bootstrap style-library plus embedded javascript component for #tables in UI:
# 1. Setting Up the Database Connection
#
from flask import Flask, render_template, request, redirect, url_for
import psycopg2

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(
        dbname='dbBGEF_v5',
        user='postgres',
        password='postinLent0',
        host='localhost'
    )
    return conn

# CRUD Controllers:

# Create
@app.route('/create_image', methods=['GET', 'POST'])
def create_image():
    if request.method == 'POST':
        imageName = request.form['imageName']
        AxSize = request.form['AxSize']
        resolution = request.form['resolution']
        image_url = request.form['image_url']

        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("INSERT INTO ImageMetadata (imageName, AxSize, resolution, image_url) VALUES (%s, %s, %s, %s)", (imageName, AxSize, resolution, image_url))
        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for('index'))
    return render_template('image_create.html')

@app.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM ImageMetadata')
    images = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('index.html', images=images)
@app.route('/update_image/<int:id>', methods=['GET', 'POST'])
def update_image(id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM ImageMetadata WHERE id = %s', (id,))
    image = cur.fetchone()
    if request.method == 'POST':
        imageName = request.form['imageName']
        AxSize = request.form['AxSize']
        resolution = request.form['resolution']
        image_url = request.form['image_url']
        cur.execute("UPDATE ImageMetadata SET imageName = %s, AxSize = %s, resolution = %s, image_url = %s WHERE id = %s", (imageName, AxSize, resolution, image_url, id))
        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for('index'))
    cur.close()
    conn.close()
    return render_template('image_update.html', image=image)

@app.route('/delete_image/<int:id>', methods=['POST'])
def delete_image(id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('DELETE FROM ImageMetadata WHERE id = %s', (id,))
    conn.commit()
    cur.close()
    conn.close()
    return redirect(url_for('index'))

# Templates: CRUD-UI

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}{% endblock %}</title>
    <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
    <div class="container">
        {% block content %}{% endblock %}
    </div>
    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.5.4/dist/umd/popper.min.js"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
</body>
</html>

{% extends "base.html" %}
{% block title %}Image Metadata{% endblock %}
{% block content %}
    <h1>Image Metadata</h1>
    <a href="{{ url_for('create_image') }}" class="btn btn-primary">Add New Image</a>
    <table class="table table-striped">
        <thead>
            <tr>
                <th>ID</th>
                <th>Image Name</th>
                <th>Ax Size</th>
                <th>Resolution</th>
                <th>Image URL</th>
                <th>Actions</th>
            </tr>
        </thead>
        <tbody>
            {% for image in images %}
            <tr>
                <td>{{ image[0] }}</td>
                <td>{{ image[1] }}</td>
                <td>{{ image[2] }}</td>
                <td>{{ image[3] }}</td>
                <td>{{ image[4] }}</td>
                <td>
                    <a href="{{ url_for('update_image', id=image[0]) }}" class="btn btn-warning">Edit</a>
                    <form action="{{ url_for('delete_image', id=image[0]) }}" method="post" style="display:inline;">
                        <button type="submit" class="btn btn-danger">Delete</button>
                    </form>
                </td>
            </tr>
            {% endfor %}
        </tbody>
    </table>
{% endblock %}

{% extends "base.html" %}
{% block title %}Create Image{% endblock %}
{% block content %}
    <h1>Create New Image</h1>
    <form method="post">
        <div class="form-group">
            <label for="imageName">Image Name</label>
            <input type="text" class="form-control" id="imageName" name="imageName" required>
        </div>
        <div class="form-group">
            <label for="AxSize">Ax Size</label>
            <input type="text" class="form-control" id="AxSize" name="AxSize" required>
        </div>
        <div class="form-group">
            <label for="resolution">Resolution</label>
            <input type="text" class="form-control" id="resolution" name="resolution" required>
        </div>
        <div class="form-group">
            <label for="image_url">Image URL</label>
            <input type="text" class="form-control" id="image_url" name="image_url" required>
        </div>
        <button type="submit" class="btn btn-primary">Submit</button>
    </form>
{% endblock %}

{% extends "base.html" %}
{% block title %}Update Image{% endblock %}
{% block content %}
    <h1>Update Image</h1>
    <form method="post">
        <div class="form-group">
            <label for="imageName">Image Name</label>
            <input type="text" class="form-control" id="imageName" name="imageName" value="{{ image[1] }}" required>
        </div>
        <div class="form-group">
            <label for="AxSize">Ax Size</label>
            <input type="text" class="form-control" id="AxSize" name="AxSize" value="{{ image[2] }}" required>
        </div>
        <div class="form-group">
            <label for="resolution">Resolution</label>
            <input type="text" class="form-control" id="resolution" name="resolution" value="{{ image[3] }}" required>
        </div>
        <div class="form-group">
            <label for="image_url">Image URL</label>
            <input type="text" class="form-control" id="image_url" name="image_url" value="{{ image[4] }}" required>
        </div>
        <button type="submit" class="btn btn-primary">Submit</button>
    </form>
{% endblock %}
#
# JavaScript Component for Tables:
# To enhance the table functionality, the following dataTables-component can be added to  base.html:
#
# <link rel="stylesheet" type="text/css" href="https://cdn.datatables.net/1.10.21/css/jquery.dataTables.css">
# # <script type="text/javascript" charset="utf8" src="https://cdn.datatables.net/1.10.21/js/jquery.dataTables.js"></script>
# <script>
    # $(document).ready(function() {
        # $('.table').DataTable();
    # });
# </script
#