'''
vertically (row-wise)
horizontally (column wise)

pd.concate[df1, df2], axis = 0, ignore_index = True

axis = 1 for column
axis = 0 for row as default
'''
import pandas as pd

# Vertically
df_Region1 = pd.DataFrame({
    "CustomerID" : [1,2],
    "Name" : ["Gopal", "Raju"]
})
df_Region2 = pd.DataFrame({
    "CustomerID" : [3, 4],
    "Name" : ["Shyam", "Hari"]
})

df_concate = pd.concat([df_Region1, df_Region2], axis= 0, ignore_index= True)
df_concate = pd.concat([df_Region1, df_Region2], axis= 1, ignore_index= True)
print(df_concate)