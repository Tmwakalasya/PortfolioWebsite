import streamlit as st
import pandas
st.set_page_config(layout="wide")
col1,col2= st.columns(2)
with col1:
    st.image("images/picture.jpg")
with col2:
    st.title("Tuntufye Mwakalasya")
    content = """Greetings! I'm currently a freshman at FIU pursuing a Bachelor of Science in Computer Science, 
    with a passion for problem-solving and an intuitive mindset. 
    I'm always open to new learning opportunities and enjoy exploring a diverse range of topics, 
    such as Math, AI, Technology, and quantitative finance."""
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




