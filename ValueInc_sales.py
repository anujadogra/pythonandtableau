# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 20:26:46 2024

@author: Anuja
"""

import pandas as pd

# file_name = pd.read_csv('file.csv') <-- format of read csv 

data = pd.read_csv('transaction2.csv')


data = pd.read_csv('transaction2.csv', sep= ';')

# summary of the data
data.info()

 

# working with calculations 
# defining variables 

CostPerItem = 11.73
SellingPricePerItem = 21.11
NumberofItemsPurchased = 6

# Mathematical operations on Tableau 

ProfitPerItem = 21.11-11.73
ProfitPerItem = SellingPricePerItem - CostPerItem

ProfitPerTransaction = NumberofItemsPurchased * ProfitPerItem
CostPerTransaction = NumberofItemsPurchased * CostPerItem
SellingPricePerTransaction = NumberofItemsPurchased * SellingPricePerItem 

#CostPerTransaction coloumn Calculation 
#CostPerTransaction = NumberofItemsPurchased * CostPerItem
#To singl;e out the coloumn -- varible = dataframe['Coloumn name']

CostPerItem = data['CostPerItem']
NumberofItemsPurchased = data['NumberOfItemsPurchased']

CostPerTransaction = CostPerItem * NumberofItemsPurchased

# adding a new coloumn in dataframe 

data['CostPerTransaction'] = CostPerTransaction
data['CostPerTransaction'] = data['CostPerItem'] * data['NumberOfItemsPurchased']

#for selling price per transaction
SellingPricePerItem = data['SellingPricePerItem']
SellingPricePerTransaction = SellingPricePerItem * NumberofItemsPurchased

data['SellingPricePerTransaction'] = SellingPricePerTransaction

#for profit per trnsaction 
ProfitPerItem = data

#profit calculation = sales-cost 
data['ProfitPerTransaction']= data['SellingPricePerTransaction'] - data['CostPerTransaction']

#markup calculation = (sales- cost)/ cost

data['Markup'] =  ( data['SellingPricePerTransaction'] - data['CostPerTransaction'] ) / data['CostPerTransaction']

data['Markup'] =   data['ProfitPerTransaction']  / data['CostPerTransaction']


#Rounding Markup 
roundmarkup = round(data['Markup'], 2)

data['Markup'] = round(data['Markup'], 2)

#Combining data fields

my_name = 'Anuja' + 'Dogra'

my_date = 'Day' + '-' + 'Month' +'-' + 'Year'

# my_date = data['Day'] + '-' + data['Month'] +'-' + data['Year']

#checking coloumns data type 
print(data['Day'].dtype)

#change coloumns type : done for year, date and day

day = data['Day'].astype(str)

print(day.dtype)

# my_date = day + '-'

month = data['Month'].astype(str)
print(month.dtype)

year = data['Year'].astype(str)
print(year.dtype)

my_date = day + '-' + month + '-' + year

data.info()

#now to add this back in data frame 

data['date'] = my_date




#using iloc to view specific coloumns/rows 

data.iloc[0] # views the row with index =0 

data.iloc[0:3]  #first three rows

data.iloc[-5:]  #last 5 rows 

data.head(5)  #brings in first 5 rows

# bring in all rows and a specific coloumns 

data.iloc[:,2] # coln shows all the rows and 2 shows the second coloumn...also as both row and coloumn starts with 0, so second coloun or row may be in actual the third one  

data.iloc[4,2] # this will give a specific value 

#using split to split the client keyword field
#new_var(split var) = coloumn.str.split('sep' , expand= True)

split_col = data['ClientKeywords'].str.split(',' , expand= True)

#creating new col for the split columns in client keywords

data['ClientAge'] = split_col[0]
data['Clienttype'] = split_col[1]
data['LengthofContract'] = split_col[2]

#using the replace function 
data['ClientAge']= data['ClientAge'].str.replace('[' , '')

data['LengthofContract']= data['LengthofContract'].str.replace(']' ,'')


#using the lower fuction to change item to lowercase

data['ItemDescription'] = data['ItemDescription'].str.lower()




#HOW TO MERGE FILES

#bringing in new data set
season2 = pd.read_csv('value_inc_seasons.csv')

#mergimg files: merge_df = pd.merge(df_old, df_new, on = 'key')
   
data = pd.merge(data, season2, on = 'Month')



# Dropping col

#df = df.drop('columnname' , axis=1)

data = data.drop('ClientKeywords' , axis= 1)
# data = data.drop('Season_y' , axis= 1)
data = data.drop('Day' , axis=1)
data = data.drop('Month' , axis=1)
data = data.drop('Year' , axis=1)

#data = data.drop(['Year', 'Month'] , axis= 1)....when want to drop multiple 


#Export into a CSV

data.to_csv('ValueInc_Cleaned.csv' , index = False)



 



