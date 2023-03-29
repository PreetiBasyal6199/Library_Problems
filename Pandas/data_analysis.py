import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("MOCK_DATA .csv")

'''
Returning the first five data
'''

df_top = df.head()
print(df_top)


'''
Returning the last five data
'''
df_bottom = df.tail()
print(df_bottom)

'''
    Getting info about the dataframe
'''
print(df.info())


'''
    Remove rows that contain empty cells.
'''
df.dropna()                                 # Note: By default, the dropna() method returns a new DataFrame, and will not change the original.
df.dropna(inplace=True)                     # Note: Now, the dropna(inplace = True) will NOT return a new DataFrame, but it will remove all rows containing NULL values from the original DataFrame.

'''
Replacing empty cells with new value
'''
df.fillna(20)

'''
    Replace Only For Specified Columns
'''
df['first_name'].fillna("Test", inplace=True)

'''
Replace the specific position data
'''

df.loc[1,'first_name'] ="Updated Name"              # this will change the data of 1st location of column first_name
print(df)


'''
Looping around the data
'''
for x in df.index:
    if df.loc[x, 'gender'] =="Male":
        df.drop(x, inplace=True)
print(df)

'''
Removing duplicates
'''

df.drop_duplicates(inplace=True)

'''
Plotting the dataframe
'''
df.plot(kind="scatter", y="gender", x='ip_address')
plt.show()

