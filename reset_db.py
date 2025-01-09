from backend.app.database import SessionLocal, engine
from backend.app.database import Base
from backend.app.models import SalesData
from datetime import datetime, timedelta
import random

def reset_database():
    # drop and recreate all tables
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    
    # create test data
    db = SessionLocal()
    try:
        products = {
            "Laptop": 1200.0,
            "Mouse": 25.0,
            "Keyboard": 50.0,
            "Monitor": 300.0
        }
        regions = ["North", "South", "East", "West"]
        
        # create sales over last 30 days
        for i in range(30):
            for product_name, unit_price in products.items():
                quantity = random.randint(1, 10)
                sale = SalesData(
                    product_name=product_name,
                    quantity=quantity,
                    unit_price=unit_price,
                    region=regions[i % len(regions)],
                    timestamp=datetime.now() - timedelta(days=i)
                )
                db.add(sale)
        
        db.commit()
        print("Database reset and populated with test data successfully!")
    
    finally:
        db.close()

if __name__ == "__main__":
    reset_database()