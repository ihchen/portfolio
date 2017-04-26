import os

from flask import Flask, render_template, redirect

app = Flask(__name__)
app.config.from_object('portfolio_config')
app.config.from_envvar('PORTFOLIO_SETTINGS', silent=True)

@app.route('/')
def portfolio():
    return render_template('index.html')

@app.route('/<path:project>')
def project(project):
    if project == "soundulate":
        url = "https://turing.pugetsound.edu/soundulate/"
    elif project == "mempassgen":
        url = "https://ihchen.github.io/mempassgen"
    else:
        return redirect('/')
    return render_template('project.html', url=url)
