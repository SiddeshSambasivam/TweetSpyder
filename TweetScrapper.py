"""
_____________________________________________________________________________________

T W E E T   S P Y D E R 
_____________________________________________________________________________________

TweetSpyder is a web based utility program to scrap data from twitter using its api. 
The program cleans the data and stores the cleaned information to csv file for further 
exploration and analysis.


Twitter has various notable APIs such as: 
    Tweets: Searching, Posting, Filtering, engagement, streaming.
    Trends: Trending topics in a given location.
    Geo: Information about known places or places near a location.

-----------------------------------------------------------------------------------

Project Scrap away

"""

import json
import tweepy
import os
import pandas as pd 
from Credentials import json_cred
import time


def startup():

    time.sleep(0.5)
    print('\t[0]Importing the dependencies...')

    cred_status = os.path.exists('./UserCredentials.json')
    time.sleep(0.5)
    print('\t[1]Checking the status of the .json file')
    if(cred_status==0):
        json_cred()
    
    global creds 

    with open('UserCredentials.json','r') as file:
        creds = json.load(file)
        time.sleep(0.5)
        print('\t[2]File Loaded')

def authenticate():
    
    global auth 
    auth = tweepy.OAuthHandler(creds['Consumer_key'], creds['Consumer_secret'])

    auth.set_access_token(creds['Access_token'], creds['Access_key'])
    time.sleep(1)
    print('\t[3]Authenticating the Access...')
    api = tweepy.API(auth)

def tracker(name):

    c = os.path.exists('./database.txt')
    d = str(name) + ':'
    with open('./database.txt', 'a') as file:
        file.write(d)
    print('file written')
    
    
def write(tweets):

    FileName = str(input('\n\nFile Name: '))
    
    print('Data is being written into the file...')
    FileName.replace(' ','')
    data = pd.DataFrame(data=[tweet.text for tweet in tweets], columns=['Tweets'])
    loc = 'Data_Base/{}.csv'.format(FileName)
    data.to_csv(loc)
    time.sleep(2)
    print('Data written')
    tracker(FileName)
        

def read():
    print("\n\t\t\tDataBase of dataframes")
    with open('database.txt', 'r') as file:
        l = file.readline()
        print(l)
    s = str(l).split(':')
    for i in range(0,len(s)):
        print(i,'.',s[i],'\n')

    
    #data = pd.read_csv('./tweets.csv')
    #time.sleep(2)
    #print('\n\nPrinting the dataframe...\n')
    #print(data)


def main():    
    retry = 'y'
    s=0
    while(retry=='y'):
        
        os.system('clear')    
        print('\n\n\t\t\t______________________\n')
        print("    \t\t\tT W E E T  S P Y D E R")
        print("    \t\t\t______________________\n")
        

        if(s==0):
            startup()
            authenticate()
            s+=1
        api = tweepy.API(auth)
        time.sleep(2)
        choice = int(input('\n\t1. Query tweets\n\t2. View the dataframe\n\t3. Exit\n\n\tChoice= '))
        if(choice == 1):
            api = tweepy.API(auth)
            query_text = str(input('\nQuery text: '))
            tweets = api.search(query_text, count=200, lang= 'en')
            time.sleep(1)
            print('\n[]Query search complete.\n')
            time.sleep(1)
            write(tweets)
            
            
        elif(choice == 2):
            read()
        
        elif(choice == 3):
            exit()

        time.sleep(1)
        retry=str(input('\n\nRetry (y/n): '))
    

if __name__ == "__main__": 
    main()
    