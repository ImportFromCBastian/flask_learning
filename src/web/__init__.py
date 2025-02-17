from flask import Flask
from flask import render_template
from src.core import database
from src.core.config import config
from src.core import seeds
from src.core.model import issues


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
    def landing():
        issue = issues.list_issues()
        return render_template("index.html", issues=issue)

    @app.cli.command(name="reset-db")
    def reset():
        database.reset_db()

    @app.cli.command(name="seed-db")
    def seed():
        print("Seeding the database...🌱")
        seeds.grow()
        print("Database seeded.👍")

    return app
