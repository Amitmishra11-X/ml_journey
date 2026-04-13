import pandas as pd
df = pd.read_csv(r"D:\Download1\india_colleges.csv")
print(df.shape)
print(df.head())
print(df.columns)
print(df['placement_avg_lpa'].max())
print(df['placement_avg_lpa'].min())


good_colleges = df[df['rating'] > 4.0]
print(good_colleges[['name', 'rating']])

# high rating + good placement
best = df[(df['rating'] > 4) & (df['placement_avg_lpa'] > 8)]

print(best[['name', 'rating', 'placement_avg_lpa']])

print(df['rating'].dtype)
print(df['rating'].mean())
print(df['name'][2])