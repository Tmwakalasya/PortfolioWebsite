import streamlit as st
import pandas

st.set_page_config(layout="wide")
col1, col2 = st.columns(2)
with col1:
    st.image("images/21.png")
with col2:
    st.title("Tuntufye Mwakalasya")
    content = """Greetings! I'm Tuntufye Mwakalasya, currently a freshman at FIU pursuing a Bachelor of Science in Computer Science, 
    with a passion for problem-solving and an intuitive mindset. 
    I'm always open to new learning opportunities and enjoy exploring a diverse range of topics, 
    such as Math,Computer Science, AI, Technology, and quantitative finance."""
    st.info(content)
st.info("Below you can find some of the python projects I have worked on. Feel free to contact me:)")
col4, empty_col, col5 = st.columns([1.5, 0.5, 1.5])
df = pandas.read_csv("venv/data.csv", sep=";")
with col4:
    for index, row in df[:10].iterrows():
        # Iterate through each row in the Dataframe from 1 to 10
        st.header(row["title"])
        st.write(row['description'])
        st.image("images/" + row["image"])
        st.write(f"[Source code]({row['url']})")

with col5:
    # Iterate through each row in the dataframe from to 11 to 20
    st.header(row["title"])
    st.write(row['description'])
    st.image("images/" + row["image"])
    st.write(f"[Source code]({row['url']})")
