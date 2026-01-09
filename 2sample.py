# how to  make files
import pandas as pd

data = {
    "Name": ['Ram', 'Shyam', 'Hari', 'Sita'],
    "Age": [15, 20, 25, 10],
    "Location": ["Pokhara", "Kathmandu", "Chitwan", "Lalitpur"]
}

df = pd.DataFrame(data)
# print(df)

# df.to_csv("sample_data.csv", index=False)
# for xlsx file Python use module openpyxl if not install "pip install openpyxl"
# df.to_excel("sample_data.xlsx", index=False)
df.to_json("sample_data.json", index=False)

# print(pd.read_excel("sample_data.xlsx"))