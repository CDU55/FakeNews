import aspectlib as aspectlib

from DataLayer.DataSetEntry import SocialMediaDataSetEntry


@aspectlib.Aspect()
def my_decorator_exit_db(function):
    raw_data = function()
    entries = []
    for entry in raw_data:
        param_followers_number = compare_followers_number(entry)
        param_likes_number = compare_likes_number(entry)
        param_comments_number = compare_comments_number(entry)
        param_spelling = compare_spelling_number(entry)
        param_length = compare_length(entry)
        param_label = entry.label
        new_entry = SocialMediaDataSetEntry(param_followers_number, param_likes_number, param_comments_number,
                                            param_spelling, param_length, param_label)
        entries.append(new_entry)
    return entries


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
