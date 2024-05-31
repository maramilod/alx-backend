#!/usr/bin/env python3
""" 6-app simple flask app with babel """

from typing import Optional
from flask import Flask, g, render_template, request
from flask_babel import Babel


class Config(object):
    """ Config class for languages"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


@app.route('/', strict_slashes=False)
def index() -> str:
    """ 6-app simple flask app """
    return render_template('6-index.html')


@babel.localeselector
def get_locale() -> str:
    """
    This function is used to select the best match locale based on the
      following criteria:
    1. If the locale is passed as a query parameter, it will be used if it is
       supported by the app.
    2. If the user is logged in and has a locale set, it will be used if it is
       supported by the app.
    3. If the locale is passed as a header, it will be used if it is supported
      by the app.
    4. If none of the above conditions are met, the function will return the
      best match locale based on the user's browser preferences.
    """
    # Check if locale is passed as a query parameter
    locale = request.args.get('locale')
    if locale in app.config["LANGUAGES"]:
        return locale

    # Check if user is logged in and has a locale set
    if g.user and g.user.get('locale') in app.config["LANGUAGES"]:
        return g.user.get('locale')

    # Check if locale is passed as a header
    locale = request.headers.get('locale')
    if locale in app.config["LANGUAGES"]:
        return locale

    # Return the best match locale based on the user's browser preferences
    return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_user() -> Optional[dict]:
    """ get_user returns a user dictionary or None if the ID cannot be found
    or if login_as was not passed
    """
    user_id = request.args.get('login_as')
    if user_id:
        return users.get(int(user_id))
    return None


@app.before_request
def before_request() -> None:
    """ before_request """
    g.user = get_user()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
