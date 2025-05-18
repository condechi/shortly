import os
from app import create_app

# WSGI app for Gunicorn & Cloud Run
app = create_app()

# Entry point for local execution (optional)
def main():
    host = os.environ.get("FLASK_RUN_HOST", "0.0.0.0")
    port = int(os.environ.get("PORT", 8080))
    debug = os.environ.get("FLASK_DEBUG", "0").lower() in ("1", "true", "yes")

    print(f"Starting server on http://{host}:{port} (debug={debug})")
    app.run(host=host, port=port, debug=debug, use_reloader=False)

if __name__ == "__main__":
    main()