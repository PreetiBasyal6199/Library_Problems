import pandas as pd

a={
    'person':["Ram","Hari","Sita"],
    'marks' : [100,200,300]
}

b= pd.DataFrame(a)
print(b)

''' Result:
           person  marks
        0    Ram    100
        1   Hari    200
        2   Sita    300
'''


'''
Locating the attribute using index
'''
print(b.loc[0])                         #  Note: This returns a Pandas Series.          
''' Result:
        person    Ram
        marks     100
        Name: 0, dtype: object
'''

print(b.loc[0][1])          # Reslt: 100

print(b.loc[[0,1]])               # Note: This returns a Dataframe
''' Result:
           person  marks
        0    Ram    100
        1   Hari    200
'''


'''
Giving index to Dataframes
'''

c = pd.DataFrame(a, index=["P1","P2","P3"])
print(c)
''' Result:
           person  marks
        P1    Ram    100
        P2   Hari    200
        P3   Sita    300
'''

print(c.loc["P2"])           
'''
    person    Hari
    marks      200
    Name: P2, dtype: object
'''   