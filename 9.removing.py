import pandas as pd

data = {
    "Name": ["Ram", "Shyam", "Hari", "Sita", "Gita", "Rita"],
    "Age": [20, 22, 25, 24, 21, 23],
    "Salary": [75000, 40000, 45000, 60000, 40000, 55000],
    "Performance": [95, 70, 75, 80, 70, 90]
}

df = pd.DataFrame(data)
print(df)
# Here drop helps to remove the columns or row that are not in use and 
# Here we use inplace  = True because it help to change structure in same dataframe if it is false or not use then it will create new dataset insted of using the original one
# df.drop(columns = ["Performance"], inplace= True)

# we can also delete multiple column
df.drop(columns= ["Performance", "Age"], inplace=True)
print(df)