import streamlit as st
import pickle
import sklearn 

tfidf = pickle.load(open("vectorizer.pkl", "rb"))
model = pickle.load(open("model2.pkl", "rb"))
st.title("Email spam classifier")
sms = st.text_area("Enter your email")
if st.button("predict"):
    vector_input = tfidf.transform([sms])
    result = model.predict(vector_input)[0]
    if result==1:
        st.header("Not spam")
    else:
        st.header("spam")