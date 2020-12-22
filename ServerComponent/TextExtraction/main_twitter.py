from APIs import WebAPI, TwitterAPI, TextAPI

#Links for test
twitter = "https://mobile.twitter.com/pinkfloyd/status/1325772237341945858"
badea = "https://mobile.twitter.com/lupulalbastru1/status/1284161708194504705"
test = "https://mobile.twitter.com/RockstarGames/status/1327306496217128967"

#Set the link
entry = twitter
#User profile name
user = TwitterAPI.getProfileName(entry)
#Html text
text = open("htmlsource.txt", "r", encoding="utf8").read()
# Text extract
data = TwitterAPI.getDataFromTwitter(text)

#Print area
print("Data about user profile")
print()
print("Username:", user)
print("Verified:", TwitterAPI.checkVerifiedAccount(user))
print("Number of followers:", TwitterAPI.getFollowers(user))
print("Number of tweets:", TwitterAPI.getTweets(user))
print()
print("Data about post")
print()
print("Likes:", TwitterAPI.getLikes(text))
print("Retweets:", TwitterAPI.getRetweets(text))
print("Quote Tweets", TwitterAPI.getQuoteTweets(text))
print("There are", TextAPI.getWrongWordsNumbers(data),"wrong words out of",TextAPI.getWordsNumber(data))
print("Text:", TwitterAPI.getDataFromTwitter(text))
print(TextAPI.getListOfSentences(data))