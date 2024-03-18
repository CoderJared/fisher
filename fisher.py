"""
  Create By Jared on $Date
"""
from flask import Flask, make_response

# from config import DEBUG

__author__ = "Jared"

app = Flask(__name__)
app.config.from_object('config')


# print(app.config['DEBUG'])


@app.route('/hello')
def hello_world():
    return "Hello World!"


@app.route('/html')
def hello_html():
    # This is default setting:
    # status code 200,404,301
    # content-type http headers
    # content-type = text/html
    # Response
    return "<h1>Hello World! This is Html</h1>"


@app.route('/testResponse')
def test_response():
    headers = {
        'content-type': 'text/plain'
    }
    response = make_response('<html></html>', 404)
    response.headers = headers
    return response


# app.add_url_rule('/hello', view_func=hello_world)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=app.config['DEBUG'], port=81)
