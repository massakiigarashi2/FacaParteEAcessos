import streamlit as st
from PIL import Image

##página  inicial
st.sidebar.title('Página Inicial')
paginaselecionada = st.sidebar.selectbox('Selecione a Página desejada', ['Sobre','Nossos Serviços'])

if paginaselecionada == 'Sobre':
  st.title('Sobre a Nossa Plataforma')
  st.write('Nós somos uma plataforma que disponibiliza funções para os gestores e colaboradores das empresas distribuírem as tarefas de maneira mais assertiva e organizada. Além disso, os membros da FunControll têm acesso a meios de melhoria de qualidade de vida e podem agendar sessões com terapeutas, psicólogos e selecionar funções para relaxar, como meditações.')
  image = Image.open('logo.jpg')
  st.image(image)
  
##Como funcioina
  st.title('Como Funciona?')
  x = st.slider('Etapas:', 1, 3)
  if x == 1 :
    st.write ("GESTORES realizam o cadastro")
    gest= Image.open('gestor.jpg')
    st.image(gest)
  elif x == 2 :
    st.write ("COLABORADORES passam a ter acesso com o código liberado ao gestor.")
    colab = Image.open('colaborador.jpg')
    st.image(colab)
  else :
    st.write ("GESTORES E COLABORADORES usufruem de  todas as funcionalidades da plataforma. ")
    gestcolab = Image.open('gestorcolaborador.jpg')
    st.image(gestcolab)
    

##Serviços
elif paginaselecionada == 'Nossos Serviços':
  st.title('Nossos Serviços')
  y = st.selectbox('A FunControll conta com:',['Planner de tarefas','Meditação','Receita de Remédios Naturais','Psicólogos'])
  if y == 'Planner de tarefas':
    st.write('Baseado nas tarefas e disponibilidades dos colaboradores, é gerado um planner com a melhor distribuição de funções')
    planner = Image.open('planner.jpg')
    st.image(planner)
  elif y == 'Meditação':
    st.write('Para os colaboradores que se sentirem sobrecarregados, ficará disponível técnicas de meditação para ajudar')
    med = Image.open('meditacao.jpg')
    st.image(med)
  elif y == 'Receita de Remédios Naturais':
    st.write('Será disponibilizado receita de remédios naturais para ajudar no relaxamento da ansiedade ou estresse')
    remed = Image.open('remedio.jpg')
    st.image(remed)
  else:
    st.write('Para os colaboradores que desejarem, será oferecido sugestões de psicólogos online.')
    psic = Image.open('psicologo.jpg')
    st.image(psic)


