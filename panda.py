import pandas as pd
#creating data 
df = pd.DataFrame({'yes' : [50, 100], 'NO' : [60, 20]})
print (df)

df = pd.DataFrame({'Rohan': ['Item is good', 'okk'],
                   'Ram': ['good', 'okk']},
                  index=['product A', 'product B'])
print(df)
import pandas as pd
df= pd.Series([1, 2, 3, 4, 5], index = ['2025 sales', '2026 sales', '2024 sales', '2023 sales', '2022 sales'], name = 'product A')
print(df)