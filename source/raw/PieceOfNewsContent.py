from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db = SQLAlchemy(app)

class PieceOfNewsContent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    editorID = db.Column(db.Integer)
    newsHeader = db.Column(db.Integer)
    editor = db.Column(db.String(255))
    content = db.Column(db.String(255))
    sendTime = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, editorID, newsHeader, editor, content, sendTime):
        self.editorID = editorID
        self.newsHeader = newsHeader
        self.editor = editor
        self.content = content
        self.sendTime = sendTime

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)