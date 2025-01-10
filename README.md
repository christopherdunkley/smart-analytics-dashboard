# Smart Analytics Dashboard

A full-stack business analytics dashboard built with Python FastAPI and React. This project demonstrates modern software development practices and data analytics capabilities.

## Features
- REST API built with FastAPI
- SQLAlchemy ORM for database management
- Data analytics and visualisation
- Authentication and authorisation
- Comprehensive test suite
- React frontend with interactive charts

## Tech Stack
- Backend: Python, FastAPI, SQLAlchemy, Pandas
- Frontend: React, Recharts, Tailwind CSS
- Database: SQLite (development)
- Testing: pytest

## Getting Started

### Prerequisites
- Python 3.11 or later
- Node.js 18 or later
- Visual Studio Code (recommended)

### VSCode Extensions
- Python (Microsoft)
- Pylance
- Tailwind CSS IntelliSense
- ESLint
- Prettier

### Backend Setup
```bash
# Create and activate virtual environment
python -m venv venv
.\venv\Scripts\activate

# Install dependencies manually (recommended)
pip install fastapi
pip install uvicorn
pip install sqlalchemy
pip install pandas
pip install pytest
pip install python-dotenv
pip install httpx

# Start the backend server
python -m uvicorn backend.app.main:app --reload
```

### Frontend Setup
```bash
# Navigate to frontend directory
cd frontend

# Install dependencies
npm install

# Start the development server
npm run dev
```

## Development

The application will be available at:
- Backend API: http://localhost:8000/docs
- Frontend: http://localhost:5173

## Project Structure
```
smart-analytics-dashboard/
├── backend/              # FastAPI backend
│   ├── app/
│   │   ├── main.py
│   │   ├── models.py
│   │   └── ...
│   └── tests/
└── frontend/            # React frontend
    ├── src/
    │   ├── components/
    │   └── ...
    └── ...
```

## Contributing
This project is for demonstration purposes.

## License
MIT