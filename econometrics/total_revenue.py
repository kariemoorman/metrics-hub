import pandas as pd
import random
import json

def calculate_total_revenue(df):
    """
    Calculate the total revenue based on the price and quantity in the DataFrame.

    Parameters:
        df (pandas.DataFrame): DataFrame containing 'Price' and 'Quantity' columns.

    Returns:
        JSON: JSON containing the total revenue for each row in the DataFrame.
    """
    # Calculate total revenue for each entry
    df['Total Revenue'] = df['Price'] * df['Quantity']

    # Save the DataFrame to a JSON file
    output_file = 'Total_Revenue.json'
    df.to_json(output_file, orient='records', indent=4)

    print(f"DataFrame with Total Revenue saved to '{output_file}.'")



# Generate random data for 50 entries and convert it into a JSON string
# data = []
# for _ in range(50):
#     product_id = random.randint(1000, 9999)
#     price = round(random.uniform(10.0, 100.0), 2)  
#     quantity = random.randint(1, 100) 
#     data.append({'Product_ID': product_id, 'Price': price, 'Quantity': quantity})

# Convert the data to a JSON string
# json_data = json.dumps(data)

# Load the JSON string into a Pandas DataFrame
# df = pd.read_json(json_data)

# calculate_total_revenue(df)
