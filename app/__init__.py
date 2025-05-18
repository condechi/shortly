import os
from flask import Flask, render_template

def create_app(config_object=None):
    """
    Application factory: create and configure the Flask app, register blueprints and error handlers.
    """
    app = Flask(__name__, template_folder='templates')
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE_URL=os.environ.get('DATABASE_URL', 'sqlite:///shortly.db')
    )

    # Register main blueprint
    from app.routes import main_bp
    app.register_blueprint(main_bp)

    # Custom 404 error handler
    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('404.html'), 404

    return app