"""
_____________________________________________________________________________________

T W E E T   S P Y D E R 
_____________________________________________________________________________________

TweetSpyder is a web based utility program to scrap data from twitter using its api. 
The program cleans the data and stores the cleaned information to csv file for futher 
exploration and analysis.


Twitter has various notable APIs such as: 
    Tweets: Searching, Posting, Filtering, engagement, streaming.
    Trends: Trending topics in a given location.
    Geo: Information about known places or places near a location.

"""


print("T W E E T  S P Y D E R")
print("---------------------")
print('[0]Importing the dependencies...')

import json
import tweepy
import os
import pandas as pd 
from Credentials import json_cred


# Validating the status of the json file
#==================================================================

cred_status = os.path.exists('./UserCredentials.json')
print('[1]Checking the status of the .json file')
if(cred_status==0):
    json_cred()
    
with open('UserCredentials.json','r') as file:
    creds = json.load(file)
    print('[2]File Loaded')

#==================================================================



# AUTHENTICATION
#=================================================================================================================================================================
# OAuthHandler is an instance of a delegation protocol that is useful for conveying authorization decisions across a network of web-enabled applications and APIs. 
auth = tweepy.OAuthHandler(creds['Consumer_key'], creds['Consumer_secret'])

# The access token gives the program permission to use api such as search,stream,etc.
auth.set_access_token(creds['Access_token'], creds['Access_key'])

print('[3]Authenticating the Access...')
api = tweepy.API(auth)

#=================================================================================================================================================================



# Querying the input from user and using it to search tweets
query_text = str(input('Query text: '))
tweets = api.search(query_text, count=200, lang= 'en')

# Converting the raw data into a dataframe
data = pd.DataFrame(data=[tweet.text for tweet in tweets], columns=['Tweets'])
print(data)

# Writing the data into a csv file
data.to_csv('./tweets.csv')