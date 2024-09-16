from flask import Flask
from src.core import database
from src.core.config import config


def create_app(env="development", static_folder="static"):
    """
    Creates the Flask app.
    :param env: The environment to run the app in.
    :param static_folder: The folder to serve static files from.
    :return: The Flask app.
    """

    app = Flask(__name__)

    # This handles the environment configuration.
    app.config.from_object(config[env])

    # The database is initialized with the app.
    database.init_app(app)

    @app.route("/")
    def hello_world():
        return "Hello, World!"

    @app.cli.command(name="reset-db")
    def reset():
        database.reset_db()

    return app
