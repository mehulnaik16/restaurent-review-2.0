import streamlit as st
import pandas as pd
import numpy as np
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB

nltk.download('stopwords')

# Initialize session state for tracking reviews
if 'positive_reviews' not in st.session_state:
    st.session_state.positive_reviews = 0
if 'total_reviews' not in st.session_state:
    st.session_state.total_reviews = 0

st.title('Sentiment Analysis for Restaurant Reviews')

# Load and preprocess the dataset
dataset = pd.read_csv('Restaurant_Reviews.tsv', delimiter='\t', quoting=3)
corpus = []
ps = PorterStemmer()

for i in range(len(dataset)):
    review = re.sub('[^a-zA-Z]', ' ', dataset['Review'][i])
    review = review.lower()
    review_words = review.split()
    review_words = [word for word in review_words if not word in set(stopwords.words('english'))]
    review = [ps.stem(word) for word in review_words]
    review = ' '.join(review)
    corpus.append(review)

cv = CountVectorizer(max_features=1500)
X = cv.fit_transform(corpus).toarray()
y = dataset.iloc[:, 1].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

classifier = MultinomialNB(alpha=0.1)
classifier.fit(X_train, y_train)

def predict_sentiment(sample_review):
    sample_review = re.sub('[^a-zA-Z]', ' ', sample_review)
    sample_review = sample_review.lower()
    sample_review_words = sample_review.split()
    sample_review_words = [word for word in sample_review_words if not word in set(stopwords.words('english'))]
    final_review = [ps.stem(word) for word in sample_review_words]
    final_review = ' '.join(final_review)
    temp = cv.transform([final_review]).toarray()
    return classifier.predict(temp)

# Streamlit app layout
st.subheader('Enter a review to predict its sentiment')
sample_review = st.text_area('Review Text')

if st.button('Predict Sentiment'):
    if sample_review:
        prediction = predict_sentiment(sample_review)
        st.session_state.total_reviews += 1
        if prediction:
            st.session_state.positive_reviews += 1
            st.write("**POSITIVE REVIEW**")
            print("POSITIVE REVIEW")
        else:
            st.write("**NEGATIVE REVIEW**")
            print("NEGATIVE REVIEW")

        # Calculate and display percentages
        positive_percentage = (st.session_state.positive_reviews / st.session_state.total_reviews) * 100
        negative_percentage = 100 - positive_percentage
        total_reviews=st.session_state.total_reviews
        st.write(f"Total Reviews: {total_reviews}") 
        st.write(f"Positive Reviews: {positive_percentage:.2f}%",f", Count: {st.session_state.positive_reviews}")
        st.write(f"Negative Reviews: {negative_percentage:.2f}%",f", Count: {total_reviews-st.session_state.positive_reviews}")
    else:
        st.write("Please enter a review text.")

# Optionally, show the dataset
if st.checkbox('Show raw data'):
    st.subheader('Dataset')
    st.write(dataset)
