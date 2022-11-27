import streamlit as st
import numpy as np
import pandas as pd
import csv


# Code to read a single file 
uploaded_file = st.file_uploader("Choose a file", type = ['csv', 'xlsx'])
if uploaded_file is not None:
    try:
        data = pd.read_csv(uploaded_file)
        data.to_csv('data.csv', index=False)
    except Exception as e:
        print(e)
        data = pd.read_excel(uploaded_file)
        data.to_csv('data.csv', index=False)

    with open("data.csv", "r") as f:
        reader = csv.reader(f, delimiter=",")
        for i, line in enumerate(reader):
            st.write(f"{i}: {line}")