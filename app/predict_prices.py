import pandas as pd

# Load the dataset
df = pd.read_csv('book1.csv')

# Assuming 'ram' and 'rom' are the column names in your dataset
X = df[['ram', 'rom']]
y = df['price']