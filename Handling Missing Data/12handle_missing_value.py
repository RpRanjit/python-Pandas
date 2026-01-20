#  Once the missing value is detected we have to either fill it or remove it
# if that column or row desn't have any impact or alter in the dataset then removing is the best option

# for that process we use df.dropna(axis = 0, inplace = True)
# we know why we use inplace but if you have to remove missing valus in row, then place value of axis as 0, if it is colum place it to 1

import pandas as pd

data = {
    "Name": ["Ram", None, "Hari", "Sita", "Gita", "Rita"],
    "Age": [20, None, 25, 24, 21, 23],
    "Salary": [75000, None, 45000, 60000, 40000, 55000],
    "Performance": [95, None, 75, 80, 70, 90]
}

df = pd.DataFrame(data)
print(df)
# df.dropna(inplace= True) #to remove all missing value in dataframe
# df.dropna(axis= 0, inplace=True) #to remove missing value of row
# print(df)
# df.dropna(axis= 1, inplace=True) #to remove missing value of column
# print(df)


# most case we can fill the missing data by default value than just removing it for that we use fillna(default/name, inplace = True)

# df.fillna("Not Available", inplace= True)
# print(df)

# Instead of writing default we can write the mean vakue of entire data or something by calculationg
df["Age"].fillna(df["Age"].mean(), inplace=True)
df["Salary"].fillna(df["Salary"].mean(), inplace=True)
print(df)

# Note: Interpolation