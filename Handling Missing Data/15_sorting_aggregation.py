# If you want to organize you data or take out summary of it sorting is use into something meaningful

# at first shorting data

# syntax  df.sort_values(by= "column NAME", true/False, inplace = true)
# True - in ascending order
# Flase - in descending order

import pandas as pd

data = {
    "Name": ["Ram", "Harui", "Gita","Shyam", "Sita"],
    "Age": [20, 33, 25, 33, 20],
    "Salary": [10000, 40000, 30000, 25000, 35000]
}

df = pd.DataFrame(data)
# for single columns
df.sort_values(by="Age", ascending=False, inplace=True)
# print(df)
# for multiple column
df.sort_values(by=["Age", "Salary"], ascending=[False, True], inplace= True)
# print(df)



# for aggregation
# to find out sum, mean,statistics or count
# summary statisctics
# df["Column name"].mean()
# df["Column name"].sum()
# df["Column name"].min()
# df["Column name"].max()

avg_salary = df["Salary"].mean()
print(avg_salary)

# most importtant part is grouping 
# which means to calculate the data in small groups

grouped = df.groupby("Age")["Salary"].sum()
print(grouped)
'''
df.groupby("Age")["Salary].sum()
age = 20 > (10000, 35000) = 45000
age = 25 [30000] = 30000
age = 33 [40000, 25000] = 65000

'''

# above is for single column group
# next is for multiple column group

grouped = df.groupby(["Age", "Name"])["Salary"].sum()
print(grouped)

'''
Some common aggregation function
1. sum() - add every value in group
2. mean() - calculate mean value in group
3. count() - calculate no of value in group
4. min() - cAlculate minimum value in group
5. max() - cAlculate minimum value in group
6. std() - cAlculate standard deviation value in group
'''