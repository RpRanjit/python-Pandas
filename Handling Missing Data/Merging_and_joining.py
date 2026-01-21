# merging is used while required data fo two different dataframe
# eg in an ecommerce you want to find out the list of clients who have made purchase in both year./condition or anything we use merge
# pd.merge(df1, df2, on="Column_name", how="type of join")
# df1 - 1st dataframe
# df2 - 2st dataframe
# column_name = Column name that are similar in both dataframe
# how - inner, outer. left, right, cross
# inner - output only those keys match
# outer -  output all data but give NaN in those whose keys doesn't match
# left - it gives all data of left side along with the similar keys 
# right - it gives all data of right side along with the similar keys \
# cross - '''let d1 = n rows and d2 = m rows the cross shows m*n rows every possible datasets so we don't need join key like customerId'''
import pandas as pd
df_customer = pd.DataFrame({
    "CustomerId": [1, 2, 3],
    "Name": ["Ram", "Shyam", "Hari"]
})
df_orders = pd.DataFrame({
    "CustomerId": [1, 2, 4],
    "OrderAmount": [300, 350, 400]
})

# df_merged = pd.merge(df_customer, df_orders, on="CustomerId", how="inner")
# df_merged = pd.merge(df_customer, df_orders, on="CustomerId", how="outer")
# df_merged = pd.merge(df_customer, df_orders, on="CustomerId", how="left")
# df_merged = pd.merge(df_customer, df_orders, on="CustomerId", how="right")
df_merged = pd.merge(df_customer, df_orders, how="cross")
print(df_merged)