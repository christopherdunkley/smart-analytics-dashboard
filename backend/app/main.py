from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import List
from . import models, schemas
from .database import SessionLocal, engine
from .analytics import SalesAnalytics

app = FastAPI(title="Smart Business Analytics Dashboard")

# add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # in prod, this would be replaced with a frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/sales/", response_model=schemas.Sales)
def create_sale(sale: schemas.SalesCreate, db: Session = Depends(get_db)):
    db_sale = models.SalesData(**sale.model_dump())
    db.add(db_sale)
    db.commit()
    db.refresh(db_sale)
    return db_sale

@app.get("/sales/", response_model=List[schemas.Sales])
def read_sales(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    sales = db.query(models.SalesData).offset(skip).limit(limit).all()
    return sales

@app.get("/analytics/summary")
def get_sales_summary(db: Session = Depends(get_db)):
    """Get summary statistics for all sales"""
    analytics = SalesAnalytics(db)
    return analytics.get_summary_stats()

@app.get("/analytics/trends")
def get_sales_trends(db: Session = Depends(get_db)):
    """Get time series analysis of sales trends"""
    analytics = SalesAnalytics(db)
    return analytics.get_time_series_analysis()