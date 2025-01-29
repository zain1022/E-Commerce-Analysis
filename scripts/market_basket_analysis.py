import pandas as pd
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules

# Load cleaned data
df = pd.read_csv('data/munch_cleaned_data.csv')

# Create a basket matrix
basket = df.groupby(['OrderID', 'ProductName'])['Quantity'].sum().unstack().reset_index().fillna(0)
basket.set_index('OrderID', inplace=True)
basket = basket.applymap(lambda x: 1 if x > 0 else 0)

# Apply the Apriori algorithm
frequent_itemsets = apriori(basket, min_support=0.1, use_colnames=True)
rules = association_rules(frequent_itemsets, metric='lift', min_threshold=1.0)

# Save results
rules.to_csv('data/market_basket_output.csv', index=False)
print("Market basket analysis results saved as 'market_basket_output.csv'")
