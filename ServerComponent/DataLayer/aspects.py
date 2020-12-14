import aspectlib as aspectlib

from DataLayer import DataCategories


@aspectlib.Aspect()
def my_decorator_exit_db(cutpoint, *args, **kwargs):
    raw_data = yield
    for entry in raw_data:
        entry.followers_number = DataCategories.get_followers_category(entry.followers_number)
        entry.verified = entry.verified
        entry.tweets_number = DataCategories.get_tweets_number_category(entry.tweets_number)
        entry.retweets = DataCategories.get_shares_category(entry.retweets)
        entry.quote_tweets = DataCategories.get_quote_tweets_category(entry.quote_tweets)
        entry.likes_number = DataCategories.get_likes_category(entry.likes_number)
        entry.grammar_index = DataCategories.get_grammar_index_category(entry.grammar_index)
        entry.subject_relevance = DataCategories.get_subject_relevance_index_category(entry.subject_relevance)
        entry.label = DataCategories.get_label(entry.label)


def my_decorator_exit_db_fun(raw_data):
    for entry in raw_data:
        entry.followers_number = DataCategories.get_followers_category(entry.followers_number)
        entry.verified = entry.verified
        entry.tweets_number = DataCategories.get_tweets_number_category(entry.tweets_number)
        entry.retweets = DataCategories.get_shares_category(entry.retweets)
        entry.quote_tweets = DataCategories.get_quote_tweets_category(entry.quote_tweets)
        entry.likes_number = DataCategories.get_likes_category(entry.likes_number)
        entry.grammar_index = DataCategories.get_grammar_index_category(entry.grammar_index)
        entry.subject_relevance = DataCategories.get_subject_relevance_index_category(entry.subject_relevance)
        entry.label = DataCategories.get_label(entry.label)


def compare_followers_number(entry):
    if entry.followers_number < 100:
        return "low"
    else:
        if entry.followers_number < 500:
            return "medium"
        else:
            return "high"


def compare_likes_number(entry):
    if entry.likes_number < 100:
        return "low"
    else:
        if entry.likes_number < 500:
            return "medium"
        else:
            return "high"


def compare_comments_number(entry):
    if entry.likes_number < 20:
        return "low"
    else:
        if entry.likes_number < 100:
            return "medium"
        else:
            return "high"


def compare_spelling_number(entry):
    if entry.likes_number < 20:
        return "low"
    else:
        if entry.likes_number < 50:
            return "medium"
        else:
            return "high"


def compare_length(entry):
    if entry.likes_number < 20:
        return "low"
    else:
        if entry.likes_number < 50:
            return "medium"
        else:
            return "high"
