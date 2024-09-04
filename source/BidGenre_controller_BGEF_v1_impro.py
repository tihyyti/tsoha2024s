
from flask import Flask, render_template, request, redirect, url_for
from models import db, BidGenreService

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@localhost/yourdatabase'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

bid_genre_service = BidGenreService()

@app.route('/createBidGenre', methods=['GET', 'POST'])
def create_bid_genre():
    if request.method == 'POST':
        bidGenre = request.form['bidGenre']
        bidder = request.form['bidder']
        bidGenreHeader = request.form['bidGenreHeader']
        bid_genre_service.create_bid_genre(bidGenre, bidder, bidGenreHeader)
        return redirect(url_for('get_all_bid_genres'))
    return render_template('create_bid_genre.html')

@app.route('/deleteBidGenre', methods=['GET'])
def delete_bid_genre():
    bid_genre_id = request.args.get('bid_genre_id')
    bid_genre_service.delete_bid_genre(bid_genre_id)
    return redirect(url_for('get_all_bid_genres'))

@app.route('/getBidGenre', methods=['GET'])
def get_bid_genre():
    bid_genre_id = request.args.get('bid_genre_id')
    bid_genre = bid_genre_service.get_bid_genre_by_id(bid_genre_id)
    return render_template('bid_genre.html', bid_genre=bid_genre)

@app.route('/getAllBidGenres', methods=['GET'])
def get_all_bid_genres():
    bid_genres = bid_genre_service.get_all_bid_genres()
    return render_template('bid_genres.html', bid_genres=bid_genres)

@app.route('/updateBidGenre', methods=['GET', 'POST'])
def update_bid_genre():
    if request.method == 'POST':
        bid_genre_id = request.form['bid_genre_id']
        bidGenre = request.form['bidGenre']
        bidder = request.form['bidder']
        bidGenreHeader = request.form['bidGenreHeader']
        bid_genre_service.update_bid_genre(bid_genre_id, bidGenre=bidGenre, bidder=bidder, bidGenreHeader = bidGenreHeader)
        return redirect(url_for('get_all_bid_genres'))
    bid_genre_id = request.args.get('bid_genre_id')
    bid_genre = bid_genre_service.get_bid_genre_by_id(bid_genre_id)
    return render_template('update_bid_genre.html', bid_genre = bid_genre)

@app.route('/assignNewsHeaderToBidGenre/<int:piece_of_news_header_id>', methods=['POST'])
def assign_news_header_to_bid_genre(piece_of_news_header_id):
    bid_genre_id = request.form['bid_genre_id']
    if piece_of_news_header_id is None or bid_genre_id is None:
        return redirect(url_for('get_all_bid_genres'))
    bid_genre_service.assign_news_header_to_bid_genre(bid_genre_id, piece_of_news_header_id)
    return redirect(url_for('get_all_bid_genres'))

@app.route('/assignNewsGenreToBidGenre/<int:news_genre_id>', methods=['POST'])
def assign_news_genre_to_bid_genre(news_genre_id):
    bid_genre_id = request.form['bid_genre_id']
    if news_genre_id is None or bid_genre_id is None:
        return redirect(url_for('get_all_bid_genres'))
    bid_genre_service.assign_news_genre_to_bid_genre(bid_genre_id, news_genre_id)
    return redirect(url_for('get_all_bid_genres'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)

#TEMPLATES: Jinja2

#create_bid_genre.html

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Create Bid Genre</title>
</head>
<body>
    <h1>Create Bid Genre</h1>
    <form action="{{ url_for('create_bid_genre') }}" method="post">
        <label for="bidGenre">Bid Genre:</label>
        <input type="text" id="bidGenre" name="bidGenre" required>
        <br>
        <label for="bidder">Bidder:</label>
        <input type="text" id="bidder" name="bidder" required>
        <br>
        <label for="bidGenreHeader">Bid Genre Header:</label>
        <input type="text" id="bidGenreHeader" name="bidGenreHeader" required>
        <br>
        <button type="submit">Create</button>
    </form>
</body>
</html>

#bid_genre.html

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Bid Genre Details</title>
</head>
<body>
    <h1>Bid Genre Details</h1>
    <p>Bid Genre: {{ bid_genre.bidGenre }}</p>
    <p>Bidder: {{ bid_genre.bidder }}</p>
    <p>Bid Genre Header: {{ bid_genre.bidGenreHeader }}</p>
    <a href="{{ url_for('get_all_bid_genres') }}">Back to Bid Genres List</a>
</body>
</html>

#bid_genres.html

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Bid Genres List</title>
</head>
<body>
    <h1>Bid Genres List</h1>
    <ul>
        {% for bid_genre in bid_genres %}
            <li>{{ bid_genre.bidGenreHeader }} - <a href="{{ url_for('get_bid_genre', bid_genre_id=bid_genre.id) }}">Details</a></li>
        {% endfor %}
    </ul>
    <a href="{{ url_for('create_bid_genre') }}">Create New Bid Genre</a>
</body>
</html>

#update_bid_genre.html

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Update Bid Genre</title>
</head>
<body>
    <h1>Update Bid Genre</h1>
    <form action="{{ url_for('update_bid_genre') }}" method="post">
        <input type="hidden" name="bid_genre_id" value="{{ bid_genre.id }}">
        <label for="bidGenre">Bid Genre:</label>
        <input type="text" id="bidGenre" name="bidGenre" value="{{ bid_genre.bidGenre }}" required>
        <br>
        <label for="bidder">Bidder:</label>
        <input type="text" id="bidder" name="bidder" value="{{ bid_genre.bidder }}" required>
        <br>
        <label for="bidGenreHeader">Bid Genre Header:</label>
        <input type="text" id="bidGenreHeader" name="bidGenreHeader" value="{{ bid_genre.bidGenreHeader }}" required>
        <br>
        <button type="submit">Update</button>
    </form>
</body

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

form {
    background: #fff;
    padding: 20px;
    margin: 20px 0;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

label {
    display: block;
    margin: 10px 0 5px;
}

input[type="text"] {
    width: 100%;
    padding: 10px;
    margin: 5px 0 20px;
    border: 1px solid #ccc;
    border-radius: 4px;
}

button {
    display: inline-block;
    padding: 10px 20px;
    font-size: 16px;
    cursor: pointer;
    background: #333;
    color: #fff;
    border: none;
    border-radius: 4px;
}

button:hover {
    background: #555;
}

ul {
    list-style-type: none;
    padding: 0;
}

li {
    background: #fff;
    margin: 10px 0;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 4px;
}

a {
    color: #333;
    text-decoration: none;
}

a:hover {
    text-decoration: underline;
}