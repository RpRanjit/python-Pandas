# NaN(Not a number)
# None(for object)

import pandas as pd
# lets make the data null os a row
data = {
    "Name": ["Ram", None, "Hari", "Sita", "Gita", "Rita"],
    "Age": [20, None, 25, 24, 21, 23],
    "Salary": [75000, None, 45000, 60000, 40000, 55000],
    "Performance": [95, None, 75, 80, 70, 90]
}

df = pd.DataFrame(data)
print(df)
# we can detect where the data are  misssing using isnull() method
print("To check the missing data.")
# if the value is True then the data are missing otherwise it is not
print(df.isnull())
# to find out the number of missing valuse in a colummn we can use sum() method .isnull().sum()
print(df.isnull().sum())
