from flask import Flask, request, jsonify, render_template
from models.recommendation_model import MovieRecommender

app = Flask(__name__)

recommender = MovieRecommender('data/movies.csv', 'data/ratings.csv')


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/search', methods=['POST'])
def search():
    data = request.json
    title = data.get('title')
    results = recommender.search(title)
    return jsonify(results.to_dict(orient='records'))


@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.json
    movie_id = data.get('movie_id')
    recommendations = recommender.find_similar_movies(movie_id)
    return jsonify(recommendations.to_dict(orient='records'))


if __name__ == '__main__':
    app.run(debug=True)
