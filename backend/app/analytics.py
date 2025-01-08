from typing import List, Dict
import pandas as pd
from sqlalchemy.orm import Session
from . import models
from fastapi import HTTPException

class SalesAnalytics:
    def __init__(self, db: Session):
        self.db = db

    def _get_sales_dataframe(self) -> pd.DataFrame:
        """Convert sales data from database to pandas DataFrame"""
        sales = self.db.query(models.SalesData).all()
        if not sales:
            raise HTTPException(status_code=404, detail="No sales data found")
        
        sales_dicts = []
        for sale in sales:
            sale_dict = {
                'id': sale.id,
                'product_name': sale.product_name,
                'quantity': sale.quantity,
                'unit_price': sale.unit_price,
                'total_amount': sale.total_amount,
                'timestamp': sale.timestamp,
                'region': sale.region
            }
            sales_dicts.append(sale_dict)
        
        return pd.DataFrame(sales_dicts)

    def get_summary_stats(self) -> Dict:
        """Calculate summary statistics for sales data"""
        df = self._get_sales_dataframe()
        
        summary = {
            'total_revenue': float(df['total_amount'].sum()),
            'average_order_value': float(df['total_amount'].mean()),
            'total_orders': len(df),
            'total_units_sold': int(df['quantity'].sum()),
            'top_products': df.groupby('product_name')['quantity']\
                .sum()\
                .nlargest(5)\
                .to_dict(),
            'revenue_by_region': df.groupby('region')['total_amount']\
                .sum()\
                .to_dict()
        }
        
        return summary

    def get_time_series_analysis(self) -> Dict:
        """Analyze sales trends over time"""
        df = self._get_sales_dataframe()
        df['date'] = df['timestamp'].dt.date
        
        daily_sales = df.groupby('date').agg({
            'total_amount': ['sum', 'count']
        }).reset_index()

        daily_sales.columns = ['date', 'revenue', 'orders']
        
        return {
            'daily_revenue': [
                {
                    'date': str(row['date']),
                    'revenue': float(row['revenue']),
                    'orders': int(row['orders'])
                }
                for _, row in daily_sales.iterrows()
            ]
        }