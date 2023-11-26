#!/usr/bin/python3
"""
A script that starts a Flask web application
using the option strict_slashes=False
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_HBNB():
    """ A method to return hello HBNB """
    return "Hello HBNB!"


if __name__ == "__main__":
    # Run the app
    app.run(host="0.0.0.0", port=5000)
