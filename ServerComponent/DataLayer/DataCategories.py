def error_case(argument):
    if not isinstance(argument, int) and not isinstance(argument, float):
        return True
    if argument < 0:
        return True
    return False


def get_followers_category(followers_number):
    if error_case(followers_number):
        return 0
    if followers_number > 500000:
        # mega
        return 4
    elif 500000 >= followers_number > 100000:
        # macro
        return 3
    elif 100000 >= followers_number > 10000:
        # micro
        return 2
    else:
        # nano
        return 1


def get_likes_category(likes_number):
    if error_case(likes_number):
        return 0
    if likes_number > 100000:
        # mega
        return 4
    elif 100000 >= likes_number > 20000:
        # macro
        return 3
    elif 20000 >= likes_number > 2000:
        # micro
        return 2
    else:
        # nano
        return 1


def get_comments_category(comments_number):
    if error_case(comments_number):
        return 0
    if comments_number > 50000:
        # mega
        return 4
    elif 50000 >= comments_number > 10000:
        # macro
        return 3
    elif 10000 >= comments_number > 1000:
        # micro
        return 2
    else:
        # nano
        return 1


def get_shares_category(shares_number):
    if error_case(shares_number):
        return 0
    if shares_number > 25000:
        # mega
        return 4
    elif 25000 >= shares_number > 5000:
        # macro
        return 3
    elif 5000 >= shares_number > 500:
        # micro
        return 2
    else:
        # nano
        return 1


def get_quote_tweets_category(shares_number):
    if error_case(shares_number):
        return 0
    if shares_number > 4000:
        return 4
    elif 4000 >= shares_number > 2000:
        return 3
    elif 2000 >= shares_number > 500:
        return 2
    else:
        return 1


def get_grammar_index_category(grammar_index):
    if error_case(grammar_index):
        return 0
    if grammar_index == 1:
        return 4
    elif 1 > grammar_index >= 0.95:
        return 3
    elif 0.95 > grammar_index >= 0.8:
        return 2
    else:
        return 1


def get_tweets_number_category(tweets_number):
    if error_case(tweets_number):
        return 0
    if tweets_number > 30000:
        return 4
    elif 30000 >= tweets_number > 10000:
        return 3
    elif 10000 >= tweets_number > 2500:
        return 2
    else:
        return 1


def get_subject_relevance_index_category(subject_index):
    if error_case(subject_index):
        return 0
    if 100 >= subject_index > 80:
        return 4
    if 80 >= subject_index > 65:
        return 3
    if 65 >= subject_index > 50:
        return 2
    else:
        return 1


def get_label(credibility_score):
    if error_case(credibility_score):
        return 0
    if credibility_score >= 65:
        return 1
    else:
        return 0
