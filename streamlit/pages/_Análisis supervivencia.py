import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly_express as px
import plotly.graph_objects as go
import altair as alt

st.set_page_config(page_title="APP TITANIC", layout="centered",page_icon="🚢")

st.title("Análisis de supervivencia")


df0 = pd.read_csv(r"/Users/laura/Desktop/Upgrade Hub/DataAnalytics/Contenidos/Modulo1/13_Trabajo_Modulo_1/streamlit/datos/titanic_preprocessed.csv")



st.markdown("<h5 style=>Porcentajes de pasajeros supervivientes o no según su edad</h5>", unsafe_allow_html=True)

def recode_age(age):
    if 0 < age < 1:
        return 'Bebé (<1 año)'
    elif 1 <= age < 10:
        return 'Niñ@ (1–9 años)'
    elif 10 <= age < 19:
        return 'Adolescente (10–18 años)'
    elif 19 <= age < 60:
        return 'Adult@ (10–59 años)'
    else:
        return 'Mayor (>60 años)'

def recode_embarked(port):
    if port == 'S':
        return 'Southampton'
    elif port == 'Q':
        return 'Queenstown'
    else:
        return 'Cherbourg'

df0['Embarked'] = df0['Embarked'].apply(recode_embarked)

def recode_survived(option):
    if option == 0:
        return 'Fallecido'
    else:
        return 'Superviviente'

df0['Survived'] = df0['Survived'].apply(recode_survived)

col1,col2 = st.columns(2)

#filtro_survived = st.sidebar.selectbox('Supervivientes', df0['Survived'].unique())

filtro_survivedpclass = st.sidebar.radio('Filtro supervivencia',['Fallecido','Superviviente'])

with col1 : 
    
    if filtro_survivedpclass == 'Superviviente':
        df0.sort_values('Age')
        df0['Grupo de edad'] = df0['Age'].apply(recode_age)
        grupoedad_count = pd.DataFrame(df0.loc[df0['Survived'] == 'Superviviente', ['Grupo de edad']].value_counts(), columns=['Personas'])
        grupoedad_count.reset_index(level=0, inplace = True)
        st.dataframe(grupoedad_count)

    else:
        
        df0.sort_values('Age')
        df0['Grupo de edad'] = df0['Age'].apply(recode_age)
        grupoedad_count = pd.DataFrame(df0.loc[df0['Survived'] == 'Fallecido', ['Grupo de edad']].value_counts(), columns=['Personas'])
        grupoedad_count.reset_index(level=0, inplace = True)
        st.dataframe(grupoedad_count)

with col2:
    if filtro_survivedpclass == 'Superviviente':
        df0.sort_values('Age')
        df0['Grupo de edad'] = df0['Age'].apply(recode_age)
        grupoedad_count = pd.DataFrame(df0.loc[df0['Survived'] == 'Superviviente', ['Grupo de edad']].value_counts(), columns=['Personas'])
        grupoedad_count.reset_index(level=0, inplace = True)
        fig = px.pie(grupoedad_count, values=grupoedad_count['Personas'], names='Grupo de edad')
        plt.title('Fallecidos')
        st.plotly_chart(fig)
    else:
        df0.sort_values('Age')
        df0['Grupo de edad'] = df0['Age'].apply(recode_age)
        grupoedad_count = pd.DataFrame(df0.loc[df0['Survived'] == 'Fallecido', ['Grupo de edad']].value_counts(), columns=['Personas'])
        grupoedad_count.reset_index(level=0, inplace = True)
        fig = px.pie(grupoedad_count, values=grupoedad_count['Personas'], names='Grupo de edad')
        plt.title('Supervivientes')
        st.plotly_chart(fig)



st.markdown("<h5 style=>Distribución de pasajeros en función la clase en la que viajan y supervivencia</h5>", unsafe_allow_html=True)





data = df0.groupby(['Survived'])['Pclass'].value_counts().to_frame()
px.data.tips()
fig1 = px.histogram(data, x=data.index.get_level_values(1), y="Pclass",
             labels={"value": "Pclass", "count": "count"},
             color=data.index.get_level_values(0), barmode='group',
             height=400,
             color_discrete_map = {0:'blue',1:'purple'}).update_layout(
    xaxis_title= "Pclass",yaxis_title="count")
st.plotly_chart(fig1)


st.markdown("<h5 style=>Distribución de pasajeros en función del tamaño de su familia a bordo y supervivencia</h5>", unsafe_allow_html=True)


df0['Tamaño de la familia'] = df0['SibSp']+df0['Parch']+1

data = df0.groupby(['Survived'])['Tamaño de la familia'].value_counts().to_frame().sort_index()
px.data.tips()
fig1 = px.histogram(data, x="Tamaño de la familia", y=data.index.get_level_values(1),
             labels={"value": "count", "count": "Tamaño de la familia"},
             color=data.index.get_level_values(0), barmode='group',
             height=400,
             range_x= ["1","11"],
             orientation = 'h').update_layout(
    xaxis_title= "count", yaxis_title="Tamaño de la familia").update_yaxes(type = 'category', )
st.plotly_chart(fig1)