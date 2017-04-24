import os

from flask import Flask

app = Flask(__name__)
app.config.from_object('portfolio_config')
app.config.from_envvar('PORTFOLIO_SETTINGS', silent=True)

from portfolio import views
