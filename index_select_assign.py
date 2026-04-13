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

#use loc and ilocdf[row:column]
colleges = df.loc[:10,['state', 'name']]
print(colleges) 

colleges = df.iloc[:10]
print(colleges)

colleges1 = df.iloc[:100][['state', 'name']]
print(colleges1)

#condition
specific_state_college = df.loc[df.state == 'Uttar Pradesh']
print(specific_state_college)