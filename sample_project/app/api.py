from flask import Flask, jsonify, send_from_directory
from flask_restx import Api
from flask_cors import CORS
from app.config import config_by_name
from app.controllers import add_resources
from .exts import db


def create_app(env=None):

    app = Flask(__name__, static_folder='uploads')

    CORS(app)
    
    app.config.from_object(config_by_name[env or 'dev'])
    
    api = Api(app, title="Auto-conspects API", version="0.1.0")

    add_resources(api)

    db.init_app(app)

    @app.route('/uploads/<path:filename>')
    def serve_page(filename):
        return send_from_directory('uploads', filename)

    return app
