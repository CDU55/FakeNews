import pandas as pd
import jellyfish


def calculate_maximum_similarity(social_media_post_text):
    chunksize = 10 ** 3
    max_sim = 0
    for chunk in pd.read_csv("india-news-headlines.csv", chunksize=chunksize):
        for values_group in chunk.values:
            current_headline = values_group[2]
            current_sim = jellyfish.jaro_distance(social_media_post_text,current_headline)
            if current_sim > max_sim:
                max_sim = current_sim
    return max_sim

def extract_headlines_from_csv():
    chunksize = 10 ** 3
    file = open("headlines.txt", "w")
    for chunk in pd.read_csv("india-news-headlines.csv", chunksize=chunksize):
        for values_group in chunk.values:
            file.write(values_group[2] + "\n")
