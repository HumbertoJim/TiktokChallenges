# import libraries
import pandas as pd

# read the dataset
df = pd.read_csv('./../datasets/people.csv')

# calculate the sex counts by job
sex_by_job = df.groupby('Job Title')['Sex'].value_counts()
sex_by_job = sex_by_job.reset_index()

# create a table with the first 10 rows ordered by people counts
frst10 = sex_by_job.head(10).sort_values('count', ascending=False)

print(frst10, '\n')

# what is the job with the most women?
mask = sex_by_job['Sex'] == "Female"
answer = sex_by_job[mask].sort_values('count').tail(1)

print(answer)
