def error_case(argument):
    if not isinstance(argument, int) and not isinstance(argument, float):
        return True
    if argument < 0:
        return True
    return False


def get_category(value, categories_values):
    if error_case(value):
        return 0
    categories_values = sorted(categories_values)
    if value < categories_values[0]:
        return 1
    if value > categories_values[len(categories_values) - 1]:
        return len(categories_values) + 1
    for category_index in range(len(categories_values) - 1):
        lower_bound = categories_values[category_index]
        upper_bound = categories_values[category_index + 1]
        if lower_bound < value <= upper_bound:
            return category_index + 2


def get_followers_category(followers_number):
    if error_case(followers_number):
        return 0
    categories_values = [10000, 100000, 500000]
    category = get_category(followers_number, categories_values)
    return category


def get_likes_category(likes_number):
    categories_values = [2000, 20000, 100000]
    category = get_category(likes_number, categories_values)
    return category


def get_comments_category(comments_number):
    categories_values = [1000, 10000, 50000]
    category = get_category(comments_number, categories_values)
    return category


def get_shares_category(shares_number):
    categories_values = [500, 5000, 25000]
    category = get_category(shares_number, categories_values)
    return category


def get_quote_tweets_category(quote_tweets):
    categories_values = [500, 2000, 4000]
    category = get_category(quote_tweets, categories_values)
    return category


def get_grammar_index_category(grammar_index):
    categories_values = [0.8, 0.95, 1]
    category = get_category(grammar_index, categories_values)
    return category


def get_tweets_number_category(tweets_number):
    categories_values = [2500, 10000, 30000]
    category = get_category(tweets_number, categories_values)
    return category


def get_subject_relevance_index_category(subject_index):
    if subject_index > 100:
        return 0
    categories_values = [50, 65, 80]
    category = get_category(subject_index, categories_values)
    return category


def get_label(credibility_score):
    if error_case(credibility_score):
        return 0
    if credibility_score >= 65:
        return 1
    else:
        return 0
