import os
from flask import Flask

def create_app():
    app = Flask(__name__)
    
    # Secret key configuration
    app.secret_key = os.environ.get('SECRET_KEY', '5791628bb0b13ce0c676dfde280ba245')
    
    # Import and register blueprints/routes
    from app.routes import main_bp
    app.register_blueprint(main_bp)
    
    # Register error handlers
    from flask import render_template
    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('404.html'), 404
        
    return app
