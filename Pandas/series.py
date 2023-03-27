import pandas as pd

'''
Series is like column in a table. It is a 1-D array holding data of anytype.
'''

a =[1,2,3,4]

''' 
Without Labels
'''
b= pd.Series(a)
print(b)
''' Result: 
        0    1
        1    2
        2    3
        3    4
        dtype: int64
'''
print(b[3])                 # Result:  4
# print(b[4])                 # KeyError


'''
With Labels
'''

c=pd.Series(a, index=['a','b','c', 'd'])
print(c)
'''  Result:
        a    1
        b    2
        c    3
        d    4
        dtype: int64
'''

print(c['d'])               # Result: 4


'''
We can also use key-value pair like dictionary for creating Series
'''

dict1={
    'apple': 140,
    'banana': 100,
    'orange': 140
}
dict_series=pd.Series(dict1)
print(dict_series)
''' Result:
        apple     140
        banana    100
        orange    140
        dtype: int64
'''

dict_series2 = pd.Series(dict1, index=["apple","banana"])
print(dict_series2)

'''
    Result:
    apple     140
    banana    100
    dtype: int64
'''

dict_series3 = pd.Series(dict1, index=["apple","cat"])
print(dict_series3) 

''' Result:
        apple    140.0
        cat        NaN
        dtype: float64
'''