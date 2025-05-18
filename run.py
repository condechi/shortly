import os
from app import create_app


# Entry point for the application
def main():
    app = create_app()

    # Determine host, port, and debug settings
    host = os.environ.get("FLASK_RUN_HOST", "0.0.0.0")  # bind to all interfaces for Cloud Run
    port = int(os.environ.get("PORT", 8080))           # default to 8080 in container
    debug = os.environ.get("FLASK_DEBUG", "0").lower() in ("1", "true", "yes")

    print(f"Starting server on http://{host}:{port} (debug={debug})")
    app.run(host=host, port=port, debug=debug, use_reloader=False)

if __name__ == "__main__":
    main()