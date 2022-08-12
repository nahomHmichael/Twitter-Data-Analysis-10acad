from select import select
import streamlit as st
import pandas as pd
import matplotlib as plt

import numpy as np


def side_bar():
    st.title('Twitter Tweets Analysis')

    
    

    data=pd.read_pickle('.trained_model/cleaned_tweet.pkl')


    if st.checkbox("Show Data"):
        st.write(data.head(50))

    

    

    
    tweets=st.sidebar.radio('Sentiment Type',('positive','negative','neutral'))
    

    visualizers=st.sidebar.radio('Visualization of tweets',['Bar Chart','Pie Chart'],key=1)

    if tweets == "positive":
        polarity=st.write(data.query('polarity>0')[['original_text']].head(5))
    elif tweets == "negative":
        polarity=st.write(data.query('polarity<0')[['original_text']].head(5))
    else:
        polarity=st.write(data.query('polarity==0')[['original_text']].head(5))


        

        # if visualizers=="Bar Chart":
        #     fig= px.bar(sentiment, x='Sentiment', y='Tweets', color = "Tweets" ,height =500)


    
