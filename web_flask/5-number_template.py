#!/usr/bin/python3
"""
A script that starts a Flask web application
using the option strict_slashes=False
"""

from flask import Flask, render_template, url_for
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
    """ Display "C " followed by the value of the text variable """
    formatted_text = text.replace('_', ' ')
    return f'C {escape(formatted_text)}'


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def display_python(text):
    """ Display "python" followed by the value of the text variable """
    formatted_text = text.replace('_', ' ')
    return f'Python {escape(formatted_text)}'


@app.route('/number/<int:n>', strict_slashes=False)
def display_n(n):
    """ Display "n is a number" only if n is an integer """
    return f'{escape(n)} is a number'


@app.route('/number_template/<int:n>', strict_slashes=False)
def display_number_template(n):
    """ Display a HTML page only if n is an integer """
    return render_template('5-number.html', n=n)


if __name__ == "__main__":
    # Run the app
    app.run(host="0.0.0.0", port=5000)
