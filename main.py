import streamlit as st
import pandas
st.set_page_config(layout="wide")
col1,col2= st.columns(2)
with col1:
    st.image("images/picture.jpg")
with col2:
    st.title("Tuntufye Mwakalasya")
    content = """I am a freshman 
at FIU pursuing a BS in Computer Science. 
I enjoy problem-solving and am also very intuitive I am always open to learning new things and 
I enjoy exploring a variety of topics that interest Me such as Math, AI, Technology, and quantitative finance."""
    st.info(content)
st.info("Below you can find some of the python projects. Feel free to contact me")
col4,empty_col,col5 = st.columns([1.5,0.5,1.5])
df = pandas.read_csv("venv/data.csv",sep=";")
with col4:
    for index,row in df.iterrows():
        st.header(row["title"])
        st.write(row['description'])
        st.image("images/" + row["image"])
        st.write(f"[Source code]({row['url']})")

with col5:
    for index,row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row['description'])
        st.image("images/" + row["image"])
        st.write(f"[Source code]({row['url']})")




