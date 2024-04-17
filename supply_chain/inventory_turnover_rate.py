import pandas as pd
import json
# import numpy as np
# from datetime import datetime, timedelta

def inventory_turnover_metric(df, datetime_column, cost_column, inventory_value_column, period):
    """
    Inventory Turnover rate measures how quickly inventory is sold or used up within a specific time period. 
    It is calculated as the cost of goods sold divided by the average inventory value. 
    A higher inventory turnover indicates efficient inventory management.
    
    Calculate inventory turnover metric for day over day, week over week, or month over month periods.
    
    Parameters:
    - df: DataFrame containing columns DateTime, Cost_of_Goods_Sold, Inventory_Value.
    - period: String indicating the period for calculation: 'day', 'week', or 'month' (default is 'day').
    
    Returns:
    - JSON containing Date and corresponding inventory turnover metric.
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

    # Group by period and calculate inventory turnover
    inventory_turnover = df.groupby(pd.Grouper(key='Date', freq=freq)).apply(
        lambda x: x[cost_column].sum() / x[inventory_value_column].mean()
    ).reset_index().rename(columns={0: f'{column} Inventory_Turnover'})
    
    # Convert datetime column to string format
    inventory_turnover[datetime_column] = inventory_turnover[datetime_column].dt.strftime('%Y-%m-%d')
    
    # Convert DataFrame to JSON
    result_json = inventory_turnover.to_json(orient='records', indent=4)

     # Write JSON to file
    output_file= f'{column}_Inventory_Turnover.json'
    with open(output_file, 'w') as f:
        f.write(result_json)



# np.random.seed(0)
# dates = [datetime(2024, 1, 1) + timedelta(days=i) for i in range(40)]
# cost_of_goods_sold = np.random.randint(8000, 15000, size=40)
# average_inventory_value = np.random.randint(4000, 8000, size=40)


# data = {
#     'Date': [date.strftime('%Y-%m-%d') for date in dates],
#     'Cost_of_Goods': cost_of_goods_sold,
#     'Average_Inventory_Value': average_inventory_value
# }

# df = pd.DataFrame(data)

# inventory_turnover_metric(df=df, datetime_column='Date', cost_column='Cost_of_Goods', inventory_value_column='Average_Inventory_Value', period='week')
