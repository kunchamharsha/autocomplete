from flask import jsonify
from pytrie import SortedStringTrie as Trie
import pandas as pd
import time

trieds=Trie() #trieds is short for trie datastructure.
listofallnames=[]

def loadstrings():
    """
    Function to load a csv file, preprocess the data and load it into the Trie Datastructure
    """
    start=time.time()
    df = pd.read_csv("data.csv",error_bad_lines=False)#loading csv data file as a dataframe using pandas
    listofallnames={}
    print 'key generation in process, please wait.'
    count=0
    for index, row in df.iterrows():
        rowdata={}
        #preprocessing data in the dataframe
        rowdata['firstname']=str(row['givenName']).lower()
        rowdata['middlename']=str(row['middleName']).lower()
        rowdata['lastname']=str(row['surname']).lower()
        if str(row['givenName'])!='nan':
            try:
                listofallnames[str(rowdata['firstname'])].append(rowdata)
            except KeyError:
                listofallnames[str(rowdata['firstname'])]=[rowdata]
        if str(row['middleName'])!='nan':
            try:
                listofallnames[str(rowdata['middlename'])].append(rowdata)
            except KeyError:
                listofallnames[str(rowdata['middlename'])]=[rowdata]
        if str(row['surname'])!='nan':
            try:
                listofallnames[str(rowdata['lastname'])].append(rowdata)
            except KeyError:
                listofallnames[str(rowdata['lastname'])]=[rowdata]
        count=count+1
        if count%25000==0:
            #a counter to notify the admin on the progress of number of keys preprocessed yet.
            print str(count)+' keys have been added to the dictionary'
    for i in listofallnames:
        trieds[i]=listofallnames[i]
    end=time.time()
    print 'total time to add keys to the trieds is '+str(end-start)



def returnsearchresults(searchterm):
    """
    Function to return search results 
    from the data repository based on the search term input by the users.
    """
    start=time.time()
    searchresults=trieds.items(prefix=searchterm)
    end=time.time()
    print 'time taken to search for the key is '+str(end-start)
    return jsonify(sorted(searchresults,key=lambda x:x[0]))

