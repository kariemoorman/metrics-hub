import pandas as pd
import json 
# from datetime import datetime, timedelta
# import numpy as np

def supplier_lead_time(df, order_date_column, delivery_date_column):
    """
    Supplier lead time measures the time it takes for suppliers to deliver goods after receiving an order. 
    It helps assess supplier performance and the reliability of the supply chain.
    
    Calculate the supplier lead time as the difference between delivery date and order date.

    Parameters:
    - df: DataFrame containing columns for order date and delivery date.
    - order_date_column: Name of the column containing order dates.
    - delivery_date_column: Name of the column containing delivery dates.

    Returns:
    - JSON containing supplier lead time in days.
    """
    # Convert date columns to datetime
    df[order_date_column] = pd.to_datetime(df[order_date_column])
    df[delivery_date_column] = pd.to_datetime(df[delivery_date_column])
    
    # Calculate lead time
    df['Lead_Time(days)'] = (df[delivery_date_column] - df[order_date_column]).dt.days
    df[order_date_column] = df[order_date_column].dt.strftime('%Y-%m-%d')
    df[delivery_date_column] = df[delivery_date_column].dt.strftime('%Y-%m-%d')
    
    # Sort DataFrame by delivery date
    df.sort_values(by=[order_date_column, 'Lead_Time(days)'], inplace=True)
    
    # Convert DataFrame to JSON
    result_json = df.to_json(orient='records', indent=4)

    # Write JSON to file
    output_file= f'Supplier_Lead_Time.json'
    with open(output_file, 'w') as f:
        f.write(result_json)


# Generate example data
# np.random.seed(0)

# Generate random order dates
# start_date = datetime(2024, 1, 1)
# end_date = datetime(2024, 1, 31)
# order_dates = [start_date + timedelta(days=np.random.randint((end_date - start_date).days)) for _ in range(100)]

# Generate random delivery dates (assuming delivery happens 1 to 7 days after order)
# delivery_dates = [order_date + timedelta(days=np.random.randint(1, 8)) for order_date in order_dates]

# Create DataFrame
# data = {
#     'Order_Date': order_dates,
#     'Delivery_Date': delivery_dates
# }

# df = pd.DataFrame(data)

# supplier_lead_time(df=df, order_date_column='Order_Date', delivery_date_column='Delivery_Date')
