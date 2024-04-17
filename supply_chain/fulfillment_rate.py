
import pandas as pd
import json
# import numpy as np
# from datetime import datetime, timedelta

def fulfillment_rate(df, datetime_column, total_orders_column, fulfilled_orders_column, period):
    """
    Fulfillment rate measures the percentage of customer orders that are fulfilled completely from available stock. 
    It helps assess how well a company meets customer demand and satisfaction.
    Calculate the fill rate as the percentage of customer orders that are fulfilled completely from available stock.

    Parameters:
    - df: DataFrame containing columns for total orders and fulfilled orders.
    - datetime_column: Name of column containing datetime.
    - total_orders_column: Name of the column containing total orders.
    - fulfilled_orders_column: Name of the column containing fulfilled orders.

    Returns:
    - Float representing the fill rate as a percentage.
    """
    
    # Convert 'Date' column to datetime
    df['Date'] = pd.to_datetime(df[datetime_column])
    
    # Resample DataFrame based on the period
    if period == 'day':
        freq = 'D'
        column = 'Daily'
    elif period == 'week':
        freq = 'W-MON'
        column = 'Weekly'
    elif period == 'month':
        freq = 'M'
        column = 'Monthly'
    else:
        raise ValueError("Invalid period. Choose 'day', 'week', or 'month'.")

    # Group by period and calculate fill rate
    fill_rate_data = df.groupby(pd.Grouper(key='Date', freq=freq)).apply(
        lambda x: (x[fulfilled_orders_column].sum() / x[total_orders_column].sum()) * 100 if x[total_orders_column].sum() != 0 else 0
    ).reset_index().rename(columns={0: f'{column}_Fill_Rate'})
    
    # Convert datetime column to string format
    fill_rate_data[datetime_column] = fill_rate_data[datetime_column].dt.strftime('%Y-%m-%d')
    
    # Convert DataFrame to JSON
    result_json = fill_rate_data.to_json(orient='records', indent=4)

     # Write JSON to file
    output_file= f'{column}_Fulfillment_Rate.json'
    with open(output_file, 'w') as f:
        f.write(result_json)


# np.random.seed(0)
# size = 40
# dates = [datetime(2024, 1, 1) + timedelta(days=i) for i in range(size)]
# total_orders = np.random.randint(80, 220, size=size)
# fulfilled_orders = np.random.randint(70, total_orders + 1, size=size)

    
# # Example dataset
# data = {
#     'Date': dates,
#     'Total_Orders': total_orders,
#     'Fulfilled_Orders': fulfilled_orders
# }

# # Convert data to DataFrame
# df = pd.DataFrame(data)

# fulfillment_rate(df=df, datetime_column='Date', total_orders_column='Total_Orders', fulfilled_orders_column='Fulfilled_Orders', period='week')
