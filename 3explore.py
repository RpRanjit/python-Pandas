# 1. understant the data sets
# 2. identify the problems
# 3. plan the next step

# let's assume you have thousands or millions of data, so it is impossible to analyse all of them that's where modles name head() and tail() are in use 
# where head() is used to extract data from the head/top. You can use head(n) n- no of data/rows but the default is 5
# where tail() is used to extract data from the tai;/bottom. You can use tail(n) n- no of data/rows but the default is 5

import pandas as pd

# df= pd.read_json("sample_Data.json")
# # print(df)

# print("For top/head content")
# print(df.head(6)) # you can use head() only it defaukt value is 5

# print("For bottom/tail content")
# print(df.tail(6))


# we get the basic structure of data but
# 1. we don;t know the n of rows/ column
# 2. what typr of datatypes are they storing and
# 3. and are there any data missiong or not

# that why we use info() method which gives
# no of rows, column    column name    datatypes  non null count   memory uses in dataframe

df= pd.read_json("sample_Data.json")
print("Displaying info of the data set")

print(df.info())