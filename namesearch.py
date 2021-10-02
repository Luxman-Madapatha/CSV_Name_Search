#!/usr/bin/env python
# coding: utf-8

# In[1]:


#!/usr/bin/env python
# coding: utf-8
# In[1]:
#Import required Pythin modules
import time
#start time count
tic = time.perf_counter()
import pandas as pd
from csv import writer
import csv
import re
import sys
import os

#set recursionlimit
sys.setrecursionlimit(10**9) 

# special characters in names
regex = re.compile('[._-]') 

#define variable names of csv and xlsx
dict_excel_file = 'firstnames and lastnames.xlsx'
input_DATABASE = 'DATABASE.csv'

#copy previous OUTPUT.csv to the backup folder
os.system('cmd /c "move OUTPUT.csv BACKUP"')

# import the names "firstnames" file into a data frame
df1 = pd.read_excel(dict_excel_file, sheet_name='Firstnames')

#import the input csv file into a data frame
df2 = pd.read_csv(input_DATABASE)

# import the names "lastnames" file into a data frame
df3 = pd.read_excel(dict_excel_file, sheet_name='Lastnames')

# Keep the DataFrame with valid entries in the same variable for all three dataframes.
df1.dropna(inplace=True)
df2.dropna(inplace=True)
df3.dropna(inplace=True)

#convert the thre data frames into dictionaries
dictionaryDF1 = df1.to_dict()
dictionaryDF2 = df2.to_dict()
dictionaryDF3 = df3.to_dict()

#define variables

#tracker for single and double names

#single names in first names
setSingle1 = set()
#single names in last names
setSingle2 = set()

#double names in first names
dictDouble0 = {}
#double names in last names
dictDouble1 = {}

#printing function1 to OUTPUT.csv file [without formatting]

def append_list_as_row(file_name, list_of_elem):
    # Open file in append mode
    with open(file_name, 'a+', newline='') as write_obj:
        # Create a writer object from csv module
        csv_writer = writer(write_obj)
        # Add contents of list as last row in the csv file
        csv_writer.writerow(list_of_elem)

#print the headers to the OUTPUT.csv file
OutputFileHeaders = ["INPUT","OUTPUT1","OUTPUT2"]
append_list_as_row('OUTPUT.csv', OutputFileHeaders) 

#printing function2 to OUTPUT.csv file [with formatting]

#string1 input
#string2 dictionary
#string3 outcome message

def printToCsv(string1,string2,string3):
     
    LEN1 = len(string1)
    LEN2 = len(string2)
    LEN3 = LEN2/LEN1
    row_contents = str(string1+","+ string2 + " " + string1 + "," +'{0:1.0%}'.format(LEN3)+ "," +string3)
    row_contentsList = list(row_contents.split(",")) 
    print(list(row_contentsList))
    append_list_as_row('OUTPUT.csv', row_contentsList)

#function to check for double names

def dicDoubleFunction(nameStr,dictionaryDF1, dictionaryDF3):
    
    SplitList1 = re.split(regex,nameStr,1)
    
    for key in dictionaryDF1["FIRSTNAME"]: 
        if  dictionaryDF1["FIRSTNAME"][key] == SplitList1[0]:
            dictDouble0[nameStr] = SplitList1[0]
            break
            
    for key in dictionaryDF3["LASTNAME"]: 
        if  dictionaryDF3["LASTNAME"][key] == SplitList1[1]:
            dictDouble1[nameStr] = SplitList1[1]
            break
        
    if (nameStr in dictDouble0 and nameStr in dictDouble1):
        printToCsv(nameStr, SplitList1[0] + " " + SplitList1[1],"Exactly match both names")
        
    elif nameStr in dictDouble0:
        printToCsv(nameStr,SplitList1[0],"Matched firstname only")  
        
    elif nameStr in dictDouble1:
        printToCsv(nameStr,SplitList1[1],"Matched lastname only")
        
    elif (nameStr not in dictDouble0 and nameStr not in dictDouble1):
        printToCsv(nameStr,"","Both not found!")
        
#function to check for single names in DF1

def dicSingleFunctionFirst(nameStr,dictionaryDF1):
        
    for key in dictionaryDF1["FIRSTNAME"]:
                        
        if nameStr == dictionaryDF1["FIRSTNAME"][key]:
            printToCsv(nameStr,dictionaryDF1["FIRSTNAME"][key],"Exact match from firstname")
            setSingle1.add(nameStr)
            break
            
        elif nameStr[:-1] == dictionaryDF1["FIRSTNAME"][key]:
            printToCsv(nameStr,dictionaryDF1["FIRSTNAME"][key],"Leading match from firstname")
            setSingle1.add(nameStr)
            break
            
        elif nameStr[1:] == dictionaryDF1["FIRSTNAME"][key]:
            printToCsv(nameStr,dictionaryDF1["FIRSTNAME"][key],"Trailing match from firstname")
            setSingle1.add(nameStr)
            break
            
#function to check for single names in DF3
            
def dicSingleFunctionLast(nameStr,dictionaryDF3):
    
    for key in dictionaryDF3["LASTNAME"]:
        if nameStr == dictionaryDF3["LASTNAME"][key]:
            printToCsv(nameStr,dictionaryDF3["LASTNAME"][key],"Exact match from lastname")
            setSingle2.add(nameStr)
            break
        
        elif nameStr[:-1] == dictionaryDF3["LASTNAME"][key]:
            printToCsv(nameStr,dictionaryDF3["LASTNAME"][key],"Leading match from lastname")
            setSingle2.add(nameStr)
            break
            
        elif nameStr[1:] == dictionaryDF3["LASTNAME"][key]:
            printToCsv(nameStr,dictionaryDF3["LASTNAME"][key],"Trailing match from lastname")
            setSingle2.add(nameStr)
            break

#main look through input file which calls above functions

for key in dictionaryDF2["NAME"]:
      
    if(regex.search(dictionaryDF2["NAME"][key]) == None): 
        dicSingleFunctionFirst(dictionaryDF2["NAME"][key],dictionaryDF1)
        
        if dictionaryDF2["NAME"][key] not in setSingle1:
            dicSingleFunctionLast(dictionaryDF2["NAME"][key],dictionaryDF3)
            if dictionaryDF2["NAME"][key] not in setSingle2:
                printToCsv(dictionaryDF2["NAME"][key],"","Not Found!")
        
    else:
        dicDoubleFunction(dictionaryDF2["NAME"][key],dictionaryDF1,dictionaryDF3)

# timer code

toc = time.perf_counter()

print("I----------------- STATS---------------------------------------------------------I")
print(f"Downloaded the file in {toc - tic:0.2f} seconds")
print("I----------------- STATS---------------------------------------------------------I")  


# In[ ]:





# In[ ]:




