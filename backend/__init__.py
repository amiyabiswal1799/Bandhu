from flask import Flask
from flask_cors import CORS
from config import get_config
from config.database import close_db


def create_app(config_name=None):
    app = Flask(__name__, 
                template_folder='../frontend/templates',
                static_folder='../frontend/static')
    
    config = get_config(config_name)
    app.config.from_object(config)
    
    CORS(app)
    
    from backend.routes import main_bp
    app.register_blueprint(main_bp)
    
    @app.teardown_appcontext
    def shutdown_session(exception=None):
        close_db()
    
    return app
