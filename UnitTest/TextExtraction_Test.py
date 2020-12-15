from ServerComponent.TextExtraction.APIs import TextAPI, TwitterAPI
import unittest


class TestTwitter(unittest.TestCase):
    def test_textapi(self):
        sentence = "This is a teat. Please work!"

        # getWordsNumber function
        self.assertEqual(TextAPI.getWordsNumber("ERROR404:Data not found"), 0)
        self.assertEqual(TextAPI.getWordsNumber(sentence), 6)

        # calculateNumber function
        self.assertEqual(TextAPI.calculateNumber("1.5K"), 1500)
        self.assertEqual(TextAPI.calculateNumber("15K"), 15000)
        self.assertEqual(TextAPI.calculateNumber("15.2K"), 15200)

        # getListOfSentences function
        self.assertEqual(len(TextAPI.getListOfSentences(sentence)), 2)

        # detectLanguage function
        self.assertEqual(TextAPI.detectLanguage(sentence), "en")

        # getWrongWordsNumbers function
        self.assertEqual(TextAPI.getWrongWordsNumbers(sentence), 1)

    def test_twitterapi(self):
        url = 'https://twitter.com/realDonaldTrump/status/1335971721262796801'
        html = open("htmlsource.txt", "r", encoding="utf8").read()
        sentence = "This is a teat. Please work!"

        # getDataFromTwitter function
        self.assertNotEqual(TwitterAPI.getDataFromTwitter(html), "ERROR404:Data not found")

        # getProfileName function
        self.assertEqual(TwitterAPI.getProfileName(url), "realDonaldTrump")
        user = TwitterAPI.getProfileName(url)

        # checkVerifiedAccount function
        self.assertEqual(TwitterAPI.checkVerifiedAccount(user), True)
        self.assertEqual(TwitterAPI.checkVerifiedAccount("mrabobi"), False)

        # getFollowers function
        self.assertEqual(str(TwitterAPI.getFollowers(user))[0], '8')
        self.assertEqual(str(TwitterAPI.getFollowers(user))[1], '8')

        # getTweets function
        self.assertEqual(str(TwitterAPI.getTweets(user))[0], '5')
        self.assertEqual(str(TwitterAPI.getTweets(user))[1], '9')

        # getRetweets function
        self.assertEqual(TwitterAPI.getRetweets(html), 68200)
        self.assertEqual(TwitterAPI.getLikes(sentence), 0)

        # getQuoteTweets function
        self.assertEqual(TwitterAPI.getQuoteTweets(html), 11600)
        self.assertEqual(TwitterAPI.getLikes(sentence), 0)

        # getLikes function
        self.assertEqual(TwitterAPI.getLikes(html), 317200)
        self.assertEqual(TwitterAPI.getLikes(sentence), 0)


if __name__ == "__main__":
    unittest.main()
