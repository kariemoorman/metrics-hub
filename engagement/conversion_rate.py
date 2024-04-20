import pandas as pd
import random
import json

def calculate_conversion_rate(df):
    """
    Calculate the conversion rate for each feature in the DataFrame
    and save the results as a JSON file.

    Parameters:
        df (pandas.DataFrame): DataFrame containing columns for features,
                               'Conversions', and 'Visitors'.
        output_file (str): Path to the output JSON file.

    Returns:
        JSON: JSON containing Feature and Conversion Rate 
    """
    # Group the DataFrame by 'Feature' and calculate conversion rates
    conversion_rates = {}
    for feature, group in df.groupby('Feature'):
        conversions = group['Conversions']
        visitors = group['Visitors']
        conversion_rates[feature] = (conversions.sum() / visitors.sum()) * 100

    # Save the conversion rates to a JSON file
    output_file = 'Conversion_Rates.json'
    with open(output_file, 'w') as file:
        json.dump(conversion_rates, file, indent=4)

    print(f"Conversion rates saved to '{output_file}'")

# Example Usage
# data = []
# for i in range(5):
#     feature = i+1  
#     feature_data = []
#     for _ in range(50):
#         conversions = random.randint(0, 30) 
#         visitors = random.randint(50, 200)
#         feature_data.append({'Feature': feature, 'Conversions': conversions, 
#                              'Visitors': visitors})
#     data.extend(feature_data)

# df = pd.DataFrame(data)

# calculate_conversion_rate(df)
