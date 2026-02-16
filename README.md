# Shortly 🔗

A lightweight URL shortener web application built with Flask and SQLAlchemy. Shortly provides a simple interface to create short links, track click statistics, and manage your shortened URLs.

## 📋 Overview

Shortly is a ChatGPT-driven application development process demonstrating a fully functional URL shortening service. The application generates unique 6-character codes for long URLs, tracks usage statistics, and provides an intuitive web interface for link management.

## ✨ Features

- **URL Shortening**: Convert long URLs into short, shareable links with unique 6-character codes
- **Click Tracking**: Monitor how many times each shortened link has been accessed
- **Statistics Dashboard**: View detailed stats including creation date, click count, and last accessed time
- **Recent Links**: Display the 5 most recently created links on the homepage
- **Responsive UI**: Bootstrap-based interface that works across devices
- **Cloud-Ready**: Includes Docker and Google Cloud Run deployment configuration

## 🏗️ Architecture

### Project Structure

```
shortly/
├── app/
│   ├── __init__.py           # Flask application factory
│   ├── models.py             # SQLAlchemy ORM models
│   ├── routes.py             # Flask routes and view functions
│   └── templates/            # Jinja2 HTML templates
│       ├── base.html         # Base template with Bootstrap
│       ├── home.html         # Homepage with form and recent links
│       ├── stats.html        # Statistics page for individual links
│       └── 404.html          # Custom 404 error page
├── run.py                    # Application entry point
├── wsgi.py                   # WSGI entry point for Gunicorn
├── crash_course.py           # Database model demonstration script
├── requirements.txt          # Python dependencies
├── Dockerfile                # Container image configuration
├── cloudbuild.yaml           # Google Cloud Build configuration
└── shortly.db                # SQLite database (local development)
```

### Technology Stack

- **Backend**: Python 3.10+, Flask 2.0+
- **Database**: SQLAlchemy 1.4+ (SQLite for local, PostgreSQL for production)
- **Web Server**: Gunicorn 20.1+
- **Frontend**: Bootstrap 5.3, Jinja2 templates
- **Deployment**: Docker, Google Cloud Run, Cloud SQL

## 🚀 Getting Started

### Prerequisites

- Python 3.10 or higher
- pip (Python package manager)
- Git

### Local Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/condechi/shortly.git
   cd shortly
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python run.py
   ```

5. **Access the application**
   
   Open your browser and navigate to `http://localhost:8080`

### Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `PORT` | Port for the web server | `8080` |
| `FLASK_DEBUG` | Enable Flask debug mode | `0` (disabled) |
| `DATABASE_URL` | Database connection string | `sqlite:///shortly.db` |
| `FLASK_RUN_HOST` | Host address to bind | `0.0.0.0` |

## 🐳 Docker Deployment

### Build the Docker image

```bash
docker build -t shortly .
```

### Run the container

```bash
docker run -p 8080:8080 -e PORT=8080 shortly
```

The application will be available at `http://localhost:8080`

## ☁️ Google Cloud Run Deployment

This project includes a `cloudbuild.yaml` configuration for automated deployment to Google Cloud Run.

### Prerequisites

- Google Cloud Project with billing enabled
- Cloud Run API enabled
- Cloud SQL instance configured (optional, for PostgreSQL)
- Cloud Build API enabled

### Deploy using Cloud Build

```bash
gcloud builds submit --config cloudbuild.yaml
```

The build process will:
1. Build the Docker image
2. Push it to Google Container Registry
3. Deploy to Cloud Run with automatic environment configuration
4. Connect to Cloud SQL PostgreSQL instance (if configured)

## 📊 Database Models

### Link Model

```python
class Link:
    id              # Integer, primary key
    original_url    # String, the full URL to shorten
    code            # String(6), unique short code
    created_at      # DateTime, creation timestamp
    click_count     # Integer, number of clicks
    last_accessed   # DateTime, last visit timestamp
```

### Crash Course Script

Run `crash_course.py` to see a demonstration of the ORM models in action:

```bash
python crash_course.py
```

This script demonstrates:
- Creating tables
- Inserting a new link
- Querying links
- Updating click statistics

## 🛣️ API Routes

| Route | Method | Description |
|-------|--------|-------------|
| `/` | GET | Homepage with URL form and recent links |
| `/create` | POST | Create a new shortened URL |
| `/<code>` | GET | Redirect to original URL (tracks clicks) |
| `/stats/<code>` | GET | View statistics for a short code |

## 🔧 Development

### Running Tests

Currently, the project does not include automated tests. To test functionality:

1. Start the application locally
2. Create a short link through the web interface
3. Access the shortened URL to test redirects
4. View the `/stats/<code>` page to verify click tracking

### Code Quality

The codebase follows standard Python conventions:
- PEP 8 style guidelines
- Docstrings for modules and functions
- Modular architecture with separation of concerns

## 📝 Configuration

### Database Configuration

**Local Development (SQLite)**
```python
DATABASE_URL = 'sqlite:///shortly.db'
```

**Production (PostgreSQL)**
```python
DATABASE_URL = 'postgresql+psycopg2://user:password@host:port/dbname'
```

### Short Code Generation

Links are generated with 6-character alphanumeric codes (a-Z, 0-9). This provides:
- 62^6 = 56.8 billion possible combinations
- Collision-resistant for most use cases

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is part of a ChatGPT-driven app development process demonstration.

## 🐛 Known Issues

- No collision checking for generated short codes (relies on database unique constraint)
- No link expiration feature
- No authentication/authorization system
- Click tracking doesn't prevent duplicate counting from same user

## 🔮 Future Enhancements

- [ ] Custom short code support
- [ ] Link expiration dates
- [ ] User authentication
- [ ] QR code generation
- [ ] Analytics dashboard
- [ ] API endpoints for programmatic access
- [ ] Rate limiting
- [ ] Link validation and preview

## 📞 Support

For issues, questions, or contributions, please open an issue in the GitHub repository.

---

**Built with ❤️ using Flask and ChatGPT**