import streamlit as st
from constant import *
import numpy as np
import pandas as pd
from PIL import Image
from streamlit_timeline import timeline
import plotly.express as px
import plotly.graph_objects as go
import requests
import matplotlib.pyplot as plt
from streamlit_player import st_player
from streamlit_lottie import st_lottie
import google.generativeai as genai

# Set page configuration
st.set_page_config(page_title="Ataul Haque's Portfolio", layout="wide", page_icon='👨‍🔬')

@st.cache_resource
def load_model() -> genai.GenerativeModel:
    model = genai.GenerativeModel('gemini-pro')
    return model

# Configure the model
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
model = load_model()

# Load Lottie animation
def load_lottieurl(url):
    r = requests.get(url)
    return r.json() if r.status_code == 200 else None

coding_animation = load_lottieurl("https://lottie.host/0e57b408-5eee-4f98-957c-32f7bfdccefd/UvF6HC89gA.json")

# Sidebar
st.sidebar.title("Connect with Me")
st.sidebar.write('📧: atauldilse@gmail.com')
pdfFileObj = open('pdfs/CV_Ataul Haque.pdf', 'rb')
st.sidebar.download_button('Download Resume', pdfFileObj, file_name='CV_Ataul Haque.pdf', mime='application/pdf')

# Main content
st.title("Welcome to My Portfolio")
st.markdown(info['Stackoverflow_flair'], unsafe_allow_html=True)

# Summary Section
with st.container():
    st.subheader('Summary')
    st.write(info['Brief'])
    st.write("[Read More >](https://www.linkedin.com/in/ataulhaque/)")

# What I Do Section
with st.container():
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I Do")
        st.write("##")
        st.write("This is my Professional Career Snapshot. To know more about me, contact me through my [LinkedIn](https://www.linkedin.com/in/ataulhaque/).")
        st.write("[WhatsApp ⌘](https://wa.me/919953112091)")
    with right_column:
        st_lottie(coding_animation, height=300, key="coding")

# Career Snapshot Section
st.subheader('Career Snapshot')
with st.spinner(text="Building timeline..."):
    with open('timeline.json', "r") as f:
        data = f.read()
        timeline(data, height=500)

# Skills & Tools Section
st.subheader('Skills & Tools ⚒️')
def skill_tab():
    rows, cols = len(info['skills']) // skill_col_size, skill_col_size
    skills = iter(info['skills'])
    if len(info['skills']) % skill_col_size != 0:
        rows += 1
    for x in range(rows):
        columns = st.columns(skill_col_size)
        for index_ in range(skill_col_size):
            try:
                columns[index_].button(next(skills))
            except StopIteration:
                break

with st.spinner(text="Loading skills..."):
    skill_tab()

# Education Section
st.subheader('Education 📖')
fig = go.Figure(data=[go.Table(
    header=dict(values=list(info['edu'].columns), fill_color='cyan', align='left', height=50, font_size=20),
    cells=dict(values=info['edu'].transpose().values.tolist(), fill_color='darkgrey', align='left', height=40, font_size=15)
)])
fig.update_layout(width=750, height=400)
st.plotly_chart(fig)

# Daily Routine Section
st.subheader('Daily Routine:')
st.graphviz_chart(graph)

# Chat Interface
st.subheader('Chat with Me')
if "messages" not in st.session_state:
    st.session_state["messages"] = []

for message in st.session_state["messages"]:
    role = message["role"]
    content = message["content"]
    with st.chat_message(role):
        st.markdown(content)

st.info("Write your prompt/query below: 👇")
prompt = st.chat_input("You:")

if prompt:
    st.session_state["messages"].append({"role": "user", "content": prompt})
    with st.chat_message("assistant"):
        response = model.generate_content(prompt)
        st.markdown(response.text)
        st.session_state["messages"].append({"role": "assistant", "content": response})