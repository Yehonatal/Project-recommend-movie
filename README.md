
# Project Recommend Movie

This project is a Flask-based web application that provides movie recommendations based on user input. The system uses the TF-IDF vectorizer and cosine similarity to find similar movie titles and user ratings to provide personalized recommendations.

## Features

- **Movie Search:** Users can search for movies by title.
- **Recommendations:** Provides a list of recommended movies based on the selected movie's title and user ratings.

## Installation

To run this project locally, follow these steps:

1. **Clone the repository:**

   ```bash
   git clone <repository-url>
   cd movie-recommendation-app
   ```

2. **Download the dataset and add it to the data folder**
   - Dataset : <https://files.grouplens.org/datasets/movielens/ml-25m.zip>

3. **Set up the virtual environment:**

   ```bash
   python3 -m venv venv
   ```

4. **Activate the virtual environment:**

   On macOS/Linux:

   ```bash
   source venv/bin/activate
   ```

   On Windows:

   ```bash
   venv\Scripts\activate
   ```

5. **Install the dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Run the Flask app:**

   ```bash
   python app.py
   ```

   Open your web browser and go to `http://127.0.0.1:5000/`.
