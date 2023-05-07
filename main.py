import streamlit as st
st.set_page_config(layout="wide")
col1,col2 = st.columns(2)
with col1:
    st.image("images/picture.jpg")
with col2:
    st.title("Tuntufye Mwakalasya")
    content = """I am a freshman 
at FIU pursuing a BS in Computer Science. 
I enjoy problem-solving and am also very intuitive I am always open to learning new things and 
I enjoy exploring a variety of topics that interest Me such as Math, AI, Technology, and quantitative finance."""
    st.info(content)