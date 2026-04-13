import pandas as pd 
df = pd.read_csv(r"D:\Download1\india_colleges.csv")
##how to select, assign, indexing happen

punjab_colleges = df[df['state']=='Punjab']
print(punjab_colleges)


#filter for search
top_colleges = df[
    (df['rating'] >= 8.0) & 
    ((df['state'] == 'Uttar Pradesh') | (df['state'] == 'Delhi'))
]

print(top_colleges)