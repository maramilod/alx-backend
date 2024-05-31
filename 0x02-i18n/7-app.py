#!/usr/bin/env python3
""" 7-app simple flask app with babel """

from typing import Optional
from flask import Flask, g, render_template, request
from flask_babel import Babel
import pytz


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
    """ 7-app simple flask app """
    return render_template('7-index.html')


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


@babel.timezoneselector
def get_timezone() -> str:
    """
    Get the best match timezone based on the following criteria:
    1. If the timezone is passed as a query parameter, it will be used if it is
       a valid timezone.
    2. If the user is logged in and has a timezone set, it will be used if it
      is a valid timezone.
    3. If none of the above conditions are met, the function will return the
       default timezone set in the app's configuration.

    Returns:
        str: The best match timezone.
    """
    # Check if timezone is passed as a query parameter
    timezone = request.args.get('timezone')

    if timezone:
        try:
            # If the timezone is valid, return it
            return pytz.timezone(timezone)
        except pytz.exceptions.UnknownTimeZoneError:
            pass

    if g.user:
        # Check if user is logged in and has a timezone set
        timezone = g.user.get('timezone')
        if timezone:
            try:
                # If the timezone is valid, return it
                return pytz.timezone(timezone)
            except pytz.exceptions.UnknownTimeZoneError:
                pass

    # Return the default timezone set in the app's configuration
    return app.config['BABEL_DEFAULT_TIMEZONE']


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
