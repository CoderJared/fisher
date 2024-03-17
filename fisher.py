"""
  Create By Jared on $Date
"""
from flask import Flask

__author__ = "Jared"

app = Flask(__name__)


@app.route('/hello')
def hello_world():
    return "Hello World!"


app.run(debug=True)
