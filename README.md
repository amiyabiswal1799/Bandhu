# AI Chatbot Application

A Python-based AI chatbot application built with Flask, SQLAlchemy, and integrated with AWS services (RDS MySQL and S3).

## Features

- **Flask Web Framework**: Lightweight and flexible web framework
- **Database Integration**: SQLAlchemy ORM with MySQL (AWS RDS) connection pooling
- **AWS S3 Integration**: File storage and retrieval capabilities
- **LLM Integration**: Ready for integration with LLM APIs (OpenAI, Anthropic, etc.)
- **Environment-based Configuration**: Secure configuration management using environment variables

## Project Structure

```
.
├── backend/              # Backend application logic
│   ├── __init__.py
│   └── routes.py        # API routes and endpoints
├── frontend/            # Frontend templates and static files
│   ├── templates/       # HTML templates
│   └── static/          # CSS, JS, and other static assets
│       ├── css/
│       └── js/
├── config/              # Configuration management
│   ├── __init__.py
│   ├── database.py      # Database connection configuration
│   └── s3.py           # AWS S3 configuration
├── models/              # Database models
│   └── __init__.py
├── utils/               # Utility functions
│   ├── __init__.py
│   └── helpers.py
├── tests/               # Test files
├── app.py              # Application entry point
├── requirements.txt    # Python dependencies
├── .env.example        # Environment variables template
└── README.md           # This file
```

## Prerequisites

- Python 3.8 or higher
- MySQL database (AWS RDS recommended)
- AWS account with S3 bucket
- Virtual environment tool (venv or virtualenv)

## Setup Instructions

### 1. Clone the Repository

```bash
git clone <repository-url>
cd <repository-name>
```

### 2. Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Copy the example environment file and configure it with your credentials:

```bash
cp .env.example .env
```

Edit `.env` and update the following variables:

- **Database Configuration**: Update with your RDS MySQL credentials
  - `DB_HOST`: Your RDS endpoint
  - `DB_NAME`: Database name
  - `DB_USER`: Database username
  - `DB_PASSWORD`: Database password

- **AWS Configuration**: Update with your AWS credentials
  - `AWS_ACCESS_KEY_ID`: Your AWS access key
  - `AWS_SECRET_ACCESS_KEY`: Your AWS secret key
  - `S3_BUCKET_NAME`: Your S3 bucket name

- **Application Configuration**:
  - `SECRET_KEY`: Generate a secure secret key
  - `LLM_API_KEY`: Your LLM provider API key

### 5. Initialize the Database

```bash
python -c "from config.database import init_db; init_db()"
```

### 6. Run the Application

```bash
# Development mode
python app.py

# Or using Flask CLI
export FLASK_APP=app.py
flask run
```

The application will be available at `http://localhost:5000`

## Configuration

### Database Connection Pool

The application uses SQLAlchemy connection pooling with the following default settings:

- **Pool Size**: 10 connections
- **Max Overflow**: 20 additional connections
- **Pool Timeout**: 30 seconds
- **Pool Recycle**: 3600 seconds (1 hour)

These can be adjusted in the `.env` file.

### AWS S3

S3 integration is pre-configured for file uploads and storage. The S3 client is initialized with your AWS credentials from the environment variables.

## Development

### Running Tests

```bash
pytest tests/
```

### Code Style

Follow PEP 8 guidelines for Python code style.

## API Endpoints

- `GET /` - Home page
- `GET /health` - Health check endpoint
- `POST /api/chat` - Chat endpoint (to be implemented)

## Deployment

For production deployment, consider:

1. Set `FLASK_ENV=production` in your `.env` file
2. Use a production WSGI server (gunicorn, uWSGI)
3. Set up proper logging
4. Configure SSL/TLS certificates
5. Set up monitoring and alerting

### Using Gunicorn

```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:8000 app:app
```

## Contributing

1. Create a feature branch
2. Make your changes
3. Write tests for new functionality
4. Submit a pull request

## License

[Add your license here]

## Support

For issues and questions, please open an issue in the repository.
