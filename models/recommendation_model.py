import pandas as pd
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np


class MovieRecommender:
    def __init__(self, movies_path, ratings_path):
        self.movies = pd.read_csv(movies_path)
        self.ratings = pd.read_csv(ratings_path)
        self.movies["clean_title"] = self.movies["title"].apply(
            self.clean_title)

        self.vectorizer = TfidfVectorizer(ngram_range=(1, 2))
        self.tfidf = self.vectorizer.fit_transform(self.movies["clean_title"])

    def clean_title(self, title):
        return re.sub("[^a-zA-Z0-9 ]", "", title)

    def search(self, title):
        title = self.clean_title(title)

        query_vec = self.vectorizer.transform([title])
        similarity = cosine_similarity(query_vec, self.tfidf).flatten()
        indices = np.argpartition(similarity, -5)[-5:]
        results = self.movies.iloc[indices].iloc[::-1]

        return results

    def find_similar_movies(self, movie_id):
        similar_users = self.ratings[(self.ratings["movieId"] == movie_id) & (
            self.ratings["rating"] > 4)]["userId"].unique()

        similar_user_recs = self.ratings[(self.ratings["userId"].isin(
            similar_users)) & (self.ratings["rating"] > 4)]["movieId"]

        similar_user_recs = similar_user_recs.value_counts() / len(similar_users)
        similar_user_recs = similar_user_recs[similar_user_recs > .10]

        all_users = self.ratings[(self.ratings["movieId"].isin(
            similar_user_recs.index)) & (self.ratings["rating"] > 4)]
        all_user_recs = all_users["movieId"].value_counts(
        ) / len(all_users["userId"].unique())
        rec_percentages = pd.concat([similar_user_recs, all_user_recs], axis=1)
        rec_percentages.columns = ["similar", "all"]
        rec_percentages["score"] = rec_percentages["similar"] / \
            rec_percentages["all"]

        rec_percentages = rec_percentages.sort_values("score", ascending=False)

        return rec_percentages.head(10).merge(self.movies, left_index=True, right_on="movieId")[["score", "title", "genres"]]
