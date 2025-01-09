from typing import List, Dict
import pandas as pd
import numpy as np
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

    def _safe_float(self, value) -> float:
        """Convert value to float, replacing NaN with 0"""
        if pd.isna(value) or np.isnan(value):
            return 0.0
        return float(value)

    def get_summary_stats(self) -> Dict:
        """Calculate summary statistics for sales data"""
        df = self._get_sales_dataframe()
        
        # calculate top products - handle NaN values
        top_products = df.groupby('product_name')['quantity'].sum()
        top_products = top_products.fillna(0)
        top_products_dict = {
            k: int(v) for k, v in top_products.nlargest(5).items()
        }

        # calculate revenue by region - handle NaN values
        revenue_by_region = df.groupby('region')['total_amount'].sum()
        revenue_by_region = revenue_by_region.fillna(0)
        revenue_by_region_dict = {
            k: self._safe_float(v) for k, v in revenue_by_region.items()
        }
        
        summary = {
            'total_revenue': self._safe_float(df['total_amount'].sum()),
            'average_order_value': self._safe_float(df['total_amount'].mean()),
            'total_orders': len(df),
            'total_units_sold': int(df['quantity'].sum()),
            'top_products': top_products_dict,
            'revenue_by_region': revenue_by_region_dict
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
        
        # handle NaN values within the results
        return {
            'daily_revenue': [
                {
                    'date': str(row['date']),
                    'revenue': self._safe_float(row['revenue']),
                    'orders': int(row['orders'])
                }
                for _, row in daily_sales.iterrows()
            ]
        }