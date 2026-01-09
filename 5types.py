# What should you know before analysing data
# 1 - how big is your dataset
# 2 - what are the names of columns

# basically, we can use two attributes Shapes and column

import pandas as pd

data = {
    "Name": ["Ram", "Shyam", "Hari", "Sita", "Gita", "Rita"],
    "Age": [20, 22, 25, 24, 21, 23],
    "Salary": [75000, 40000, 45000, 60000, 40000, 55000],
    "Performance": [95, 70, 75, 80, 70, 90]
}

df = pd.DataFrame(data)

print("shapes and column names")

print(f"Shapes:- {df.shape}")
print(f"Column Names:- {df.columns}")