from flask import render_template
from app import app


@app.route("/")
@app.route("/hello")
def hello():
    return 'Hello, World'