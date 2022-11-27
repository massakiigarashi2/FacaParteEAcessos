# importar os pacotes necessários
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import streamlit as st
# importar o arquivo excel em um df
df = pd.read_excel("planner_tarefas.xlsx")
# eliminar as colunas com valores ausentes
summary = df.dropna(subset=['Descricao da tarefa'], axis=0)['Descricao da tarefa']
# concatenar as palavras
all_summary = " ".join(s for s in summary)
# lista de stopword
stopwords = set(STOPWORDS)
stopwords.update(["da", "meu", "em", "você", "de", "ao", "os"])
# gerar uma wordcloud
wordcloud = WordCloud(stopwords=stopwords,
                      background_color="black",
                      width=1600, height=800).generate(all_summary)
# mostrar a imagem final
fig, ax = plt.subplots(figsize=(10,6))
ax.imshow(wordcloud, interpolation='bilinear')
ax.set_axis_off()
plt.imshow(wordcloud);
wordcloud.to_file("nuvem.png")
imagem = Image.open('nuvem.png')
st.image(imagem)