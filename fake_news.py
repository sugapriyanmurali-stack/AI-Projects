import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

news_data={
    "text":["Government announces new scheme ",
            "Aliens residuals have been found ",
            "Celebrity says epstein's island is fake",
            "New vaccine have been found",
            "Drinking alcohol increases your IQ"],
    "label":["Real","Fake","Fake","Real","Fake"]

}
df=pd.DataFrame(news_data)

x=df["text"]
y=df["label"]

vectorizer=CountVectorizer()
x_vectorized=vectorizer.fit_transform(x)

model=MultinomialNB()
model.fit(x_vectorized,y)

print("Ai fake news detector.")
print("...............")

user=input("Enter the news:")
user_vector=vectorizer.transform([user])

prediction=model.predict(user_vector)

print("AI prediction:",prediction[0])