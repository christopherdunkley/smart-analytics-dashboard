# Smart Analytics Dashboard Backend

FastAPI backend for the Smart Analytics Dashboard, providing REST API endpoints for business analytics data.

## Features
- REST API endpoints for sales data
- Data analytics processing with pandas
- SQLAlchemy ORM for database management
- Automatic API documentation with Swagger UI

## Setup
```bash
# Create and activate the virtual environment
python -m venv venv
.\venv\Scripts\activate

# Install dependencies
pip install fastapi
pip install uvicorn
pip install sqlalchemy
pip install pandas
pip install pytest
pip install python-dotenv
pip install httpx

# Start the server
python -m uvicorn app.main:app --reload
```

## API Documentation
Once server is running, visit http://localhost:8000/docs for interactive API documentation.

## Project Structure
```
backend/
├── app/
│   ├── __init__.py
│   ├── main.py          # Main application file
│   ├── models.py        # SQLAlchemy models
│   ├── schemas.py       # Pydantic schemas
│   ├── database.py      # Database configuration
│   └── analytics.py     # Analytics logic
└── tests/               # Test files
```

## Testing
```bash
pytest tests/
```