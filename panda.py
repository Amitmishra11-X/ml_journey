import pandas as pd
#creating data 
df = pd.DataFrame({'yes' : [50, 100], 'NO' : [60, 20]})
print (df)

df = pd.DataFrame({'Rohan': ['Item is good', 'okk'],
                   'Ram': ['good', 'okk']},
                  index=['product A', 'product B'])
print(df)