from DataLayer import DataCategories

followers_number_weight = 10
verified_weight = 15
tweets_number_weight = 5
retweets_weight = 15
quote_tweets_weight = 5
likes_number_weight = 5
grammar_index_weight = 15
subject_relevance_weight = 30
comments_weight=10


def get_followers_score(followers_number):
    return DataCategories.get_followers_category(followers_number) * followers_number_weight / 4


def get_likes_score(likes_number):
    return DataCategories.get_likes_category(likes_number) * likes_number_weight / 4


def get_comments_score(comments_number):
    return DataCategories.get_comments_category(comments_number) * comments_weight / 4


def get_share_score(share_number):
    return DataCategories.get_shares_category(share_number) * retweets_weight / 4


def get_grammar_score(grammar_index):
    return DataCategories.get_grammar_index_category(grammar_index) * grammar_index_weight / 4


def get_subject_relevance_score(subject_index):
    return DataCategories.get_subject_relevance_index_category(subject_index) * subject_relevance_weight / 4


def get_quote_tweets_score(quote_tweets):
    return DataCategories.get_quote_tweets_category(quote_tweets) * quote_tweets_weight / 4


def get_tweets_number_score(tweets_number):
    return DataCategories.get_tweets_number_category(tweets_number) * tweets_number_weight / 4


def get_verified_score(verified):
    if verified:
        return verified_weight
    else:
        return verified_weight


def get_post_score(followers_number, verified, tweets_number, retweets, quote_tweets, likes_number, grammar_index,
                   subject_relevance):
    total_score = 0
    total_score += get_followers_score(followers_number)
    total_score += get_verified_score(verified)
    total_score += get_tweets_number_score(tweets_number)
    total_score += get_share_score(retweets)
    total_score += get_quote_tweets_score(quote_tweets)
    total_score += get_likes_score(likes_number)
    total_score += get_grammar_score(grammar_index)
    total_score += get_subject_relevance_score(subject_relevance)
    return total_score
