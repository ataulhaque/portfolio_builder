import pandas as pd
import streamlit as st
import os

st.header('My Blogs')
path = os.getcwd()+'/pdfs/my_blogs.csv'
df = pd.read_csv(path)
df['category1'] = df.apply(lambda x:x['category1'].split('|'),axis=1)
df = df.explode('category1')
grouped = df.groupby(['category1']).agg(list)
grouped['total'] = grouped['url'].transform(len)
grouped = grouped.sort_values(by='total',ascending=False)
for x,y in grouped.iterrows():
    with st.expander(x.upper()):
        blog = {a:b for a,b in zip(y['title'],y['url'])}
        for a,b in blog.items():
            st.markdown("""<a href={}><b><u>{}</b></u></a>""".format(b,a),unsafe_allow_html=True)