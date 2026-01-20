# Interpolation is the method where you can put estimated value in the missing values
# only use fornumerical column
# linear, polynomial interpolation etc.
# - preserve data integrity
# - smooth trends
# - avoid data loss

# we use interpolate() method which help to estimate the missing data by the help of other data present on column or datasets

import pandas as pd

data = {
    "Name": ["Ram", "Shyam", "Hari", "Sita", "Gita", "Rita"],
    "Age": [20, None, 25, 24, 21, 23],
    "Salary": [75000, None, 45000, 60000, 40000, 55000],
    "Performance": [95, None, 75, 80, 70, 90]
}

df = pd.DataFrame(data)
print(df)