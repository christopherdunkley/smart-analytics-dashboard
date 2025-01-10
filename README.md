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

# Install Tailwind css and its dependencies
npm install -D tailwindcss@3.3.3 postcss@8.4.27 autoprefixer@10.4.14

# Initialise Tailwind
npx tailwindcss init -p

# Create or edit .vscode/settings.json and add:
{
  "files.associations": {
    "*.css": "tailwindcss"
  }
}
```

### Loading Test Data
```bash
# Make sure the virtual environment is activated and navigate to the project root
.\venv\Scripts\activate

# create a Python shell
python

# Then, in this Python shell, run:
from backend.app.database import SessionLocal
from backend.app.test_data import add_test_data

db = SessionLocal()
add_test_data(db)
db.close()
exit()

# Alternatively, run the reset script:
python reset_db.py
```

This will populate the database with sample sales data that will appear in your dashboard visualisations.

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