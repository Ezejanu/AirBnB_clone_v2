#!/usr/bin/python3
"""
A script that starts a Flask web application
using the option strict_slashes=False
"""

from flask import Flask, render_template
from markupsafe import escape

app = Flask(__name__)


@app.route("/hello_HBNB", strict_slashes=False)
def hello_HBNB():
    """ A method to display "hello HBNB" """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ A method to display "HBNB" """
    return "HBNB"


@app.route('/c/<text>')
def show_entry(text):
    """show C with the variable text entered"""
    return "C " + text.replace('_', ' ')


if __name__ == "__main__":
    # Run the app
    app.run(host="0.0.0.0", port=5000)
