import pandas as pd

data = pd.read_csv('output/dataset.csv')
data = data.groupby('sex')['age'].count()

data.to_csv('output/final_data.csv')
print(data)
