import pandas as pd
# for linear interpolation method

data = {
    "Time": [1, 2, 3, 4, 5],
    "Value": [10, None, 30, None, 50]
}

df = pd.DataFrame(data)
print("Before interpolation")
print(df)


df["Value"] = df["Value"].interpolate(method="linear")
# learn other mehods of interpolation also like time, polynomial, index etc
print("After interpolation")
print(df)


'''
Use interpolation on following states:
1. time series data 
2. numeric data with trends
3. avoid dropping rows
cons
1. can't be utilize with strings and character
2. it's output data is prediction which may always not be right
'''
