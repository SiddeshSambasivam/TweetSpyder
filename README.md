# TweetSpyder

![TS](https://articles-images.sftcdn.net/wp-content/uploads/sites/3/2017/05/twitter-logo-small-fade-1920.png)

## INTRODUCTION
### Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

## Required Dependencies
```
JSON 
Pandas
Tweepy
```

## Installation 
#### For Windows,<br />
Open the conda terminal and paste the following,<br /> 
```pip install tweepy```.
<br />
#### For Linux,<br /> 
Open the terminal and paste the following <br />
```sudo apt-get install python-tweepy```.

### What is TweetSpyder ?
It is an utility program which scraps tweets for a given query by the user using twitter's API. The data scrapped is then stored as a csv file from which the data can cleaned and used for further analysis and exploration.

_________

## BACKGROUND

### What is an API ?
API stands for application programming interface. In basic terms, APIs just allows application to communicate with another.
API allows us to get data from outside sources.
1. We can send an API a request detailing the information we want.
2. APIs allows our sites to alter data on other applications, too. For instance, you’ve probably seen “Share on Facebook” or “Share on Twitter” buttons on miscellaneous websites. When/if you click one of these buttons, the site you’re visiting can communicate with your Facebook or Twitter account, and alter its data by adding new status or tweet.

### So how to get THe API for twitter ? <br />
<b>step 1:</b> Go to the twitter's developer website,
[Twitter Developer site](https://developer.twitter.com/content/developer-twitter/en.html)<br />
<b>step 2:</b> Sign in to the account and go to the apps menu<br />
<b>step 3:</b> Select create an app and complete the procedures mentioned.<br />
<b>step 4:</b> After completing all the procedures, go to app details and view the keys and token tab.<br />
<b>step 5:</b> Copy the following into the program Credentials.py<br />
<t>consumer API key        ===> credentials['Consumer_key']</t><br />
Consumer API secret key ===> credentials['Consumer_secret']<br />
Access token            ===> credentials['Access_token']<br />
Access token secret     ===> credentials['Access_key']<br />

### Terminal,
![Terminal](https://github.com/IIplutocrat45II/TweetSpyder/blob/master/images/sc1.png)

### Dataframe(csv file),
![Dataframe](https://github.com/IIplutocrat45II/TweetSpyder/blob/master/images/sc2.png)



### More Details
Clear description is given to each of the function in the python file.

Finally,Pull requests/changes/stars would be really helpful.
________________________________________________________________________________________________________________________

### Authored by
SIDDESH S S 






*References: https://medium.com/@perrysetgo/what-exactly-is-an-api-69f36968a41f*
