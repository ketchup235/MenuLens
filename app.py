from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    menu= request.files['pdf']
    if menu:
        print("INSERT CODE TO SCRAPE PDF FPR KEYWORDS")
    return render_template('upload.html')