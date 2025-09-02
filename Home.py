import streamlit as st

st.set_page_config(page_title="Fake News Detection", layout="centered")

with st.sidebar:
    st.image("Sastra.jpg", width=150)
    st.markdown("### Guide")
    st.markdown("- Dr. Ramkumar K ")

    st.markdown("### Team Members")
    st.markdown("- Ashish Arvind M ")
    st.markdown("- Harishraj T ")
    

st.markdown("""
    <h2 style='text-align: center;'>
        Detection of fake news using deep learning CNN–RNN based methods
    </h2>
""", unsafe_allow_html=True)

st.markdown("""
###### This web application allows you to detect fake news using deep learning models.


### Models Created:
- ##### Convolution Neural Network

- ##### Bidirectional LSTM

- ##### ResNet 


### Word Embeddings used for Preprocessing:
- ##### Word2Vec

- ##### GLoVe

- ##### CfastText

    
""")
