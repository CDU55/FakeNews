from DataLayer.CredibilityScore import get_post_score


def test_credibility_score():
    followers = 600000
    likes = 200000
    shares = 30000
    quote = 5000
    grammar = 1
    tweets_number = 35000
    subject_relevance = 85

    score = get_post_score(followers, 1, tweets_number, shares, quote, likes, grammar, subject_relevance)
    assert score == 100, "Credibility score should be 100"

    followers = 50000
    likes = 200000
    shares = 30000
    quote = 5000
    grammar = 1
    tweets_number = 35000
    subject_relevance = 85

    score = get_post_score(followers, 1, tweets_number, shares, quote, likes, grammar, subject_relevance)
    assert score == 95, "Credibility score should be 95"

    followers = 50000
    likes = 50000
    shares = 30000
    quote = 5000
    grammar = 1
    tweets_number = 35000
    subject_relevance = 85

    score = get_post_score(followers, 1, tweets_number, shares, quote, likes, grammar, subject_relevance)
    assert score == 93.75, "Credibility score should be 93.75"

    followers = 50000
    likes = 50000
    shares = 30000
    quote = 5000
    grammar = 1
    tweets_number = 35000
    subject_relevance = 85

    score = get_post_score(followers, 0, tweets_number, shares, quote, likes, grammar, subject_relevance)
    assert score == 93.75, "Credibility score should be 93.75"


test_credibility_score()
