import os
from flask import Flask
from dotenv import load_dotenv

def create_app():
    load_dotenv()

    UPLOAD_FOLDER = os.path.expanduser(os.getenv("UPLOAD_FOLDER", "~/RemotelifyContent"))
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)

    app = Flask(__name__)
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    app.secret_key = os.getenv("SECRET_KEY", "changeme")

    from .routes import register_routes
    register_routes(app)

    return app
