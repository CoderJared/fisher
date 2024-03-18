"""
  Create By Jared on $Date
"""
from flask import Flask

# from config import DEBUG

__author__ = "Jared"

app = Flask(__name__)
app.config.from_object('config')


# print(app.config['DEBUG'])


@app.route('/hello')
def hello_world():
    return "Hello World!"


# app.add_url_rule('/hello', view_func=hello_world)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=app.config['DEBUG'], port=81)
