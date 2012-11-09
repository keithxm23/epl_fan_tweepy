import tweepy

from my_credentials import insert_consumer_key, insert_consumer_secret, insert_access_token, insert_access_token_secret
# == OAuth Authentication ==
#
# This mode of authentication is the new preferred way
# of authenticating with Twitter.

# The consumer keys can be found on your application's Details
# page located at https://dev.twitter.com/apps (under "OAuth settings")
consumer_key=insert_consumer_key    
consumer_secret=insert_consumer_secret                     

# The access tokens can be found on your applications's Details
# page located at https://dev.twitter.com/apps (located 
# under "Your access token")
access_token=insert_access_token
access_token_secret=insert_access_token_secret                 

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

twount = 100 #set number of tweets

# If the authentication was successful, you should
# see the name of the account print out
print 'Showing last '+str(twount)+' tweets for '+api.me().name

# If the application settings are set for "Read and Write" then
# this line should tweet out the message to your account's 
# timeline. The "Read and Write" setting is on https://dev.twitter.com/apps
#api.update_status('Updating using OAuth authentication via Tweepy!')

for i in api.user_timeline(count=twount,include_rts=True):
        print i.text

