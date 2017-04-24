from portfolio import app
from flask import render_template

@app.route('/')
def portfolio():
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    return render_template('index.html')
