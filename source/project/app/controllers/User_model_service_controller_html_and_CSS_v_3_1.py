"""
These are model and service modules, which are implemented using Spring Boot in Java and the PostgreSQL 16 db. The SQL-script was sent to you yesterday by me for this Flask application we are now converting to today. Please, convert now the following Boot Spring based Java code into Flask and Jinja2 and SQLAlchemy based Service and Model with the help of all the material I have sent you yesterday and today:

@Entity
@Table(name = "User")
public class User extends AbstractPersistable<Long> {

    @Column(name = "userName")
    private String userName;
    @Column(name = "password")
    private String password;

    @OneToMany(mappedBy = "editor", fetch = FetchType.EAGER)
    private List<BidGenre> bidGenres;

    @OneToMany(mappedBy = "startedBy")
    private List<PieceOfNewsHeader> pieceOfNewsHeaders;

    @OneToMany(mappedBy = "editorID")
    private List<PieceOfNewsContent> pieceOfNewsContents;

    public List<BidGenre> getBidGenres() {
        if (this.bidGenres == null) {
            this.bidGenres = new ArrayList<>();
        }
        return this.bidGenres;
    }

    public List<BidGenre> addBidGenres(BidGenre bidGenre) {
        if (this.bidGenres == null) {
            this.bidGenres = new ArrayList<>();
        }
        this.bidGenres.add(bidGenre);
        return this.bidGenres;
    }

    public void delPieceOfNewsHeader(BidGenre bidGenre) {
        if (this.bidGenres == null) {
            return;
        }
        this.bidGenres.remove(bidGenre);
    }

    public List<PieceOfNewsHeader> getPieceOfNewsHeaders() {
        if (this.pieceOfNewsHeaders == null) {
            this.pieceOfNewsHeaders = new ArrayList<>();
        }
        return this.pieceOfNewsHeaders;
    }

    public List<PieceOfNewsHeader> addPieceOfNewsHeader(PieceOfNewsHeader pieceOfNewsHeader) {
        if (this.pieceOfNewsHeaders == null) {
            this.pieceOfNewsHeaders = new ArrayList<>();
        }
        this.pieceOfNewsHeaders.add(pieceOfNewsHeader);
        return this.pieceOfNewsHeaders;
    }

    public void delPieceOfNewsHeader(PieceOfNewsHeader pieceOfNewsHeader) {
        if (this.pieceOfNewsHeaders == null) {
            return;
        }
        this.pieceOfNewsHeaders.remove(pieceOfNewsHeader);
    }

    public List<PieceOfNewsContent> getPieceOfNewsContents() {
        if (this.pieceOfNewsContents == null) {
            this.pieceOfNewsContents = new ArrayList<>();
        }
        return this.pieceOfNewsContents;
    }

    public List<PieceOfNewsContent> addPieceOfNewsContent(PieceOfNewsContent pieceOfNewsContent) {
        if (this.pieceOfNewsContents == null) {
            this.pieceOfNewsContents = new ArrayList<>();
        }
        this.pieceOfNewsContents.add(pieceOfNewsContent);
        return this.pieceOfNewsContents;
    }

    public void delPieceOfNewsContent(PieceOfNewsContent pieceOfNewsContent) {
        if (this.pieceOfNewsContents == null) {
            return;
        }
        this.pieceOfNewsContents.remove(pieceOfNewsContent);
    }

    public User() {
    }

    public User(String userName) {
        this.userName = userName;
        this.password = "";

        List<BidGenre> bidGenres = new ArrayList<>();
        List<PieceOfNewsHeader> pieceOfNewsHeaders = new ArrayList<>();
        List<PieceOfNewsContent> pieceOfNewsContents = new ArrayList<>();
    }

    public User(String userName, String password) {
        this.userName = userName;
        this.password = password;

        List<BidGenre> bidGenres = new ArrayList<>();
        List<PieceOfNewsHeader> pieceOfNewsHeaders = new ArrayList<>();
        List<PieceOfNewsContent> pieceOfNewsContents = new ArrayList<>();
    }

    public String getUserName() {
        return userName;
    }

Let’s convert the provided Spring Boot-based Java code into Flask and SQLAlchemy-based Python code. We’ll create the User model and the corresponding service in Flask.
"""

#Flask Model

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    userName = db.Column(db.String(80), nullable=False)
    password = db.Column(db.String(80), nullable=False)

    bidGenres = db.relationship('BidGenre', backref='editor', lazy=True)
    pieceOfNewsHeaders = db.relationship('PieceOfNewsHeader', backref='startedBy', lazy=True)
    pieceOfNewsContents = db.relationship('PieceOfNewsContent', backref='editorID', lazy=True)

class BidGenre(db.Model):
    __tablename__ = 'news_genre'
    id = db.Column(db.Integer, primary_key=True)
    genre = db.Column(db.String(80), nullable=False)
    editor_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

class PieceOfNewsHeader(db.Model):
    __tablename__ = 'piece_of_news_header'
    id = db.Column(db.Integer, primary_key=True)
    header = db.Column(db.String(200), nullable=False)
    started_by_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

class PieceOfNewsContent(db.Model):
    __tablename__ = 'piece_of_news_content'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    editor_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

#Flask Service

class UserService:
    @staticmethod
    def create_user(userName, password):
        new_user = User(userName=userName, password=password)
        db.session.add(new_user)
        db.session.commit()
        return new_user

    @staticmethod
    def get_user_by_id(user_id):
        return User.query.get(user_id)

    @staticmethod
    def update_user(user_id, **kwargs):
        user = User.query.get(user_id)
        for key, value in kwargs.items():
            setattr(user, key, value)
        db.session.commit()
        return user

    @staticmethod
    def delete_user(user_id):
        user = User.query.get(user_id)
        db.session.delete(user)
        db.session.commit()

#Flask Controller

from flask import Blueprint, request, jsonify
from .services import UserService

user_bp = Blueprint('user', __name__)

@user_bp.route('/user', methods=['POST'])
def create_user():
    data = request.get_json()
    new_user = UserService.create_user(data['userName'], data['password'])
    return jsonify(new_user), 201

@user_bp.route('/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = UserService.get_user_by_id(user_id)
    return jsonify(user)

@user_bp.route('/user/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    updated_user = UserService.update_user(user_id, **data)
    return jsonify(updated_user)

@user_bp.route('/user/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    UserService.delete_user(user_id)
    return '', 204

#HTML and CSS

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>User Management</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="container">
        <h1>User Management System</h1>
        <div id="user-form">
            <h2>Create User</h2>
            <form>
                <label for="userName">User Name:</label>
                <input type="text" id="userName" name="userName" required>
                <label for="password">Password:</label>
                <input type="password" id="password" name="password" required>
                <button type="submit">Create</button>
            </form>
        </div>
    </div>
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

h1, h2 {
    color: #333;
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

input[type="text"], input[type="password"] {
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