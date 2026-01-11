import pandas as pd

data = {
    "Name": ["Ram", "Shyam", "Hari", "Sita", "Gita", "Rita"],
    "Age": [20, 22, 25, 24, 21, 23],
    "Salary": [75000, 40000, 45000, 60000, 40000, 55000],
    "Performance": [95, 70, 75, 80, 70, 90]
}

df = pd.DataFrame(data)
print(df)

# updating single data using .loc[] method
# df.loc[index, "Column_Name"] = data

# print("After updating salary of Ram")
# df.loc[0, "Salary"] = 55000
# print(df)

# updating data for entire column
# print("Updating Salary by 10%")
# df["Salary"] = df["Salary"] * 1.10
# print(df)


# updating salary using conditions

print("Updating Salary of those whose performance is grater tyhan 80 by 15%")
# df["Salary"] = df.loc[df["Performance"] > 80, "Salary"] * 1.15
# if we use above method only whose performance is >80 will be cvisible and other will be not available, So
df.loc[df["Performance"] > 80, "Salary"] = df.loc[df["Performance"] > 80, "Salary"] * 1.15
print(df)