import pandas as pd
import numpy as np
import difflib
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

movies_data = pd.read_csv('/content/movies.csv')

# Getting the movie name from the user
movie_name = input("Enter your favorite movie name: ")

# Listing all the movies with similar titles
list_of_titles = movies_data['title'].tolist()

# Finding the closest match of the movie name given by the user
find_close_match = difflib.get_close_matches(movie_name, list_of_titles)

# Now I want only one match not more than that [Finding close match]
close_match = find_close_match[0]

# Find index of the movie with title
index_of_movie = movies_data[movies_data.title == close_match]['index'].values[0]

# Using TfidfVectorizer to convert movie titles into numerical feature vectors
tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix = tfidf_vectorizer.fit_transform(movies_data['title'])

# Compute cosine similarity matrix
similarity = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Getting the list of similarity score of all movies with respect to our input
similarity_score = list(enumerate(similarity[index_of_movie]))

# Sort the movies based on their similarity score
sort_similar_movies = sorted(similarity_score, key=lambda x: x[1], reverse=True)

# Print the name of similar movies based on the index
print("Movies Suggested for you: \n")
i = 1
for movie in sort_similar_movies:
    index = movie[0]
    title_from_index = movies_data[movies_data.index == index]['title'].values[0]
    if i < 30:
        print(i, '.', title_from_index, sep='')
        i += 1
