
#Bidder Summary: This view provides a summary of each bidder, including their name,
#the total number of bids they have made, and the latest edited time for any of their bids.

CREATE VIEW BidderSummary AS
SELECT b.id AS bidder_id, b.bidderName, COUNT(bc.id) AS total_bids,
       MAX(bc.editedTime) AS latest_bid_time
FROM Bidder b
LEFT JOIN BidContent bc ON b.id = bc.bidderID
GROUP BY b.id, b.bidderName;

#Top Bidders by Bid Count: This view lists the top bidders based on the number of bids they’ve made, ordered by the count
#in descending order.

CREATE VIEW TopBidders AS
SELECT b.id AS bidder_id, b.bidderName, COUNT(bc.id) AS total_bids
FROM Bidder b
LEFT JOIN BidContent bc ON b.id = bc.bidderID
GROUP BY b.id, b.bidderName
ORDER BY total_bids DESC;

#Bid Genre Statistics: This view provides statistics for each bid genre, including the total number of bids in that genre
#and the average time between bid edits.

CREATE VIEW GenreStatistics AS
SELECT bg.id AS genre_id, bg.bidGenreHeader, COUNT(bc.id) AS total_bids,
       AVG(EXTRACT(EPOCH FROM (bc.editedTime - bh.startedTime))) AS avg_edit_time
FROM BidGenre bg
LEFT JOIN BidHeader bh ON bg.id = bh.bidGnre
LEFT JOIN BidContent bc ON bh.id = bc.bidHead
GROUP BY bg.id, bg.bidGenreHeader

#The code to implement the views BidderSummary, TopBidders, and GenreStatistics in Flask application.
#Creates models for these views, updates the service and controller classes, and adsd the necessary UI components.

#Step 1: Define the Models
#Creates models for the BidderSummary, TopBidders, and GenreStatistics views.

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class BidderSummary(db.Model):
    __tablename__ = 'bidder_summary'
    bidder_id = db.Column(db.Integer, primary_key=True)
    bidderName = db.Column(db.String(80), nullable=False)
    total_bids = db.Column(db.Integer)
    latest_bid_time = db.Column(db.DateTime)

class TopBidders(db.Model):
    __tablename__ = 'top_bidders'
    bidder_id = db.Column(db.Integer, primary_key=True)
    bidderName = db.Column(db.String(80), nullable=False)
    total_bids = db.Column(db.Integer)

class GenreStatistics(db.Model):
    __tablename__ = 'genre_statistics'
    genre_id = db.Column(db.Integer, primary_key=True)
    bidGenreHeader = db.Column(db.String(80), nullable=False)
    total_bids = db.Column(db.Integer)
    avg_edit_time = db.Column(db.Float)

#Step 2: Updates the Service
#Adds service methods to query the BidderSummary, TopBidders, and GenreStatistics views

class BidderSummaryService:
    @staticmethod
    def get_bidder_summary():
        return BidderSummary.query.all()

class TopBiddersService:
    @staticmethod
    def get_top_bidders():
        return TopBidders.query.all()

class GenreStatisticsService:
    @staticmethod
    def get_genre_statistics():
        return GenreStatistics.query.all()

#Step 3: Updates the Controller
Adds routes to fetch data from the BidderSummary, TopBidders, and GenreStatistics views.

from flask import Blueprint, jsonify
from .services import BidderSummaryService, TopBiddersService, GenreStatisticsService

summary_bp = Blueprint('summary', __name__)

@summary_bp.route('/bidder_summary', methods=['GET'])
def get_bidder_summary():
    summary = BidderSummaryService.get_bidder_summary()
    return jsonify([s.to_dict() for s in summary])

@summary_bp.route('/top_bidders', methods=['GET'])
def get_top_bidders():
    top_bidders = TopBiddersService.get_top_bidders()
    return jsonify([tb.to_dict() for tb in top_bidders])

@summary_bp.route('/genre_statistics', methods=['GET'])
def get_genre_statistics():
    stats = GenreStatisticsService.get_genre_statistics()
    return jsonify([gs.to_dict() for gs in stats])

#Step 4: Updates the UI
#Creates new HTML templates to display the data from the BidderSummary, TopBidders, and GenreStatistics views.

#HTML for Bidder Summary

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bidder Summary</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="container">
        <h1>Bidder Summary</h1>
        <table>
            <thead>
                <tr>
                    <th>Bidder ID</th>
                    <th>Bidder Name</th>
                    <th>Total Bids</th>
                    <th>Latest Bid Time</th>
                </tr>
            </thead>
            <tbody id="bidder-summary">
                <!-- Data will be populated here -->
            </tbody>
        </table>
    </div>
    <script>
        fetch('/bidder_summary')
            .then(response => response.json())
            .then(data => {
                const tableBody = document.getElementById('bidder-summary');
                data.forEach(item => {
                    const row = document.createElement('tr');
                    row.innerHTML = `
                        <td>${item.bidder_id}</td>
                        <td>${item.bidderName}</td>
                        <td>${item.total_bids}</td>
                        <td>${item.latest_bid_time}</td>
                    `;
                    tableBody.appendChild(row);
                });
            });
    </script>
</body>
</html>

#HTML for Top Bidders

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Top Bidders</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="container">
        <h1>Top Bidders</h1>
        <table>
            <thead>
                <tr>
                    <th>Bidder ID</th>
                    <th>Bidder Name</th>
                    <th>Total Bids</th>
                </tr>
            </thead>
            <tbody id="top-bidders">
                <!-- Data will be populated here -->
            </tbody>
        </table>
    </div>
    <script>
        fetch('/top_bidders')
            .then(response => response.json())
            .then(data => {
                const tableBody = document.getElementById('top-bidders');
                data.forEach(item => {
                    const row = document.createElement('tr');
                    row.innerHTML = `
                        <td>${item.bidder_id}</td>
                        <td>${item.bidderName}</td>
                        <td>${item.total_bids}</td>
                    `;
                    tableBody.appendChild(row);
                });
            });
    </script>
</body>
</html>

#HTML for Genre Statistics
HTML

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Genre Statistics</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="container">
        <h1>Genre Statistics</h1>
        <table>
            <thead>
                <tr>
                    <th>Genre ID</th>
                    <th>Bid Genre Header</th>
                    <th>Total Bids</th>
                    <th>Average Edit Time</th>
                </tr>
            </thead>
            <tbody id="genre-statistics">
                <!-- Data will be populated here -->
            </tbody>
        </table>
    </div>
    <script>
        fetch('/genre_statistics')
            .then(response => response.json())
            .then(data => {
                const tableBody = document.getElementById('genre-statistics');
                data.forEach(item => {
                    const row = document.createElement('tr');
                    row.innerHTML = `
                        <td>${item.genre_id}</td>
                        <td>${item.bidGenreHeader}</td>
                        <td>${item.total_bids}</td>
                        <td>${item.avg_edit_time}</td>
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
