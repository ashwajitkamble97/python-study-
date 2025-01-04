# Pandas

"""pandas is popular open-source python library used for data manipulation , anlysis and cleaining.
its provides us powerfull tools for working with structured data specially tabular data(data in rows and colunms)
it is build in top of NumPy and integrates well with python libraries in python's data science ecosystem."""

# 1. Series and DataFrames
# 1.1 Series
# A Series is a one-dimensional array with labels (index). 
# It can hold any data type (integers, strings, floats, etc.). 
# Think of it as a single column of a spreadsheet.

# import pandas as pd
# #create series with list
# l = [100,200,300,400,500,600]
# seriesData = pd.Series(l, index=['A','B','C','D','E','F'])
# print(seriesData)
# #acessing element
# print(seriesData['D'])# index
# print(seriesData[0])
# ----------------------------------------------------------------------------------
# 1.2 DataFrame
# A DataFrame is a two-dimensional labeled data structure, like a table in Excel. 
# It’s the core data structure of Pandas.

# Create a DataFrame from a dictionary
# import pandas as pd

# data =pd.DataFrame(
#     {
#         'Names' :['ashwajit','rohit','kunal','achal'],
#         'Ages'  :[26, 25, 24, 23],
#         'Salary':[40000,25000,50000,23000]
#     }
# )
# # print(data) 
# #accessing data
# # print(data['Names'])# by column
# # print(data.loc[0])# Access a row by index
# print(data.iloc[2:3])# Access rows by position
# ------------------------------------------------------------------------------
# 2. Reading and Writing Data
# Pandas makes it easy to load data from and save data to various formats.
# import pandas as pd
# data =pd.DataFrame(
#     {
#         'Names' :['ashwajit','rohit','kunal','achal'],
#         'Ages'  :[26, 25, 24, 23],
#         'Salary':[40000,25000,50000,23000]
#     }
# )
# # print(data)
# wrtData = data.to_csv('data.csv', index=False)#wright data in csv file
# rigtData = pd.read_csv('data.csv')#read data in csv file
# print(rigtData)
# ---------------------------------------------------------------------------------
# 3. Data Exploration
# Pandas offers various methods to quickly explore and summarize data.
import pandas as pd
data =pd.DataFrame(
    {
        'Names' :['sumedh','sachin','swapnil','snehal','naitik','vikki','ashwajit','rohit','kunal','achal'],
        'Ages'  :[38,36,34,34,30,30,26, 25, 24, 23],
        'Salary':[20000,22000,18000,75000,30000,None,40000,25000,50000,23000]
    }
)
# print(data)
# print(data.head())# first 5
# print(data.tail(3))# last 3
# print(data.info())## Get information about the DataFrame
print(data.describe())## Get summary statistics

