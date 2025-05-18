from app import create_app

# Expose the WSGI callable as 'app' for Gunicorn
app = create_app()
