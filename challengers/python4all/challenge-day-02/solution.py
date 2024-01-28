# import libraries
import pandas as pd

# read dataset
people = pd.read_csv('datasets/people.csv')

# select the first 4 columns
first_4_cols = people.columns[:4]

# prints
print(f'\nAnswer: {list(first_4_cols)}\n')
print(people[first_4_cols].head())
