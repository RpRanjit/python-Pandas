# how to read data

import pandas as pd

# Reading datas for csv files
# making an object
# make sure to write file path as string 
#  for csv file
# dp = pd.read_csv("sales_data_sample.csv", encoding = "latin1")
# for json file
# dp = pd.read_json("sample_Data.json")
# for exel file
# install xlrd for exel file "pip install xlrd"
dp = pd.read_excel("SampleSuperstore.xlsx")
print(dp)