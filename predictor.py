from transformers import BertTokenizer
import torch
import torch.nn.functional as func
import streamlit as st

@st.cache(allow_output_mutation=True)
def loading(): 
    # Model and Tokenizer loading
    tokenizer = BertTokenizer.from_pretrained("./model/tokenizer/")
    model = torch.load("./model/bert-twitter_model.h5", map_location=torch.device('cpu'))
    model.eval()

    # variables
    i2w = {
        0 : "positive",
        1 : "neutral",
        2 : "negative"
    }
    return model, tokenizer, i2w

# define function
def prediction(model, text, index_label, tokenizer):
    
    token = tokenizer.encode(text)
    tensor_token = torch.LongTensor(token).view(1, -1).to(model.device)
    logits = model(tensor_token)[0]
    label = torch.topk(logits, k=1, dim=-1)[1].squeeze().item()
    acc = func.softmax(logits, dim=-1).squeeze()[label] * 100


    return index_label[label], acc