import os

from flask import Flask, render_template

app = Flask(__name__)
app.config.from_object('portfolio_config')
app.config.from_envvar('PORTFOLIO_SETTINGS', silent=True)

@app.route('/')
def portfolio():
    return render_template('index.html')
