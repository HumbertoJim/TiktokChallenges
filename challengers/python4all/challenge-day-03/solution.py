# import libraries
import pandas as pd

# read the data
df = pd.read_csv('./../datasets/people.csv')

# calculate the sex counts
print(df['Sex'].value_counts())
