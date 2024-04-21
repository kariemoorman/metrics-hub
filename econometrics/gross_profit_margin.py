import pandas as pd
import random
import json

def calculate_gross_profit_margin(df):
    """
    Gross margin is a profitability measure that looks at the percentage of a company's revenue 
    it retains after direct expenses, such as labor and materials, have been subtracted. 
    The higher the gross margin, the more revenue a company retains.
    
    Calculate the gross profit margin for each product in the DataFrame
    and save the results as a JSON file.

    Parameters:
        df (pandas.DataFrame): DataFrame containing columns for product_id, wholesale_price,
                               market_price, inventory, and units_sold.
        output_file (str): Path to the output JSON file.

    Returns:
        None
    """
    # Calculate cost of goods sold
    df['cost_of_goods_sold'] = df['wholesale_price'] * df['units_sold']

    # Calculate revenue
    df['revenue'] = df['market_price'] * df['units_sold']

    # Calculate gross profit margin
    df['gross_profit_margin'] = ((df['revenue'] - df['cost_of_goods_sold']) / df['revenue']) * 100

    # Write the DataFrame with the added column to a JSON file
    output_file = 'Gross_Profit_Margin.json'
    df.to_json(output_file, orient='records', indent=4)
    print(f"\nDataFrame with Gross Profit Margin saved to '{output_file}'\n")
    
    # Calculate total revenue and total cost of goods sold
    total_revenue = df['revenue'].sum()
    total_cost_of_goods_sold = df['cost_of_goods_sold'].sum()

    # Calculate total gross profit margin
    total_gross_profit_margin = ((total_revenue - total_cost_of_goods_sold) / total_revenue) * 100

    # Calculate and print total gross profit margin
    print(f"Total Gross Profit Margin: {total_gross_profit_margin}")

    return total_gross_profit_margin


# def generate_random_data(num_products):
#     """
#     Generate random data for the specified number of products.

#     Parameters:
#         num_products (int): Number of products to generate random data for.

#     Returns:
#         pandas.DataFrame: DataFrame containing random data for the specified number of products.
#     """
#     data = []
#     for i in range(num_products):
#         product_id = i + 1
#         wholesale_price = round(random.uniform(5.0, 20.0), 2)
#         market_price = round(random.uniform(wholesale_price + 2, wholesale_price + 30), 2)
#         inventory = random.randint(50, 200) 
#         units_sold = random.randint(0, inventory) 
#         data.append({'product_id': product_id, 'wholesale_price': wholesale_price,
#                      'market_price': market_price, 'inventory': inventory, 'units_sold': units_sold})

#     return pd.DataFrame(data)

# Generate random data
#df = generate_random_data(80)

# Example usage
#calculate_gross_profit_margin(df)
