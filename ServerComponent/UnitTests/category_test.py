from DataLayer import DataCategories


def test_followers_category():
    argument1 = 600000
    argument2 = 200000
    argument3 = 50000
    argument4 = 'Not a number'
    assert DataCategories.get_followers_category(argument1) == 4, "Followers category should be 4 with 600000 input"
    assert DataCategories.get_followers_category(argument2) == 3, "Followers category should be 3 with 200000 input"
    assert DataCategories.get_followers_category(argument3) == 2, "Followers category should be 2 with 50000 input"
    assert DataCategories.get_followers_category(argument4) == 0, "Followers category should be 0 with string input"


def test_likes_category():
    argument1 = 200000
    argument2 = 50000
    argument3 = 4000
    argument4 = 'Not a number'
    assert DataCategories.get_likes_category(argument1) == 4, "Likes category should be 4 with 200000 input"
    assert DataCategories.get_likes_category(argument2) == 3, "Likes category should be 3 with 50000 input"
    assert DataCategories.get_likes_category(argument3) == 2, "Likes category should be 2 with 4000 input"
    assert DataCategories.get_likes_category(argument4) == 0, "Likes category should be 0 with string input"


def test_comments_category():
    argument1 = 60000
    argument2 = 20000
    argument3 = 3000
    argument4 = 'Not a number'
    assert DataCategories.get_comments_category(argument1) == 4, "Comments category should be 4 with 60000 input"
    assert DataCategories.get_comments_category(argument2) == 3, "Comments category should be 3 with 20000 input"
    assert DataCategories.get_comments_category(argument3) == 2, "Comments category should be 2 with 3000 input"
    assert DataCategories.get_comments_category(argument4) == 0, "Comments category should be 0 with string input"


def test_shares_category():
    argument1 = 30000
    argument2 = 7000
    argument3 = 2500
    argument4 = 'Not a number'
    assert DataCategories.get_shares_category(argument1) == 4, "Shares category should be 4 with 30000 input"
    assert DataCategories.get_shares_category(argument2) == 3, "Shares category should be 3 with 7000 input"
    assert DataCategories.get_shares_category(argument3) == 2, "Shares category should be 2 with 2500 input"
    assert DataCategories.get_shares_category(argument4) == 0, "Shares category should be 0 with string input"


def test_quote_tweets_category():
    argument1 = 5000
    argument2 = 3000
    argument3 = 1500
    argument4 = 'Not a number'
    assert DataCategories.get_quote_tweets_category(argument1) == 4, "Quote tweets category should be 4 with 5000 input"
    assert DataCategories.get_quote_tweets_category(argument2) == 3, "Quote tweets category should be 3 with 3000 input"
    assert DataCategories.get_quote_tweets_category(argument3) == 2, "Quote tweets category should be 2 with 1500 input"
    assert DataCategories.get_quote_tweets_category(argument4) == 0, "Quote tweets category should be 0 with string " \
                                                                     "input "


def test_grammar_index_category():
    argument1 = 1
    argument2 = 0.97
    argument3 = 0.81
    argument4 = 'Not a number'
    assert DataCategories.get_grammar_index_category(argument1) == 4, "Grammar index category should be 4 with 1 input"
    assert DataCategories.get_grammar_index_category(argument2) == 3, "Grammar index category should be 3 with 0.97 " \
                                                                      "input "
    assert DataCategories.get_grammar_index_category(argument3) == 2, "Grammar index category should be 2 with 0.81 " \
                                                                      "input "
    assert DataCategories.get_grammar_index_category(argument4) == 0, "Grammar index category should be 0 with string " \
                                                                      "input "


def test_tweets_number_category():
    argument1 = 35000
    argument2 = 12000
    argument3 = 4000
    argument4 = 'Not a number'
    assert DataCategories.get_tweets_number_category(argument1) == 4, "Tweets number category should be 4 with 35000 " \
                                                                      "input "
    assert DataCategories.get_tweets_number_category(argument2) == 3, "Tweets number category should be 3 with 12000 " \
                                                                      "input "
    assert DataCategories.get_tweets_number_category(argument3) == 2, "Tweets number category should be 2 with 4000 " \
                                                                      "input "
    assert DataCategories.get_tweets_number_category(argument4) == 0, "Tweets number category should be 0 with string " \
                                                                      "input "


def test_subject_relevance_index_category():
    argument1 = 85
    argument2 = 77
    argument3 = 53
    argument4 = 'Not a number'
    assert DataCategories.get_subject_relevance_index_category(argument1) == 4, "Comments category should be 4 with " \
                                                                                "85 input "
    assert DataCategories.get_subject_relevance_index_category(argument2) == 3, "Comments category should be 3 with " \
                                                                                "77 input "
    assert DataCategories.get_subject_relevance_index_category(argument3) == 2, "Comments category should be 2 with " \
                                                                                "53 input "
    assert DataCategories.get_subject_relevance_index_category(argument4) == 0, "Comments category should be 0 with " \
                                                                                "string input "


def test_label():
    argument1 = 83
    argument2 = 65
    argument3 = 64
    argument4 = 42
    argument5 = 'Not a number'
    assert DataCategories.get_label(argument1) == 1, "Label should be 1 with 83 input"
    assert DataCategories.get_label(argument2) == 1, "Label should be 1 with 65 input"
    assert DataCategories.get_label(argument3) == 0, "Label should be 1 with 64 input"
    assert DataCategories.get_label(argument4) == 0, "Label should be 0 with 42 input"
    assert DataCategories.get_label(argument5) == 0, "Label should be 0 with string input"


def run_all_test():
    test_followers_category()
    test_likes_category()
    test_comments_category()
    test_shares_category()
    test_quote_tweets_category()
    test_tweets_number_category()
    test_grammar_index_category()
    test_subject_relevance_index_category()
    test_label()


run_all_test()
