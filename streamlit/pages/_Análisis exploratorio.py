import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly_express as px
import plotly.graph_objects as go
import plotly.figure_factory as ff

st.set_page_config(page_title="APP TITANIC", layout="centered",page_icon="🚢")

df0 = pd.read_csv(r"/Users/laura/Desktop/Upgrade Hub/DataAnalytics/Contenidos/Modulo1/13_Trabajo_Modulo_1/streamlit/datos/titanic_preprocessed.csv")

st.title("Análisis exploratorio de los datos")

st.markdown("<h5 style=>Distribución de pasajeros por sexo</h5>", unsafe_allow_html=True)


def recode_embarked(port):
    if port == 'S':
        return 'Southampton'
    elif port == 'Q':
        return 'Queenstown'
    else:
        return 'Cherbourg'

df0['Embarked'] = df0['Embarked'].apply(recode_embarked)

col1,col2 = st.columns(2)

with col1:
    data=pd.DataFrame(df0['Sex'].value_counts())
    st.bar_chart(data=data, x=data.index.item, y='Sex', use_container_width=True)
    
with col2:
    filtro_sexo = st.sidebar.selectbox("Sexo", df0["Sex"].unique())

    if filtro_sexo:
        st.dataframe(df0.loc[df0["Sex"]==filtro_sexo])
        

st.markdown("<h5 style=>Distribución de pasajeros en función de su edad y la clase en la que viajan</h5>", unsafe_allow_html=True)

fig2 = px.scatter_3d(df0, x='PassengerId', y='Pclass', z='Age', color='Age')
st.plotly_chart(fig2, theme = None, use_container_width=True)


st.markdown("<h5 style=>Distribución de precios de billete según la clase en la que se viaja</h5>", unsafe_allow_html=True)

col1,col2 = st.columns(2)

filtro_fare = st.slider("Precio del billete", min_value= df0["Fare"].min(), max_value = df0["Fare"].max(), value = (df0["Fare"].min(),df0["Fare"].max()))

with col1:
    
    if filtro_fare:
        data = pd.DataFrame(df0.loc[df0['Fare'].between(filtro_fare[0],filtro_fare[1]), ['Fare', 'Pclass']])
        st.dataframe(data)
    
with col2:
    
    if filtro_fare:
        data = pd.DataFrame(df0.loc[df0['Fare'].between(filtro_fare[0],filtro_fare[1]), ['Fare', 'Pclass']])
        fig3 = px.scatter(data, x='Pclass', y='Fare')
        st.plotly_chart(fig3, theme = None, use_container_width = False)
