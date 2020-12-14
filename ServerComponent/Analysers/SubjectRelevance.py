from dask import dataframe as dd
import jellyfish


def load_entries():
    news_headlines = []
    chunksize = 10 ** 6
    for chunk in dd.read_csv("india-news-headlines.csv", chunksize=chunksize):
        for values_group in chunk.values:
            news_headlines.append(values_group[2])
    return news_headlines


headlines = load_entries()


def calculate_maximum_similarity(social_media_post_text):
    max_sim = 0
    for current_headline in headlines:
        current_sim = jellyfish.jaro_distance(social_media_post_text, current_headline)
        if current_sim > max_sim:
            max_sim = current_sim
    return max_sim


def extract_headlines_from_csv():
    chunksize = 10 ** 3
    file = open("headlines.txt", "w")
    for chunk in dd.read_csv("india-news-headlines.csv", chunksize=chunksize):
        for values_group in chunk.values:
            file.write(values_group[2] + "\n")


print(calculate_maximum_similarity("Lionel Messi"))
