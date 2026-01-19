# from sklearn.feature_extraction.text import CountVectorizer
# from sklearn.naive_bayes import MultinomialNB

# messages=["Win money now",
#           "Free prize offer",
#           "Call me tomorrrow",
#           "Lets meet for lunch",
#           "Congratulations you have won",
#           "Hello how are you"]
# labels = [1, 1, 0, 0, 1, 0]  # 1 = Spam, 0 = Not Spam

# vectorizer = CountVectorizer()
# X = vectorizer.fit_transform(messages)

# model = MultinomialNB()
# model.fit(X, labels)

# test_message = ["hi how are you .....you have an exciting offer"]
# test_vector = vectorizer.transform(test_message)

# prediction = model.predict(test_vector)

# if prediction[0] == 1:
#     print("Spam Message")
# else:
#     print("Not Spam Message")








from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

message=["have won",
         "Claim this limited time exclusive offer ",
         "Congratulations you have been selected",
         "Hi how are you",
         "Free prize offer ",
         "lets go for lunch",
         "Call me"]
label=[1,1,1,0,1,0,0]
vectorizer=CountVectorizer()
x=vectorizer.fit_transform(message)

model=MultinomialNB()
model.fit(x,label)

test=["you have an exclusive offer"]
test_v=vectorizer.transform(test)

prediction=model.predict(test_v)

if prediction[0]==1:
    print("Spam")
else:
    print("Not spam")
