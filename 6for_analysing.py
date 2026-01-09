# 1 - select specific column use square brackets
# 2 - filter rows use bollean conditions
# 3 - combine multiple conditions

# selecting columns
# 1 - a series
# 2 - dataframe multiple columns of data

# column = df["column name"]
# subset = df["column1", "column2",...]

# filtering rows - boolean indexing

# based on single conditions
# filtered_rows = df[df["salary"] > 50000]

# for multiple cnditions
# filtered_rows = df[(df['column1']> 50000) & (df["column2"] < 80000)]


import pandas as pd

data = {
    "Name": ["Ram", "Shyam", "Hari", "Sita", "Gita", "Rita"],
    "Age": [20, 22, 25, 24, 21, 23],
    "Salary": [75000, 40000, 45000, 60000, 40000, 55000],
    "Performance": [95, 70, 75, 80, 70, 90]
}

df = pd.DataFrame(data)

# print("Sample dataframe")
# print(df)
# print("Names (Single column returns series)")
# name = df["Name"]
# print(name)

# for multiple columns
# subsets = df[["Name", "Salary"]]
# print(subsets)



# for rows filtering
# first for single condition
print("For those whose age is above 22.")
filtered_rows = df[df["Age"] > 22]
print(filtered_rows)


# second for multiple conditions
print("For those whose Age is above 22 and salary greater than 50,000.")
new_rows = df[(df["Age"] > 22) & (df["Salary"] > 50000)]
print(new_rows)

# we acn also use OR
print("Those whose age is graeter than 22 or have salary heighere than 50,000.")
or_rows = df[(df["Age"] > 22) | (df["Salary"] >50000)]
print(or_rows)