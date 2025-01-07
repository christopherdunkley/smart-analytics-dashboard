from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class SalesBase(BaseModel):
    product_name: str
    quantity: int
    unit_price: float
    region: str
    total_amount: Optional[float] = None

class SalesCreate(SalesBase):
    pass

class Sales(SalesBase):
    id: int
    timestamp: datetime

    class Config:
        from_attributes = True