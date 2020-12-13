from ServerComponent.TextExtraction.APIs import TextAPI


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
    pass


if __name__ == "__main__":
    test_textapi()
    test_twitterapi()
    print("Everything passed")