# Adding column

import pandas as pd

data = {
    "Name": ["Ram", "Shyam", "Hari", "Sita", "Gita", "Rita"],
    "Age": [20, 22, 25, 24, 21, 23],
    "Salary": [75000, 40000, 45000, 60000, 40000, 55000],
    "Performance": [95, 70, 75, 80, 70, 90]
}

df = pd.DataFrame(data)
print(df)

# use  square bracket to add column df["Column_name"] = some_data

# print("After adding Bonus column")
# df["Bonus"] = df["Salary"] * 0.1
# df["Total Salary"] = df["Bonus"] + df["Salary"]
# print(df)

# this as an straight fordward method
# Now using alternative method called insert()
# Here we can place the column at speific position as required

# synatx for insert(location, df["column_name"], data)
# lets try
print("Using inset() method.")
# Note: you don't have to use df["Column name"] while craeting new column column using insert() method simply write "column name"
df.insert(3, "Bonus", df["Salary"] * 0.1)
df.insert(0, "Employee ID", [1, 2, 3, 4, 5, 6])
print(df)