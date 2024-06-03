import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv('COMP4010_Project2\data\surfaces_temp.csv')
df_precipitation = pd.read_csv('COMP4010_Project2\data\precipitation.csv')


# Iterate through each row starting from the third row
for index, row in df.iterrows():
    # Get the value at the reference column (C2 in this case)
    base_value = row['1901-07']
    
    # Iterate through each column starting from D
    for col in df.columns[3:]:
        # Divide the value in each cell by the base value
        df.at[index, col] = row[col] - base_value
        
for index, row in df_precipitation.iterrows():
    # Get the value at the reference column (C2 in this case)
    base_value = row['1901-07']
    
    # Iterate through each column starting from D
    for col in df.columns[3:]:
        # Divide the value in each cell by the base value
        df_precipitation.at[index, col] = row[col] - base_value


df.to_csv('temp_change.csv', index=False)
df.to_csv('precipitation_change.csv', index=False)
