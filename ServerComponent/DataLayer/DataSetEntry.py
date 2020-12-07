class SocialMediaDataSetEntry:
    def __init__(self, followers_number, likes_number, comments_number, share_number, grammar_index, subject_relevance,
                 label):
        self.followers_number = followers_number
        self.likes_number = likes_number
        self.comments_number = comments_number
        self.share_number = share_number
        self.grammar_index = grammar_index
        self.subject_relevance = subject_relevance
        self.label = label


class SocialMediaDataSetEntryUnlabeled:
    def __init__(self, followers_number, likes_number, comments_number, share_number, grammar_index, subject_relevance):
        self.followers_number = followers_number
        self.likes_number = likes_number
        self.comments_number = comments_number
        self.share_number = share_number
        self.grammar_index = grammar_index
        self.subject_relevance = subject_relevance
