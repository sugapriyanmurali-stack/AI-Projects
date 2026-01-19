from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

movies = {
    "Avengers": "action superhero",
    "Titanic": "romantic drama",
    "Inception": "action sci-fi thriller",
    "Notebook": "romantic love",
    "Interstellar": "sci-fi space",
    "John Wick": "action thriller"
}

movie_names = list(movies.keys())
movie_desc = list(movies.values())

vectorizer = CountVectorizer()
vectors = vectorizer.fit_transform(movie_desc)

similarity = cosine_similarity(vectors)

user_input=input("Enter movie type you like: ")

user_vector=vectorizer.transform([user_input])
scores=cosine_similarity(user_vector,vectors)

index=scores.argmax()
print("Recommended Movies:",movie_names[index])