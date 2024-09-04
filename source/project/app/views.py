from flask import render_template
from app import create_ap

app = create_app()

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')