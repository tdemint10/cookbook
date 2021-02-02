from flask import Flask, jsonify
from flask_restx import Api
from flask_cors import CORS

import mongoengine

db = mongoengine


def create_app(env=None):
    from app.config import config_by_name
    from app.routes import register_routes

    app = Flask(__name__)
    CORS(app)
    app.config.from_object(config_by_name[env or "dev"])
    api = Api(app, title="Cookbook API", version="0.0.1")

    register_routes(api, app)

    mongoengine.connect(app.config["DB_NAME"], host='localhost', port=27017)

    @app.route("/health")
    def health():
        return jsonify("healthy")

    return app
