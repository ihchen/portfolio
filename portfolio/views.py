from portfolio import app
from flask import render_template

@app.route('/')
def portfolio():
    return render_template('index.html')
