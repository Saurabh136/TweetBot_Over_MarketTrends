#from pytz import ZERO
#import json
#import time
import tweepy
import requests
import nsepy
import nsepython

API_KEY = "UxchAKdsCbipMBigk98o6svy0"
SECRET_KEY = "RWWYJ3D9DCYJU163yYgtV0kAloJlxNO6EQMfDnBV9HRQzPoWyj"
ACCESS_TOKEN = "1530279393569800193-ZQBlg8NHt7AB3ccqmKMO3lhewuDbFy"
ACCESS_TOKEN_SECRET = "Ya4RQq7xyPxV55WouezWxmD9OBhqXCTwkGx3X6nmU6abK"

auth_handler = tweepy.OAuthHandler(consumer_key=API_KEY, consumer_secret=SECRET_KEY)
auth_handler.set_access_token(ACCESS_TOKEN,ACCESS_TOKEN_SECRET)

api = tweepy.API(auth_handler, wait_on_rate_limit=True)

print('logged in')

from nsepython import *

def nse_reaction(index,attribute="last"):
    #positions = nsefetch('https://www.nseindia.com/api/equity-stockIndices?index=SECURITIES%20IN%20F%26O')
    #positions = nsefetch('https://www.nseindia.com/api/marketStatus')
    positions= nsefetch("https://www.nseindia.com/api/allIndices")
    endp = len(positions["data"])
    for x in range(0, endp):
        if(positions['data'][x]['index']==index.upper()):
           return positions['data'][x][attribute]

#print(nse_reaction("NIFTY 50"))
nifty = nse_reaction("NIFTY 50","percentChange")
present_close = nse_reaction("NIFTY 50","last")
previous_close =nse_reaction("NIFTY 50","previousClose")

#print(nifty)
#print(present_close)
#print(previous_close)


currentDay_price= float(present_close)
previousDay_price = float(previous_close)


if      currentDay_price > previousDay_price : #and currentDay_price > 0 :
        print(" Market rallied up by " + str(nifty) + " % , We are in a bull run. ")
        message = ' Market rallied up by ' +  str(nifty) + '% , We are in a bullrun. '       
elif    currentDay_price < previousDay_price : #and currentDay_price < 0 :
        print(' Market collapsed by ' + str(nifty) + " % , The bear run continues. ")
        message = ' Market collapsed by ' + str(nifty) + ' % , The bear run continues. '   
elif    currentDay_price >= previousDay_price and currentDay_price >= 0 :                                             
        print(" Bull Market continues , Market jumps by " + str(nifty) + " % . ")
        message = 'Bull Market continues ,  Market jumps by ' + str(nifty) + " % ."
elif    currentDay_price <= previousDay_price and currentDay_price < 0:                                                                       
        print(" Bloodbath continues , Market bleeds by " + str(nifty) + ' % .')
        message = 'Bloodbath continues , Market bleeds by ' + str(nifty) + ' % .'
elif    previousDay_price < currentDay_price : #and currentDay_price > 0 :                                                                            
        print(" Market makes fantastic recovery, bounces by " + str(nifty) + " % .")
        message = " Market makes fantastic recovery, bounces by " + str(nifty) + " % ."
elif    previousDay_price > currentDay_price: #and currentDay_price < 0 :                                                                     
        print(" Horrific reveral, Market loses " + str(nifty) + " % .")
        message = " Horrific reveral, Market loses " + str(nifty) + " % . "

api.update_status(message)
print('tweet was posted')










