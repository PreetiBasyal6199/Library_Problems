import pandas as pd

'''
Read data from a csv file
'''
data = pd.read_csv("MOCK_DATA.csv")
print(data.to_string())