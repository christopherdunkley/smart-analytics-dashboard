from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from . import models, schemas
from .database import SessionLocal, engine
from .analytics import SalesAnalytics

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Smart Business Analytics Dashboard")

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/sales/", response_model=schemas.Sales)
def create_sale(sale: schemas.SalesCreate, db: Session = Depends(get_db)):
    # We don't need to calculate total_amount manually anymore
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