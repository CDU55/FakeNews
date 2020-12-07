def get_followers_category(followers_number):
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


def get_grammar_index_category(grammar_index):
    if grammar_index == 1:
        return 4
    elif 1 > grammar_index >= 0.95:
        return 3
    elif 0.95 > grammar_index >= 0.8:
        return 2
    else:
        return 1


def get_subject_relevance_index_category(subject_index):
    if 100 >= subject_index > 80:
        return 4
    if 80 >= subject_index > 65:
        return 3
    if 65 >= subject_index > 50:
        return 2
    else:
        return 1


def get_label(credibility_score):
    if credibility_score >= 75:
        return 1
    else:
        return 0
