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
from vanilla_gan import return_decoder
import tensorflow as tf
from cycle_gan import model_loader, preprocess, generate_real, generate_fake, n_batch

st.set_page_config(page_title='mehul gupta\'s career snapshot' ,layout="wide",page_icon=':boy:')


with st.sidebar:
        components.html(embed_component['linkedin'],height=310)

st.sidebar.markdown(info['Stackoverflow_flair'],unsafe_allow_html=True)
st.subheader('Summary')
st.write(info['Brief'])

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
skill_tab()


st.subheader('Education 📖')

fig = go.Figure(data=[go.Table(
    header=dict(values=list(info['edu'].columns),
                fill_color='paleturquoise',
                align='left',height=75,font_size=20),
    cells=dict(values=info['edu'].transpose().values.tolist(),
               fill_color='lavender',
               align='left',height=50,font_size=15))])

fig.update_layout(width=800, height=400)
st.plotly_chart(fig)
st.subheader('Research Papers 📝')

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
        
        

def paper_summary(index):
    st.markdown('<h5><u>'+paper_info['name'][index]+'</h5>',unsafe_allow_html=True)
    with st.expander('See detailed version...'):
        st.caption(paper_info['role'][index]+','+paper_info['year'][index])
        st.write(paper_info['Summary'][index])
        pdfFileObj = open(paper_info['file'][index], 'rb')
        image_and_status_loader(paper_info['images'][str(index)], index)
        if index==0:
            rpa_metrics['time_improvement'] = rpa_metrics['non-ds']-rpa_metrics['ds']
            st.markdown('**Time taken per order involving Rx in seconds** (green indicates improvements from baseline)')
            cols = st.columns(3)
            for index_, row in rpa_metrics.iterrows():
                cols[index_].metric(row['category'],str(row['ds'])+'s',delta=str(round(row['time_improvement'],1))+'s' )
        st.download_button('download paper',pdfFileObj,file_name=paper_info['name'][index],mime='pdf')
    


paper_summary(0)
paper_summary(1)

st.subheader('Achievements 🥇')
achievement_list = ''.join(['<li>'+item+'</li>' for item in info['achievements']])
st.markdown('<ul>'+achievement_list+'</ul>',unsafe_allow_html=True)


st.subheader('Medium Profile ✍️')
page1,page2 = requests.get(info['Medium']), requests.get(info['publication_url'])

followers = re.findall('(\d+) Followers',page1.text)[0]
following = re.findall('(\d+) Following',page1.text)[0]
pub_followers = re.findall('Followers (?:\w+\s+){4}(\d+)',re.sub('\W+',' ', page2.text ))[0]

cols = st.columns(3)
cols[0].metric('Followers',followers)
cols[1].metric('Following',following)
cols[2].metric('Publication followers',pub_followers)

with st.expander('Read my latest blogs here...'):
    with st.spinner(text="Loading blogs.."):
        components.html(embed_component['medium'],height=900)
        
st.subheader('Daily routine as Data Scientist')
st.graphviz_chart(graph)

st.subheader('Time for some ML')
        
selection = st.radio('Choose one of the two models',models)
if selection == models[0]:
    input_ = st.slider('How many random samples you wish to generate?',0,15)
    with st.spinner('loading random samples generated...'):
            noise = tf.random.normal((input_,4),mean=0,stddev=1)
            decoder_v = return_decoder()
            images = iter(decoder_v(noise,training=False))
            row, cols = input_//4,input_%4
            if cols:
                row+=1
            for x in range(row):
                if (x-1)<row:
                    columns = st.columns(4)
                else:
                    columns = st.columns(cols)
                for index_ in range(len(columns)):
                    try:
                        img = next(images)
                    except:
                        break
                    fig,ax = plt.subplots()
                    ax.imshow(img)
                    columns[index_].pyplot(fig)
else:
    
    generator_A_B,generator_B_A = model_loader()
    input_ = st.selectbox('Which transition you wish to try',cycle_models)
    if input_:
            data = []
            for images in cycle_model_url[input_]:
                    response = requests.get(images)
                    img = Image.open(io.BytesIO(response.content))
                    data.append(np.array(img.resize((128,128))))
            st.image(data,caption=[x for x in range(len(cycle_model_url[input_]))],clamp=True,width=200)
            selection = st.multiselect('Choose one/multiple images to transit',[x for x in range(len(cycle_model_url[input_]))])
            if selection:
                    data = [data[int(x)] for x in selection]

                    dataset = tf.data.Dataset.from_tensor_slices({'image':data})
                    dataset = dataset.map(preprocess).batch(n_batch).__iter__()
                    samples,_ = generate_real(next(dataset),n_batch,0)
                    if input_== cycle_models[0]:
                        images,_ = generate_fake(samples, generator_B_A,n_batch,0)
                    else:
                        images,_ = generate_fake(samples, generator_A_B,n_batch,0)
                    cols = st.columns(len(images))
                    images = images.numpy()
                    for x in range(len(images)):
                        fig,ax = plt.subplots()
                        ax.imshow(images[x])
                        cols[x].pyplot(fig,use_column_width=True)

        

        
        
    
    