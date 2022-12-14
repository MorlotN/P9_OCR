# Import relevant libraries
import requests
import json
import streamlit as st
import os
import pandas as pd
# Set the URL of the Azure function
# urlazure = "https://p9mycontentnmo.azurewebsites.net/api/My_content"
azure_url = "https://p9mycontentnmo.azurewebsites.net/api/My_content"
click = pd.read_csv("https://github.com/MorlotN/P9_mycontentnmo/releases/download/First_P9_tag/clicks.csv")
# for example : azure_url = "https://netflix_recommendations.azurewebsites.net/api/get_recommandations/"



# id_user = st.selectbox('Sélcetionne ton id',range(0,click.user_id.max())) 
id_user = st.text_input('Entre ton id compris entre 0 et {}'.format(click.user_id.max())) 


# Set the parameters of the request
request_params = {"user_id":id_user}

# Send the request to the Azure function
if request_params['user_id'] == "":
    request_params = {"user_id":0}
if request_params:
    r = requests.post(azure_url, params=request_params)
    
    # Grab the recommendations as a Python dictionary
    recommendations_dict = json.loads(r.content.decode())
    st.write("Pour le User n°{} nous recommendons de lire les articles: ".format(id_user))
    for reco in recommendations_dict['recommendations']:
        st.write(" {} ".format(reco))
