from sqlalchemy import Boolean, Column, Integer, String, Float, DateTime, Computed
from sqlalchemy.sql import func
from .database import Base

class SalesData(Base):
    __tablename__ = "sales_data"

    id = Column(Integer, primary_key=True, index=True)
    product_name = Column(String, index=True)
    quantity = Column(Integer)
    unit_price = Column(Float)
    total_amount = Column(Float, Computed("quantity * unit_price"))
    timestamp = Column(DateTime(timezone=True), server_default=func.now())
    region = Column(String)