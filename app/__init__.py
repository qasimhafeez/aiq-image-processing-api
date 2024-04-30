import os
from flask import Flask, jsonify
from flask_cors import CORS
from .config.config import Config
from .models.image import Image, db
from dotenv import load_dotenv
from .routes.api import api as api_blueprint

# Load environment variables
dotenv_path = os.path.join(os.path.dirname(__file__), '..', '.env')
load_dotenv(dotenv_path)



def create_app():
    app = Flask(__name__)
    CORS(app)
    app.config.from_object(Config)
    db.init_app(app)

    with app.app_context():
        # Create database tables if they don't exist
        db.create_all()

        # avoid duplication of data but if we are using different files, we should come up with better approach
        # Using a script to load data is also a good approach, that way we can remove this block of code from create_app()
        if not Image.query.first():
            from .services.image_processing import read_and_process_csv
            csv_file_path = os.getenv('CSV_FILE_PATH')
            read_and_process_csv(csv_file_path)

    # Register the API blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api')

    # 404 error handling
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "status": 404,
            "error": "Not Found",
            "message": "The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again."
        }), 404

    return app

