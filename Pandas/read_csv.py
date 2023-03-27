import pandas as pd

'''
Read data from a csv file
'''
data = pd.read_csv("MOCK_DATA .csv")
print(data)                                 #  Pandas will only return the first 5 rows, and the last 5 rows
print(data.to_string())                     #  Note: This is used to return all the rows of a file

'''
    Check the number of maximum returned rows:
'''
print(pd.options.display.max_rows)     # Result: 60


'''
Increase the maximum number of rows to display the entire DataFrame:
'''

pd.options.display.max_rows =5


'''
Read data from json file
'''
json_data = pd.read_json()