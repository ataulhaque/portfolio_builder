import pandas as pd
import graphviz as graphviz

edu = [['B.Tech','IT','2011','GITA, Bhubaneswar'],['12th','Science','2006','BEMS, Belpahar'],['10th','-','2004','DAVPS Bandhbahal']]

info = {'name':'Ataul Haque', 'Brief':'Associate Consultant at [TCS](https://tcs.com/) with 10+ years of professional experience looking out to solve complex business problems; Experienced in developing end to end feature rich deployable products in BFSI domain; Love to learn new things. Working on GenAI usecases at TCS right now !! ','photo':{'path':'abc.jpg','width':150}, 'Mobile':'9953112091','Email':'atauldisle@gmail.com','Medium':'https://namasteindia.info/p/about-us.html','City':'Bengaluru, Karnataka','Stackoverflow_flair':'''<a href="https://stackoverflow.com/users/4569149/ataul-haque"><img src="https://lh5.googleusercontent.com/-D55EVhSi3Dg/AAAAAAAAAAI/AAAAAAAAXGg/WgAOsaeG-2Y/photo.jpg?sz=256" width="150" height="80"  alt="profile for Ataul Haque at Stack Overflow, Q&amp;A for professional and enthusiast programmers" title="profile for Ataul Haque at Stack Overflow, Q&amp;A for professional and enthusiast programmers"></a>''','edu':pd.DataFrame(edu,columns=['Qualification','Stream','Year','Institute']),'skills':['Python','Perl','Unix Shell Scripting','Generative AI','AI-ML','Vertex-AI','Jenkins','TeamCity','Git','Perforce','Jupyter Notebook','Colaboratory','SVN','Streamlit','PySpark','Tensorflow','Langchain','GenAI'],'achievements':['GenAI writer @ Blogger with 10+ blogs', 'Founder member of ITUAIEI - A Union for IT Professionals in India']}

models = ('Fashion MNIST samples using GAN','Cycle GAN for Image Translation')
cycle_models = ('Winter to Summer','Summer to Winter')
cycle_model_url = {cycle_models[0]:['images/winter1.jpg','images/winter2.jpg','images/winter3.jpg'],cycle_models[1]:['images/summer1.jpg','images/summer2.jpg','images/summer3.jpg']}

rpa_metrics = pd.DataFrame([['Overall',66.4, 72.5],['printed rx',54.6, 64.6],['handwritten',67.3,73.3]], columns=['category','ds','non-ds'])
rapid_metrics = pd.DataFrame([['printed',91.6,70,79.4],['handwritten',21.1,34.7,26.2],['Brute-Force_Printed',29.9,82.7,41.8],['Brute-Force_Handwritten',0.2,62,0.3]],columns=['category','precision','recall','f1_score'])
rapid_metrics = rapid_metrics.set_index(['category'])

skill_col_size = 5
embed_component= {'linkedin':"""<script src="https://platform.linkedin.com/badges/js/profile.js" async defer type="text/javascript"></script>
        <div class="badge-base LI-profile-badge" data-locale="en_US" data-size="medium" data-theme="light" data-type="VERTICAL" data-vanity="mehulgupta7991" data-version="v1"><a class="badge-base__link LI-simple-link" href="https://in.linkedin.com/in/mehulgupta7991?trk=profile-badge"></a></div>""", 'medium':"""<div style="overflow-y: scroll; height:500px;"> <div id="retainable-rss-embed" 
data-rss="https://medium.com/feed/retainable,https://medium.com/feed/data-science-in-your-pocket"
data-maxcols="3" 
data-layout="grid"
data-poststyle="inline" 
data-readmore="Read the rest" 
data-buttonclass="btn btn-primary" 
data-offset="0"></div></div> <script src="https://www.twilik.com/assets/retainable/rss-embed/retainable-rss-embed.js"></script>"""}



