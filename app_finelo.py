import pandas as pd
import streamlit as st
import plotly.express as px


st.set_page_config(page_title="Finnish elo",page_icon=":soccer:") #, layout="wide") #page_icon=":bar_chart:"

@st.cache
def get_data():
    ranking = pd.read_csv('ranking.csv', index_col=0)
    hist=pd.read_csv('hist.csv', index_col=0, parse_dates=True)
    return ranking, hist



hist_graph=st.container()
table = st.container()


with hist_graph:
    st.title('Finnish football elo')
    ranking, hist=get_data()
    teams = st.multiselect('Teams', ranking.index,
                           default=['KuPS', "HJK", 'FC Honka','Inter Turku','SJK Seinäjoki' ])
    fig = px.line(hist[teams][280:])
    fig.update_layout(xaxis_rangeslider_visible=True)
    st.write(fig)
    
with table:
    st.subheader('Ranking')
    ranking, hist=get_data()

    
    st.table(ranking.style.format("{:7.0f}"))
    st.text('Last update: 02/06/2022')
    st.text('Data from sportscore api')
