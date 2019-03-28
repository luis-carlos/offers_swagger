import pandas as pd

df = pd.read_csv("sample.csv")
print(df)
new_df = df.drop_duplicates(['letter','number'],keep='last')
print(new_df)
