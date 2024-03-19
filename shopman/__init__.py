from flask import Flask
from flask_sqlalchemy import SQLAchemy

db = SQLAchemy()

def create_app():
    app = Flask(__name__, instance_relative_config = False)
    app.config.from_mapping(
        SECRET_KEY = "Hamza_eService",
    )
    db.init_app(app)

    return app
