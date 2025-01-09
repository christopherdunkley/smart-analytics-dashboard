from sqlalchemy import Boolean, Column, Integer, String, Float, DateTime, text
from sqlalchemy.sql import func
from backend.app.database import Base    # Changed from relative import

class SalesData(Base):
    __tablename__ = "sales_data"

    id = Column(Integer, primary_key=True, index=True)
    product_name = Column(String, index=True)
    quantity = Column(Integer)
    unit_price = Column(Float)
    # Change the computed column to use explicit SQL expression
    total_amount = Column(Float, server_default=text('0.0'))
    timestamp = Column(DateTime(timezone=True), server_default=func.now())
    region = Column(String)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Calculate total_amount when instance is created
        if 'quantity' in kwargs and 'unit_price' in kwargs:
            self.total_amount = float(kwargs['quantity'] * kwargs['unit_price'])