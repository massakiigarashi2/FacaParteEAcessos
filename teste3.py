import streamlit as st
import string
import random
import pandas as pd
from datetime import date, datetime
import webbrowser
import csv

from st_aggrid import AgGrid
import numpy as np
import plotly.express as px
import io 
import openpyxl

st.write('Tabela')
uploaded_file = st.file_uploader("Choose a file", type = ['csv', 'xlsx'])
if uploaded_file is not None:
    try:
        data = pd.read_csv(uploaded_file)
        data.to_csv('data.csv', index=False)
    except Exception as e:
        print(e)
        data = pd.read_excel(uploaded_file)
        data.to_csv('data.csv', index=False)
        st.write(data)
df1 = pd.DataFrame([['a', 'b'], ['c', 'd']],
                   index=['row 1', 'row 2'],
                   columns=['col 1', 'col 2'])
df1.to_excel("output.xlsx")
