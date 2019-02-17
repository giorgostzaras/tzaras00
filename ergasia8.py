import tweepy


consumer_key = "VKZuPE4yjidJN2RiZUolPDW54"
consumer_secret = "oHVMerqwwSGKI7JPHz1pH711qYR7N54ekotZH7wQ6eQSIMqI5m"
access_token = "2811912901-WP3qVXLPktdV3z6NVZFlsfyNXcoccCdgFMWS1XY"
access_token_secret = "MJhkdlxWBBzO24pucDbkpfZnWtBkHVOcNZpglYTKF9c6n"


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
API = tweepy.API(auth)

x = raw_input("Please enter the name of the first user \n")
y = raw_input("Please enter the name of the second user \n ")

user1 = API.get_user(x)
user2 = API.get_user(y)
    
followersofuser1 = user1.followers_count
followersofuser2= user2.followers_count

print "Number of followers of the first user:"
print followersofuser1
print "Number of followers of the second user:"
print followersofuser2


tweets1 = API.user_timeline(screen_name="%s" %x, count=10)
tweets2 = API.user_timeline(screen_name="%s" %y, count=10)



class TweetAnalyzer():
    
  
   # Analush twn tweets 
    def tweets(self, tweets1):
        sumofwords1 = 0
        for tweet in tweets1:
            sumofwords1= len(tweet.text.split()) + sumofwords1
        print " Number of words of the last 100 tweets by the first user:"    
        print sumofwords1
        return sumofwords1
    
    def tweets(self, tweets2):
        sumofwords2 = 0
        for tweet in tweets2:
            sumofwords2= len(tweet.text.split()) + sumofwords2
        print "Number of words of the last 100 tweets by the first user:"    
        print sumofwords2
        return sumofwords2


tweetanalyzer = TweetAnalyzer()

words1 = tweetanalyzer.tweets(tweets1)
words2 = tweetanalyzer.tweets(tweets2)
account1 = words1*followersofuser1
account2 = words2*followersofuser2

print "The first product equals to :" ,account1
print "The second product equals to :" ,account2
if account1>account2:
    print "The first user has the biggest product of followers multiplied with the words of his last 10 tweets"
elif account1 == account2:
    print "The products of their followers multiplied with the words of their last 10 tweets are the same"
else:
    print "The second user has the biggest product of followers multiplied with the words of his last 10 tweets"

   