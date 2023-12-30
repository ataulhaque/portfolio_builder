
import streamlit as st 
from constant import *
import numpy as np 
import pandas as pd
from PIL import Image
from streamlit_timeline import timeline
import plotly.express as px
import plotly.figure_factory as ff
import requests
import re
import plotly.graph_objects as go
import io
import matplotlib.pyplot as plt
import streamlit.components.v1 as components
from graph_builder import *
#import tensorflow as tf
from streamlit_player import st_player
from streamlit_lottie import st_lottie

st.set_page_config(page_title="Ataul Haque's Portfolio",
                   layout="wide",
                   page_icon='👨‍🔬'
                   )

def load_lottieurl(url):
    r =requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

#--ASSETS--
coding_animation = load_lottieurl("https://lottie.host/0e57b408-5eee-4f98-957c-32f7bfdccefd/UvF6HC89gA.json")

st.sidebar.markdown(info['Stackoverflow_flair'],unsafe_allow_html=True)
with st.container():
    st.subheader('Summary')
    st.write(info['Brief'])
    st.write("[Read More >](https://www.linkedin.com/in/ataulhaque/)")

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
            """
            This is my Professional Career Snapshot of what I do. To know more about me, do contact me through my [LinkedIn](https://www.linkedin.com/in/ataulhaque/) account. 
            """
        )
        st.write("[WhatsApp ⌘](https://wa.me/919953112091)")

    with right_column:
        st_lottie(coding_animation, height=300, key="coding")

st.subheader('Career snapshot')
    
with st.spinner(text="Building line"):
    with open('timeline.json', "r") as f:
        data = f.read()
        timeline(data, height=500)


st.subheader('Skills & Tools ⚒️')
def skill_tab():
    rows,cols = len(info['skills'])//skill_col_size,skill_col_size
    skills = iter(info['skills'])
    if len(info['skills'])%skill_col_size!=0:
        rows+=1
    for x in range(rows):
        columns = st.columns(skill_col_size)
        for index_ in range(skill_col_size):
            try:
                columns[index_].button(next(skills))
            except:
                break
with st.spinner(text="Loading section..."):
    skill_tab()

st.write("---")
st.subheader('Education 📖')
fig = go.Figure(data=[go.Table(
    header=dict(values=list(info['edu'].columns),
                fill_color='darkgrey',
                align='left',height=50,font_size=20),
    cells=dict(values=info['edu'].transpose().values.tolist(),
               fill_color='cyan',
               align='left',height=40,font_size=15))])

fig.update_layout(width=750, height=400)
st.plotly_chart(fig)

def plot_bar():
    
    st.info('Comparing Brute Force approach with the algorithms')
    temp1 = rapid_metrics.loc[['Brute-Force_Printed','printed'],:].reset_index().melt(id_vars=['category'],value_vars=['precision','recall','f1_score'],var_name='metrics',value_name='%').reset_index()
    
    temp2 = rapid_metrics.loc[['Brute-Force_Handwritten','handwritten'],:].reset_index().melt(id_vars=['category'],value_vars=['precision','recall','f1_score'],var_name='metrics',value_name='%').reset_index()
    
    cols = st.columns(2)
    
    fig = px.bar(temp1, x="metrics", y="%", 
             color="category", barmode = 'group')
     
    cols[0].plotly_chart(fig,use_container_width=True)
    
    fig = px.bar(temp2, x="metrics", y="%", 
             color="category", barmode = 'group')
    cols[1].plotly_chart(fig,use_container_width=True)
    
    

def image_and_status_loader(image_list,index=0):
    if index==0:
        img = Image.open(image_list[0]['path'])
        st.image(img,caption=image_list[0]['caption'],width=image_list[0]['width'])
       
    else:
        st.success('C-Cube algorithm for printed prescriptions')
        rapid_metrics.loc[['Brute-Force_Printed','printed'],:].plot(kind='bar')
        cols = st.columns(3)
        for index_,items in enumerate(image_list[0]):
            cols[index_].image(items['path'],caption=items['caption'],use_column_width=True)
     
        
        st.success('3 step filtering algorithm for handwritten algorithms')
        cols = st.columns(3)
        for index_,items in enumerate(image_list[1]):
            cols[index_].image(items['path'],caption=items['caption'],use_column_width=True)
        
        plot_bar()
        
st.subheader('Daily routine as AI/ML Researcher')
st.graphviz_chart(graph)

st.sidebar.caption('Wish to connect?')
st.sidebar.write('📧: atauldilse@gmail.com')
pdfFileObj = open('pdfs/CV_Ataul Haque.pdf', 'rb')
st.sidebar.download_button('download resume',pdfFileObj,file_name='CV_Ataul Haque.pdf',mime='pdf')



        

        
        
    
    
