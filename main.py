from re import L
from predictor import loading, prediction
import streamlit as st

st.set_page_config(
    page_title="BERT Twitter Sentiment Analysis",
    page_icon="📘"
)

with st.spinner("Loading BERT, please kindly wait .... 😄😄😄"):
    model, tokenizer, index_label = loading()

@st.cache
def text_input(text):
    label_res, acc = prediction(model, text, index_label, tokenizer)
    return label_res, acc

# def test_button():
#     if review != "":
#         predict, a = text_input(review)
#     else:
#         st.write("Did you write anything🤨🤨🤨")

#     st.subheader("BERT thinkingg......")

#     if predict == "positive":
#         st.write(f"YAY! It's a positive review 🥰🥰. BERT think this is {a} accurate")
#     elif predict == "negative":
#         st.write(f"NOOOO! It's a negative review 😱😱. BERT think this is {a} accurate")
#     elif predict == "neutral":
#         st.write(f"WELL... its not bad")
    

st.title("Twitter Sentiment Analysis Magang Merdeka Kampus Merdeka (MBKM)")
st.write("What do you guys think about MBKM? 🛎️")
st.write("Well... checking all the review on twitter will be much of an issue aint it? let BERT do it for you! 😆")
st.write("So how about this, you put the review down below and BERT will think of an answer! 😉")

review = st.text_area(
    label="Input Text Here...",
    help="Input your tweets here, then click RUN!!! button, sit and see the magic happens!"
)

if st.button(label="RUN!!!"):
    if review != "":
        predict, a = text_input(review)
    else:
        st.write("Did you write anything🤨🤨🤨")

    st.subheader("BERT thinkingg......")

    if predict == "positive":
        st.write(f"YAY! It's a positive review 🥰🥰. BERT think this is {a} accurate")
    elif predict == "negative":
        st.write(f"NOOOO! It's a negative review 😱😱. BERT think this is {a} accurate")
    elif predict == "neutral":
        st.write(f"WELL... its not bad")
else:
    st.write("BERT Iddling...")


# if review != "":
#     predict, a = text_input(review)

#     st.subheader("BERT thinkingg......")

#     if predict == "positive":
#         st.write(f"YAY! It's a positive review 🥰🥰. BERT think this is {a} accurate")
#     elif predict == "negative":
#         st.write(f"NOOOO! It's a negative review 😱😱. BERT think this is {a} accurate")
#     elif predict == "neutral":
#         st.write(f"WELL... its not bad")
#     else:
#         st.write("Did you write anything🤨🤨🤨")