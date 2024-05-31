#!/usr/bin/env python3
""" 2-app simple flask app with babel """

from flask import Flask, render_template, request
from flask_babel import Babel


class Config(object):
    """ Config class """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.route('/', strict_slashes=False)
def index():
    """ 2-app simple flask app """
    return render_template('2-index.html')


@babel.localeselector
def get_locale():
    """ get_locale """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
