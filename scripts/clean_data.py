import pandas as pd

# Load the data
df = pd.read_csv('data/munch_raw_data.csv')

# Data cleaning: remove duplicates, fill missing values, etc.
df.drop_duplicates(inplace=True)
df['OrderDate'] = pd.to_datetime(df['OrderDate'])

# Save cleaned data
df.to_csv('data/munch_cleaned_data.csv', index=False)
print("Data cleaned and saved as 'munch_cleaned_data.csv'")
