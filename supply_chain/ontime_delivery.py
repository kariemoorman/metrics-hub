import pandas as pd
import json
import random
from datetime import datetime, timedelta


def calculate_on_time_delivery(orders_df):
    """
    On-time Delivery tracks the percentage of orders delivered to customers on or before the promised delivery date. 
    On-time delivery is crucial for maintaining customer satisfaction and loyalty, and is a reflection optimal fleet organization.
    
    Calculate the percentage of orders delivered on or before the promised delivery date.

    Parameters:
    - orders_df: DataFrame containing order information including order number, customer_id, cost,
                 order_date, ship_date, estimated_delivery_date, and actual_delivery_date.

    Returns:
    - Percentage of on-time delivery.
    """
    # Convert date columns to datetime
    orders_df['estimated_delivery_date'] = pd.to_datetime(orders_df['estimated_delivery_date'])
    orders_df['actual_delivery_date'] = pd.to_datetime(orders_df['actual_delivery_date'])

    # Calculate on-time deliveries
    orders_df['on_time_delivery'] = (orders_df['actual_delivery_date'] <= orders_df['estimated_delivery_date']).astype(int)


    # Calculate on-time deliveries
    on_time_orders = orders_df[orders_df['actual_delivery_date'] <= orders_df['estimated_delivery_date']]


    # Write DataFrame to JSON file
    orders_df['estimated_delivery_date'] = orders_df['estimated_delivery_date'].dt.strftime('%Y-%m-%d')
    orders_df['actual_delivery_date'] = orders_df['actual_delivery_date'].dt.strftime('%Y-%m-%d')
    output_file = 'Ontime_Delivery.json'
    orders_df.to_json(output_file, orient='records', indent=4)
    
    # Calculate percentage of on-time deliveries
    total_orders = len(orders_df)
    on_time_orders_count = len(on_time_orders)
    if total_orders == 0:
        return 0
    else:
        on_time_delivery_percentage = (on_time_orders_count / total_orders) * 100
        return on_time_delivery_percentage


# Example data
orders_data = []
size = 50
for i in range(size):
    order_number = i + 1
    customer_id = f"C{i + 1:03d}"
    cost = random.randint(20, 200)
    order_date = datetime(2024, random.randint(1, 12), random.randint(1, 28)).strftime('%Y-%m-%d')
    ship_date = (datetime.strptime(order_date, '%Y-%m-%d') + timedelta(days=random.randint(0, 5))).strftime('%Y-%m-%d')
    estimated_delivery_date = (datetime.strptime(ship_date, '%Y-%m-%d') + timedelta(days=random.randint(1, 8))).strftime('%Y-%m-%d')
    actual_delivery_date = (datetime.strptime(ship_date, '%Y-%m-%d') + timedelta(days=random.randint(0, 11))).strftime('%Y-%m-%d')
    
    warehouse_location = f"W{random.randint(1, 5):03d}"
    delivery_location = f"D{random.randint(1, 10):03d}"
    estimated_mileage = random.randint(50, 300)
    order_data = {
        "order_number": order_number,
        "customer_id": customer_id,
        "cost": cost,
        "order_date": order_date,
        "ship_date": ship_date,
        "estimated_delivery_date": estimated_delivery_date,
        "actual_delivery_date": actual_delivery_date,
        "warehouse_location": warehouse_location,
        "delivery_location": delivery_location,
        "estimated_mileage": estimated_mileage
    }
    orders_data.append(order_data)

orders_df = pd.DataFrame(orders_data)

on_time_delivery_percentage = calculate_on_time_delivery(orders_df)
print("On-time delivery percentage:", on_time_delivery_percentage)
