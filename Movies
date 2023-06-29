import pandas as pd
import numpy as np
import difflib                                                  # If the user makes errors while typing the movie name, this lib is used to get the closest match of the movie
from sklearn.metrics.pairwise import cosine_similarity          # Used to get similarities
from sklearn.feature_extraction.text import TfidfVectorizer     # Numerical feature vectors

movies_data = pd.read_csv('/content/movies.csv')               #Upload your Data Set

#Selecting only the required columns columns
selected_features = ['genres','keywords','tagline','cast','director']

#Replacing null values
for feature in selected_features:
  movies_data[feature] = movies_data[feature].fillna('')

#Combinig all the 5 selected features -> Concanating process
combined_features = movies_data['genres']+movies_data['keywords']+movies_data['tagline']+movies_data['cast']+movies_data['director']

#Converting the text data to feature vectors
vectorizer = TfidfVectorizer()
feature_vectors = vectorizer.fit_transform(combined_features)

#To get the similarities scores using cosine similarity
similarity = cosine_similarity(feature_vectors)



#Enter the movie
movie_name = input("Enter your favorite movie name: ")

#Listing all the movies with the similar title
list_of_titles = movies_data['title'].tolist()

#Finidng the close match of the movie name given by the user
find_close_match = difflib.get_close_matches(movie_name, list_of_titles)

# Now I want only one match not more than that [Finding close match]
close_match = find_close_match[0]

#Find index of the movie with title
index_of_movie = movies_data[movies_data.title == close_match]['index'].values[0]

# Getting the list of similarity score of all movies with respect to our input
similarity_score = list(enumerate(similarity[index_of_movie]))

#Sort the movies based on their similarity score
sort_similar_movies = sorted(similarity_score, key = lambda x:x[1], reverse = True)

#Print the name of similar movies based on the index
print("Movies Suggested for you: \n")
i = 1
for movie in sort_similar_movies:
  index = movie[0]
  titel_from_index = movies_data[movies_data.index==index]['title'].values[0]
  if(i<30):
    print(i,'.',' ',titel_from_index,sep='')
    i = i + 1
