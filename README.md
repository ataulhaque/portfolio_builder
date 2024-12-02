# Portfolio builder

This is Ataul Haque's Portfolio on Streamlit. 

## Contents

- LinkedIn Badge : [LinkedIn Profile?](https://www.linkedin.com/in/ataulhaque/). 
- Skills & Tools: Used streamlit buttons & columns features
- Education : Plotly(library for visualization) table
- Research Paper detailed brief description : streamlit images, streamlit metrics, streamlit expander & plotly.express grouped barplot
- Achievements : streamlit markdown (great to embed HTML codes)
- ML models integrated : Vanilla & Cycle GAN built using tensorflow

## Files description
* cyclegan/ : weights for cyclegan model used for image translation
* vanilla_gan/ : weights for vanilla gan used
* images/ : images used for research paper section
* pdf/ : pdfs available for downloading on portfolio
* constant.py : File with all static data used. 
* cycle.py : cycle_gan models 
* vanilla_gan.py: vanilla_gan models
* requirements.txt : requirements file generated using [pipreqs](https://pypi.org/project/pipreqs/)
* graph_builder.py : Daily routine graph using graphviz
* timeline.json : Json file used by streamlit_timeline for career snapshot

## How to deploy using Streamlit?
* Once confirm your app runds fine on localhost. Check using 
```
streamlit run streamlit_app.py 
```
* Create requirements.txt. 
* Push repo to github.
* Sign in https://streamlit.io/ using the same mail as for github account where code is pushed (for ease)
* Fill in the info & click deploy on the ![Deployment screen](https://user-images.githubusercontent.com/31255225/147195886-a7f69e07-ac50-4fe4-af3f-48e953c983fa.PNG) 


