# README.md
# Smart Analytics Dashboard

A full-stack business analytics dashboard built with Python FastAPI and React. This project demonstrates modern software development practices and data analytics capabilities.

## Features
- REST API built with FastAPI
- SQLAlchemy ORM for database management
- Data analytics and visualization
- Authentication and authorization
- Comprehensive test suite
- React frontend with interactive charts

## Tech Stack
- Backend: Python, FastAPI, SQLAlchemy
- Frontend: React, Chart.js
- Database: SQLite (development), PostgreSQL (production)
- Testing: pytest
- Documentation: Swagger/OpenAPI

## Getting Started
1. Clone the repository
2. Install dependencies: `pip install -r backend/requirements.txt`
3. Run the server: `uvicorn app.main:app --reload`
4. Visit `http://localhost:8000/docs` for API documentation

## Project Structure
```
smart_analytics/
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── models.py
│   │   └── ...
│   └── tests/
└── frontend/
```

## Contributing
This project is for demonstration purposes.

## License
MIT