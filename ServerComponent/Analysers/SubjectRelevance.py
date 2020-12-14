import os
import time
from dask import dataframe as dd
import jellyfish
from TextExtraction.APIs.TextAPI import getListOfSentences

csv_path = os.path.join(os.path.dirname(__file__), "india-news-headlines.csv")
headlines = dd.read_csv(csv_path).headline_text


def get_mean(sentances_scores):
    return sum(sentances_scores.values()) / len(sentances_scores.values())


def calculate_maximum_similarity(social_media_post_text, timeout=10):
    start = time.time()
    max_sim = 0
    for current_headline in headlines:
        current_sim = jellyfish.jaro_distance(social_media_post_text, current_headline)
        if current_sim > max_sim:
            max_sim = current_sim
        current_time = time.time() - start
        if current_time > timeout:
            return max_sim * 100
    return max_sim * 100


def calculate_maximum_similarity_mean(social_media_post_text, timeout=5):
    start = time.time()
    sentences = getListOfSentences(social_media_post_text)
    distance_each_sentence = {}
    for sentence in sentences:
        distance_each_sentence[sentence] = 0

    for current_headline in headlines:
        for sentence in sentences:
            current_sim = jellyfish.jaro_distance(sentence, current_headline)
            if current_sim > distance_each_sentence[sentence]:
                distance_each_sentence[sentence] = current_sim
        current_time = time.time() - start
        if current_time > timeout:
            return get_mean(distance_each_sentence) * 100
    return get_mean(distance_each_sentence) * 100


#start = time.time()
#print(calculate_maximum_similarity("Another HISTORIC breakthrough today! Our two GREAT friends Israel and the Kingdom "
#                                   "of Morocco have agreed to full diplomatic relations – a massive breakthrough for "
#                                   "peace in the Middle East!"))
#print(time.time() - start)

#start = time.time()
#dist = calculate_maximum_similarity_mean(
#    "Another HISTORIC breakthrough today! Our two GREAT friends Israel and the Kingdom "
#    "of Morocco have agreed to full diplomatic relations – a massive breakthrough for "
#    "peace in the Middle East!")
#print(dist)
#print(time.time() - start)
