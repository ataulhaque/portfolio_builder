import pandas as pd
import streamlit as st
import os

st.header('My Blogs')
path = os.path.join(os.getcwd(), 'pdfs', 'my_blogs.csv')  # Improved path handling
try:
    df = pd.read_csv(path, encoding='ISO-8859-1')  # Specify encoding to handle special characters
except FileNotFoundError:
    st.error("The file was not found. Please check the path.")  # Error handling for file read
    st.stop()  # Stop execution if the file is not found
except UnicodeDecodeError:
    st.error("There was an error decoding the file. Please check the file encoding.")  # Handle decoding errors
    st.stop()  # Stop execution if there's a decoding error

# Check if 'category1' exists in the DataFrame
if 'category1' not in df.columns:
    st.error("The 'category1' column is missing from the data.")  # Check for column existence
    st.stop()  # Stop execution if the column is missing

df['category1'] = df.apply(lambda x:x['category1'].split('|'),axis=1)
df = df.explode('category1')
grouped = df.groupby(['category1']).agg(list)
grouped['total'] = grouped['url'].transform(len)
grouped = grouped.sort_values(by='total',ascending=False)
for x,y in grouped.iterrows():
    with st.expander(x.upper()):
        blog = {a:b for a,b in zip(y['title'],y['url'])}
        for a,b in blog.items():
            st.markdown("""<a href='{}'><b><u>{}</b></u></a>""".format(b,a),unsafe_allow_html=True)  # Ensure URLs are safe