from ServerComponent.TextExtraction.APIs import TextAPI, TwitterAPI


def test_textapi():
    sentence = "This is a teat. Please work!"

    # getWordsNumber function
    assert TextAPI.getWordsNumber("ERROR404:Data not found") == 0, "Should be 0"
    assert TextAPI.getWordsNumber(sentence) == 6, "Should be 6"

    # calculateNumber function
    assert TextAPI.calculateNumber("1.5K") == 1500, "Should be 1500"
    assert TextAPI.calculateNumber("15K") == 15000, "Should be 15000"
    assert TextAPI.calculateNumber("15.2K") == 15200, "Should be 15200"

    # getListOfSentences function
    assert len(TextAPI.getListOfSentences(sentence)) == 2, "Should be 2"

    # detectLanguage function
    assert TextAPI.detectLanguage(sentence) == "en", "Should be en"

    # getWrongWordsNumbers function
    assert TextAPI.getWrongWordsNumbers(sentence) == 1, "Should be 1 (teat => test)"


def test_twitterapi():
    url = 'https://twitter.com/realDonaldTrump/status/1335971721262796801'
    html = open("htmlsource.txt", "r", encoding="utf8").read()
    sentence = "This is a teat. Please work!"

    # getDataFromTwitter function
    assert TwitterAPI.getDataFromTwitter(html) != "ERROR404:Data not found"

    # getProfileName function
    assert TwitterAPI.getProfileName(url) == "realDonaldTrump"
    user = TwitterAPI.getProfileName(url)

    # checkVerifiedAccount function
    assert TwitterAPI.checkVerifiedAccount(user) == True
    assert TwitterAPI.checkVerifiedAccount("mrabobi") == False

    # getFollowers function
    assert str(TwitterAPI.getFollowers(user))[0] == '8' and str(TwitterAPI.getFollowers(user))[1] == '8'

    # getTweets function
    assert str(TwitterAPI.getTweets(user))[0] == '5' and str(TwitterAPI.getTweets(user))[1] == '9'

    # getRetweets function
    assert TwitterAPI.getRetweets(html) == 68200
    assert TwitterAPI.getLikes(sentence) == 0

    # getQuoteTweets function
    assert TwitterAPI.getQuoteTweets(html) == 11600
    assert TwitterAPI.getLikes(sentence) == 0

    # getLikes function
    assert TwitterAPI.getLikes(html) == 317200
    assert TwitterAPI.getLikes(sentence) == 0


if __name__ == "__main__":
    test_textapi()
    test_twitterapi()
    print("Everything passed")
