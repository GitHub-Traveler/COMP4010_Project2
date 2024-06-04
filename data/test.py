import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv('df_surface_temp_longer.csv')

# Convert the 'year' column to string if it's not already
df['year'] = df['year'].astype(str)

# Create a dictionary to store the temperature of the year 1901 for each country
temperature_1901 = df[df['year'] == '1901'].set_index('ISO_A3')['temperature'].to_dict()

# Define a function to calculate temperature change
def calculate_temperature_change(row):
    if row['ISO_A3'] in temperature_1901:
        return round(row['temperature'] - temperature_1901[row['ISO_A3']], 2)
    else:
        return None

# Apply the function to each row in the DataFrame
df['temperature_change'] = df.apply(calculate_temperature_change, axis=1)

# Save the updated DataFrame back to a CSV file
df.to_csv('updated_file.csv', index=False)
