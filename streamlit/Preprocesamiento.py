#Librerías
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly_express as px #(hay que instalarlo aparte en la terminal :: conda install -c plotly plotly_express)
import plotly.graph_objects as go #(hay que instalar plotly, este de graph_objects en concreto noo existe para conda)
import plotly as pt




#Configuración de página, puede ser "centered" o "wide"

st.set_page_config(page_title="APP TITANIC", layout="centered",page_icon="🚢")


#Creación de columnas y logotipo
st.image(r"/Users/laura/Desktop/Upgrade Hub/DataAnalytics/Contenidos/Modulo1/13_Trabajo_Modulo_1/streamlit/images/Titanic.jpg", width = None, caption='Hundimiento del RMS Titanic (Untergang der Titanic, a 1912 illustration by Willy Stöwer)')

st.title("Conjunto de datos: TITANIC")


df_titanic = pd.read_csv(r"/Users/laura/Desktop/Upgrade Hub/DataAnalytics/Contenidos/Modulo1/13_Trabajo_Modulo_1/streamlit/datos/titanic.csv")
st.dataframe(df_titanic)


st.markdown("<h5 style=>El siguiente conjunto de datos está formado por 11 variables:</h5>", unsafe_allow_html=True)

st.markdown("<h5 style=>1. Passenger ID (variable cualitativa nominal)</h5>", unsafe_allow_html=True)
st.markdown("<h5 style=>2. Survived (variable cualitativa dicotómica, survived/died)</h5>", unsafe_allow_html=True)
st.markdown("<h5 style=>3. Pclass (variable cualitativa policotómica, )</h5>", unsafe_allow_html=True)
st.markdown("<h5 style=>4. Name (variable cualitativa nominal)</h5>", unsafe_allow_html=True)
st.markdown("<h5 style=>5. Sex (variable cualitativa dicotómica, male/female)</h5>", unsafe_allow_html=True)
st.markdown("<h5 style=>6. Age (variable numérica continua)</h5>", unsafe_allow_html=True)
st.markdown("<h5 style=>7. SibSp (variable numérica discreta)</h5>", unsafe_allow_html=True)
st.markdown("<h5 style=>8. Parch (variable numérica discreta)</h5>", unsafe_allow_html=True)
st.markdown("<h5 style=>9. Ticket (variable cualitativa nominal)</h5>", unsafe_allow_html=True)
st.markdown("<h5 style=>10. Fare (variable numérica continua)</h5>", unsafe_allow_html=True)
st.markdown("<h5 style=>11. Embarked (variable cualitativa policotómica, S/C/Q)</h5>", unsafe_allow_html=True)






st.markdown("<h5 style=>* Cabin (variable eliminada por tener un porcentaje de valores nulos muy alto,  77.1%)</h5>", unsafe_allow_html=True)
st.markdown("<h5 style=>* Age (variable con un porcentaje de valores nulos de 19.9%)</h5>", unsafe_allow_html=True)
st.markdown("<h5 style=>* Embarked (variable con un porcentaje de valores nulos de 0.22%)</h5>", unsafe_allow_html=True)
    


valores_nulos = pd.DataFrame(df_titanic.isnull().sum()/len(df_titanic)*100,  columns=['Porcentaje de valores nulos'])
grafica = px.bar(valores_nulos, x=valores_nulos.index, y='Porcentaje de valores nulos', template="plotly_white", width=400, height=400)
grafica.update_layout(title='Valores nulos en variables')      
st.plotly_chart(grafica)

df0 = pd.read_csv(r"/Users/laura/Desktop/Upgrade Hub/DataAnalytics/Contenidos/Modulo1/13_Trabajo_Modulo_1/streamlit/datos/titanic_preprocessed.csv")

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

st.dataframe(df0)