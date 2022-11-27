from st_aggrid import AgGrid
import streamlit as st
import pandas as pd 
import numpy as np
import plotly.express as px
from  PIL import Image
import io 
import openpyxl


st.set_page_config(layout='wide') #Choose wide mode as the default setting

#Add a logo (optional) in the sidebar
logo = Image.open('logo.jpg')
st.sidebar.image(logo,  width=120)
      
#Add an app title. Use css to style the title
st.markdown(""" <style> .font {                                          
    font-size:30px ; font-family: 'Cooper Black'; color: #FF9633;} 
    </style> """, unsafe_allow_html=True)
st.markdown('<p class="font">A melhor forma de organizar as suas tarefas</p>', unsafe_allow_html=True)

#Add a template screenshot as an example 
st.subheader('Faça o seu Planner Tarefas')
image = Image.open('planner.jpg') 
st.image(image,  caption='Para adicionar tarefas, preencha as opções ao lado')

#Allow users to download the template
planner = 'PlannerTarefas.xlsx'
df = pd.read_excel(planner)
st.write(df)  
st.sidebar.header("Opções")
opcao_form = st.sidebar.form("opcao_form")
tarefa = opcao_form.text_input('Tarefa a ser realizada')
descricao= opcao_form.text_input('Descrição da tarefa a ser realizada')
comeco = opcao_form.text_input('Data de início (AAAA/MM/DD)')
fim = opcao_form.text_input('Data de finalização (AAAA/MM/DD)')
porcentagem = opcao_form.text_input('Porcentagem da tarefa ja realizad')
equipe = opcao_form.text_input('Equipe para realizar a tarefa')
add_data = opcao_form.form_submit_button()
if add_data:
    new_data = [{"Tarefa": tarefa, "Descrição da tarefa": descricao,"Começo": comeco, "Fim": fim, "Porcentagem concluída": porcentagem,"Equipe": equipe}]
    df = df.append(new_data, ignore_index = True)
    df.to_excel(planner)
    