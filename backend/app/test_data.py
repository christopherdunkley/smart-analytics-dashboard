from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from . import models

def add_test_data(db: Session):
    """Add sample sales data"""
    products = ["Laptop", "Mouse", "Keyboard", "Monitor"]
    regions = ["North", "South", "East", "West"]
    
    # create sales over last 30 days
    for i in range(30):
        for product in products:
            sale = models.SalesData(
                product_name=product,
                quantity=5 + (i % 5),  # varying quantities
                unit_price=100 if product == "Laptop" else 20,
                region=regions[i % len(regions)],
                timestamp=datetime.now() - timedelta(days=i)
            )
            db.add(sale)
    
    db.commit()