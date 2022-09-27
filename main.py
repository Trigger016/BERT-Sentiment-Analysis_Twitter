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

st.title("Twitter Sentiment Analysis (MBKM)")
st.write("DWhat dop you guys think about MBKMl? 🛎️")
st.write("Well... checking all the review on twitter will be much of an issue, let BERT do it for you! 😆")
st.write("How about this, you put the review down below and BERT will think the answer! 😉")

review = st.text_area(
    label="Input Text Here...",
    help="Input your (or your client's) review here, then click anywhere outside the box."
)

if review != "":
    predict, a = text_input(review)

    st.subheader("BERT thinkingg......")

    if predict == "positive":
        st.write(f"YAY! It's a positive review 🥰🥰. BERT think this is {a} accurate")
    elif predict == "negative":
        st.write(f"NOOOO! It's a negative review 😱😱. BERT think this is {a} accurate")
    else:
        st.write(f"WELL! its not bad")