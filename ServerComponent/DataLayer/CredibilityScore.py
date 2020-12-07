from DataLayer import DataCategories

followers_weight = 15
likes_weight = 10
comments_weight = 10
share_weight = 10
grammar_weight = 15
subject_relevance_weight = 40


def get_followers_score(followers_number):
    return DataCategories.get_followers_category(followers_number) * followers_weight / 4


def get_likes_score(likes_number):
    return DataCategories.get_likes_category(likes_number) * likes_weight / 4


def get_comments_score(comments_number):
    return DataCategories.get_comments_category(comments_number) * comments_weight / 4


def get_share_score(share_number):
    return DataCategories.get_shares_category(share_number) * share_weight / 4


def get_grammar_score(grammar_index):
    return DataCategories.get_grammar_index_category(grammar_index) * grammar_weight / 4


def get_subject_relevance_score(subject_index):
    return DataCategories.get_subject_relevance_index_category(subject_index) * subject_relevance_weight / 4


def get_post_score(followers_number, likes_number, comments_number, share_number, grammar_index, subject_index):
    total_score = 0
    total_score += get_followers_score(followers_number)
    total_score += get_likes_score(likes_number)
    total_score += get_comments_score(comments_number)
    total_score += get_share_score(share_number)
    total_score += get_grammar_score(grammar_index)
    total_score += get_subject_relevance_score(subject_index)
    return total_score

