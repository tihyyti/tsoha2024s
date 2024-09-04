"""
In the database SQL-script I delivered to you yesterday there are 2 SQL-views. Can you now add the relevant code, which implements those views, which are possibly missing from the models, service classes, controller classes and UI classes and ux ( HTML/CSS in UI) of the Flask-application which we have been converting to yesterday and today, please. These are the SQL views: Data Content: --Names of BidGenre and the number of bids, as well as the time of the latest bidtext submission.
--SQL Queries:

Requires processing of the BidGenre, BidHeader, and BidContent tables.
CREATE VIEW BidGenreList AS
SELECT g.id, g.header, COUNT(c.id) as amount, MAX(c.sendTime) AS latest
FROM BidGenre g
LEFT JOIN BidHeader h ON (g.id = h.bidGnre)
LEFT JOIN BidContent con ON (h.id = con.bidHead)
GROUP by g.id, g.header;

To implement the SQL views in your Flask application using SQLAlchemy, we need to create models for the views and update the service, controller, and UI components accordingly.

Step 1: Define the Models
We’ll create a model for the BidGenreList view.
"""

#This queries and display the data from the BidGenreList view.

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class BidGenreList(db.Model):
    __tablename__ = 'bid_genre_list'
    id = db.Column(db.Integer, primary_key=True)
    header = db.Column(db.String(80), nullable=False)
    amount = db.Column(db.Integer)
    latest = db.Column(db.DateTime)

#Step 2: Updates the Service
#Adds a service method to query the BidGenreList view.

class BidGenreService:
    @staticmethod
    def get_bid_genre_list():
        return BidGenreList.query.all()

#Step 3: Updates the Controller
#Adds a route to fetch data from the BidGenreList view.

from flask import Blueprint, jsonify
from .services import BidGenreService

bid_genre_bp = Blueprint('bid_genre', __name__)

@bid_genre_bp.route('/bid_genre_list', methods=['GET'])
def get_bid_genre_list():
    bid_genre_list = BidGenreService.get_bid_genre_list()
    return jsonify([genre.to_dict() for genre in bid_genre_list])

#Step 4: Updates the UI
#Creates a new HTML template to display the data from the BidGenreList view.

#HTML

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bid Genre List</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="container">
        <h1>Bid Genre List</h1>
        <table>
            <thead>
                <tr>
                    <th>ID</th>
                    <th>Header</th>
                    <th>Amount</th>
                    <th>Latest</th>
                </tr>
            </thead>
            <tbody id="bid-genre-list">
                <!-- Data will be populated here -->
            </tbody>
        </table>
    </div>
    <script>
        fetch('/bid_genre_list')
            .then(response => response.json())
            .then(data => {
                const tableBody = document.getElementById('bid-genre-list');
                data.forEach(item => {
                    const row = document.createElement('tr');
                    row.innerHTML = `
                        <td>${item.id}</td>
                        <td>${item.header}</td>
                        <td>${item.amount}</td>
                        <td>${item.latest}</td>
                    `;
                    tableBody.appendChild(row);
                });
            });
    </script>
</body>
</html>

#CSS

body {
    font-family: Arial, sans-serif;
    background-color: #f4f4f4;
    margin: 0;
    padding: 0;
}

.container {
    width: 80%;
    margin: auto;
    overflow: hidden;
}

h1 {
    color: #333;
    text-align: center;
    margin-top: 20px;
}

table {
    width: 100%;
    border-collapse: collapse;
    margin: 20px 0;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

th, td {
    padding: 10px;
    text-align: left;
    border-bottom: 1px solid #ddd;
}

th {
    background-color: #f2f2f2;
}

tr:hover {
    background-color: #f5f5f5;
}

"""
Sent by you:
This is the 2nd view: --List Bidtexts
--The user is listing the text sections of a specific BidHeader.
--Trigger: The user has selected a specific BidHeader from the “BidHeaders” list.
--Basic functionality: When the user selects a specific BidContent associated with a BidGenre from the “BidGenres” list, the -------relevant text sections related to this opening are displayed on the screen in chronological order. The user can add a new bid ---text or return to the “BidHeaders” list.
--Extensions:
--Bidders can add new text sections to their bids below the “Bidtexts” list.
--Result: The “Bidtexts” list is visible on the bidder’s device, showing Bidder profile info, BidGenre, BidHeader, and BidContent ----along with their respective submission times.
"""
#--SQL queries:
#--Bidheaders of BidGenre. This requires processing the BidGenre and BidHeader tables.
#--Assumed that the bid ID is known.

SELECT BidGenre, BidHeader
FROM BidGenre g
LEFT JOIN BidHeader h ON (g.id = h.bidGnre)
WHERE g.id = h.bidGnre;

BidContent list. Requires processing of the BidHeader and BidContent tables.

CREATE VIEW BidList AS
SELECT h.id, h.initialBidder, h.bidGnre, h.bidHder,
COUNT(*) AS amount, MIN(h.startedTime) AS started,
MAX(h.startedTime) AS latest
FROM BidHeader h
LEFT JOIN BidContent c ON (h.id = c.bidHead)
GROUP BY h.id, h.bidHder, h.initialBidder, h.bidGnre
ORDER BY MAX(h.startedTime) DESC;

#SQL VIEW to query and display the data from the BidList view.
#Creates the necessary models, services, controllers, and UI components.

#Step 1: Defines the Models
#Creates models for the BidGenreList and BidList views

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class BidGenreList(db.Model):
    __tablename__ = 'bid_genre_list'
    id = db.Column(db.Integer, primary_key=True)
    header = db.Column(db.String(80), nullable=False)
    amount = db.Column(db.Integer)
    latest = db.Column(db.DateTime)

class BidList(db.Model):
    __tablename__ = 'bid_list'
    id = db.Column(db.Integer, primary_key=True)
    initialBidder = db.Column(db.String(80), nullable=False)
    bidGnre = db.Column(db.String(80), nullable=False)
    bidHder = db.Column(db.String(80), nullable=False)
    amount = db.Column(db.Integer)
    started = db.Column(db.DateTime)
    latest = db.Column(db.DateTime)

#Step 2: Updates the Service
#Adds service methods to query the BidGenreList and BidList view.

class BidGenreService:
    @staticmethod
    def get_bid_genre_list():
        return BidGenreList.query.all()

class BidListService:
    @staticmethod
    def get_bid_list():
        return BidList.query.all()

#Step 3: Updatse the Controller
#Adds routes to fetch data from the BidGenreList and BidList views.

flask import Blueprint, jsonify
from .services import BidGenreService, BidListService

bid_genre_bp = Blueprint('bid_genre', __name__)

@bid_genre_bp.route('/bid_genre_list', methods=['GET'])
def get_bid_genre_list():
    bid_genre_list = BidGenreService.get_bid_genre_list()
    return jsonify([genre.to_dict() for genre in bid_genre_list])

@bid_genre_bp.route('/bid_list', methods=['GET'])
def get_bid_list():
    bid_list = BidListService.get_bid_list()
    return jsonify([bid.to_dict() for bid in bid_list])

#Step 4: Updates the UI
#Creates new HTML templates to display the data from the BidGenreList and BidList views.


#HTML for Bid Genre List


<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bid Genre List</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="container">
        <h1>Bid Genre List</h1>
        <table>
            <thead>
                <tr>
                    <th>ID</th>
                    <th>Header</th>
                    <th>Amount</th>
                    <th>Latest</th>
                </tr>
            </thead>
            <tbody id="bid-genre-list">
                <!-- Data will be populated here -->
            </tbody>
        </table>
    </div>
    <script>
        fetch('/bid_genre_list')
            .then(response => response.json())
            .then(data => {
                const tableBody = document.getElementById('bid-genre-list');
                data.forEach(item => {
                    const row = document.createElement('tr');
                    row.innerHTML = `
                        <td>${item.id}</td>
                        <td>${item.header}</td>
                        <td>${item.amount}</td>
                        <td>${item.latest}</td>
                    `;
                    tableBody.appendChild(row);
                });
            });
    </script>
</body>
</html>

#HTML for Bid List

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bid List</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="container">
        <h1>Bid List</h1>
        <table>
            <thead>
                <tr>
                    <th>ID</th>
                    <th>Initial Bidder</th>
                    <th>Bid Genre</th>
                    <th>Bid Header</th>
                    <th>Amount</th>
                    <th>Started</th>
                    <th>Latest</th>
                </tr>
            </thead>
            <tbody id="bid-list">
                <!-- Data will be populated here -->
            </tbody>
        </table>
    </div>

    <script>
        fetch('/bid_list')
            .then(response => response.json())
            .then(data => {
                const tableBody = document.getElementById('bid-list');
                data.forEach(item => {
                    const row = document.createElement('tr');
                    row.innerHTML = `
                        <td>${item.id}</td>
                        <td>${item.initialBidder}</td>
                        <td>${item.bidGnre}</td>
                        <td>${item.bidHder}</td>
                        <td>${item.amount}</td>
                        <td>${item.started}</td>
                        <td>${item.latest}</td>
                    `;
                    tableBody.appendChild(row);
                });
            });
    </script>
</body>
</html>

#CSS

body {
    font-family: Arial, sans-serif;
    background-color: #f4f4f4;
    margin: 0;
    padding: 0;
}

.container {
    width: 80%;
    margin: auto;
    overflow: hidden;
}

h1 {
    color: #333;
    text-align: center;
    margin-top: 20px;
}

table {
    width: 100%;
    border-collapse: collapse;
    margin: 20px 0;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

th, td {
    padding: 10px;
    text-align: left;
    border-bottom: 1px solid #ddd;
}

th {
    background-color: #f2f2f2;
}

tr:hover {
    background-color: #f5f5f5;
}
