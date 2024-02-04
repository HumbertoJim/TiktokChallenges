# import libraries
import pandas as pd

# read dataset
df = pd.read_csv("./../datasets/cars.csv")

# top 10 cars with the best horsepower in usa
mask = df['origin'] == 'usa'
top_10 = df[mask].sort_values(
    by='horsepower', ascending=False
).head(10)

# select columns
top_10 = top_10[['name', 'origin', 'horsepower']]

print(top_10.head(10))
