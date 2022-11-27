import streamlit as st
from PIL import Image
import string
import random
import pandas as pd
from datetime import date, datetime
import webbrowser

from st_aggrid import AgGrid
import numpy as np
import plotly.express as px
import io 
import openpyxl

# Criar senha secreta
import hashlib
def make_hashes(passwordgestor):
	return hashlib.sha256(str.encode(passwordgestor)).hexdigest()
def make_hashes(passwordcolab):
	return hashlib.sha256(str.encode(passwordcolab)).hexdigest()

def check_hashes(passwordgestor,hashed_text):
	if make_hashes(passwordgestor) == hashed_text:
		return hashed_text
	return False
def check_hashes(passwordcolab,hashed_text):
	if make_hashes(passwordcolab) == hashed_text:
		return hashed_text
	return False

# Salvar dados no banco de dados
import sqlite3 
conn = sqlite3.connect('data.db')
c = conn.cursor()
# Funções do banco de dados
def create_usergestor():
	c.execute('CREATE TABLE IF NOT EXISTS usergestor(usernamegestor TEXT, passwordgestor TEXT)')
def create_usercolab():
	c.execute('CREATE TABLE IF NOT EXISTS usercolab(usernamecolab TEXT,passwordcolab TEXT)')
def create_gestorCod():
	c.execute('CREATE TABLE IF NOT EXISTS gestorCod(gestorCod TEXT)')
def create_colabCod():
	c.execute('CREATE TABLE IF NOT EXISTS colabCod(colabCod TEXT)')
def create_empresa():
	c.execute('CREATE TABLE IF NOT EXISTS empresa(nome TEXT,ramo TEXT,colab integer, gestorCod TEXT, colabCod TEXT, email TEXT)')

def add_usergestor(usernamegestor,passwordgestor):
	c.execute('INSERT INTO usergestor(usernamegestor,passwordgestor) VALUES (?,?)',(usernamegestor,passwordgestor))
	conn.commit()
def add_usercolab(usernamecolab,passwordcolab):
	c.execute('INSERT INTO usercolab(usernamecolab,passwordcolab) VALUES (?,?)',(usernamecolab,passwordcolab))
	conn.commit()
def add_gestorCod(gestorCod):
	c.execute('INSERT INTO gestorCod(gestorCod) VALUES (?)',(gestorCod,))
	conn.commit()
def add_colabCod(colabCod):
	c.execute('INSERT INTO colabCod(colabCod) VALUES (?)',(colabCod,))
	conn.commit()
def add_empresa(nome,ramo,colab,gestorCod,colabCod,email):
	c.execute('INSERT INTO empresa(nome,ramo,colab,gestorCod,colabCod,email) VALUES (?,?,?,?,?,?)',(nome,ramo,colab,gestorCod,colabCod,email))
	conn.commit()

def excluir_gestor(usernamegestor,passwordgestor):
	c.execute('DELETE from usergestor WHERE usernamegestor =? AND passwordgestor =?',(usernamegestor,passwordgestor))
	conn.commit()
	conn.close()
def excluir_colab(usernamecolab,passwordcolab):
	c.execute('DELETE from usercolab WHERE usernamecolab =? AND passwordcolab =?',(usernamecolab,passwordcolab))
	conn.commit()
	conn.close()

def login_usergestor(usernamegestor,passwordgestor):
	c.execute('SELECT * FROM usergestor WHERE usernamegestor =? AND passwordgestor = ?',(usernamegestor,passwordgestor))
	data = c.fetchall()
	return data
def login_usercolab(usernamecolab,passwordcolab):
	c.execute('SELECT * FROM usercolab WHERE usernamecolab =? AND passwordcolab = ?',(usernamecolab,passwordcolab))
	data = c.fetchall()
	return data
def checagestorCod(gestorCod):
	c.execute('SELECT * FROM gestorCod WHERE gestorCod =?',(gestorCod,))
	data = c.fetchall()
	return data
def checacolabCod(colabCod):
	c.execute('SELECT * FROM colabCod WHERE colabCod =?',(colabCod,))
	data = c.fetchall()
	return data
def checaempresa(nome,ramo,colab,gestorCod,colabCod,email):
	c.execute('SELECT * FROM empresa WHERE nome=? AND ramo =? AND colab =? AND gestorCod =? AND colabCod =? AND email =?',(nome,ramo,colab,gestorCod,colabCod,email))
	data = c.fetchall()
	return data

def view_all_usergestor():
	c.execute('SELECT * FROM usergestor')
	data = c.fetchall()
	return data
def view_all_usercolab():
	c.execute('SELECT * FROM usercolab')
	data = c.fetchall()
	return data
def view_all_gestorcod():
	c.execute('SELECT * FROM gestorCod')
	data = c.fetchall()
	return data
def view_all_colabcod():
	c.execute('SELECT * FROM colabCod')
	data = c.fetchall()
	return data
def view_all_empresa():
	c.execute('SELECT * FROM empresa')
	data = c.fetchall()
	return data

# PÁGINA INICIAL
def main():
	st.title("SEJA BEM VINDO À FUNCONTROLL")

	menu = ["Cadastro da Empresa","Colaborador","Gestor","Cadastre-se"]
	choice = st.sidebar.selectbox("Menu",menu)

# CADASTRO DA EMPRESA
	if choice == "Cadastro da Empresa":
		st.title('Cadastro da Empresa')
		with st.form(key='incluir cliente'):
			nome = st.text_input(label = "Nome da empresa")
			ramo = st.selectbox(label = "Ramo da Empresa", options = ['Indústria', 'Comércio', 'Serviço','Outro'])
			colab = st.number_input(label = "Quantidade de colaboradores", format = "%d",step=1)
			email = st.text_input(label = "Email para contato")
			col1, col2 = st.columns((1,1))
			with col1:
				st.markdown(
					"""
					### ***Plano Básico***
					- Acesso limitado aos recursos de meditação
					- Acesso limitado aos recursos de receitas de remédios naturais
					- Recomendações de lojas de produtos naturais
					### ***R$ xx,00***
					""")  
			with col2:
				st.markdown(
					"""
					### ***Plano Premium***
					- Plano ilimitado
					- Acesso ilimitado aos recursos de meditação e receitas de remédios naturais
					- Cupons de desconto em lojas de produtos naturais
					- Acesso ao recurso de psicólogos
					### ***R$ yy,00***
					""")
			col3, col4 = st.columns((1,1))
			with col3:
				st.write('Segue abaixo o qrcode para pagamento')
				qrcode = Image.open('qrcode (2).png')
				st.image(qrcode, width=150)
			with col4:
				st.write('Ou acesse o link')
				url = 'https://www.sympla.com.br/evento-online/funcontroll/1780600?qrcode=true'
				if st.form_submit_button('Abrir pagamento'):
					webbrowser.open_new_tab(url)

			input_button_submit = st.form_submit_button("enviar")
			if input_button_submit:
				def x(size=6, chars=string.ascii_uppercase + string.digits):
					return ''.join(random.choice(chars) for _ in range(size))
				def y(size=4, chars=string.ascii_uppercase + string.digits):
					return ''.join(random.choice(chars) for _ in range(size))
							
				col1, col2 = st.columns ((1,1))
				with col1:
					st.write('Código para gestor:')
					gestorCod = x()
					st.info(gestorCod)
				with col2:
					st.write('Código para colaboradores:')
					colabCod = y()
					st.info(colabCod) 
				st.info("Esses códigos serão essenciais para a criação de usuários, tanto para o gestor, quanto para os colaboradores. Então é aconcelhável que seja anotado!")
				create_empresa()
				add_empresa(nome,ramo,colab, gestorCod, colabCod, email)	
				create_gestorCod()
				add_gestorCod(gestorCod)
				create_colabCod()
				add_colabCod(colabCod) 

# PAGINA DO COLABORADOR
	if choice == "Colaborador":
		st.subheader("Página do Colaborador")

		usernamecolab = st.sidebar.text_input("Nome")
		passwordcolab = st.sidebar.text_input("Senha",type='password')
		if st.sidebar.checkbox("Logar"):
			create_usercolab()
			hashed_pswd = make_hashes(passwordcolab)
			result = login_usercolab(usernamecolab,check_hashes(passwordcolab,hashed_pswd))
			if result:

				st.success("Bem vindo {}".format(usernamecolab))

				task = st.selectbox("Selecione o que deseja",["Página Inicial","Planner de Tarefas","Relaxar","Psicólogos","Excluir conta"])
				if task == "Página Inicial":
					st.write("Na FunControll é possível ter controle de todas as funções mediante ao tempo de trabalho")
						
				elif task == "Planner de Tarefas":
					st.subheader("Planner")
					
				elif task == "Relaxar":
					st.subheader("Espaço para relaxar")
					if st.button("Técnicas para ter controle da respiração"):
						resp = Image.open('Funcontroll (2).png')
						st.image(resp)
						resp2 = Image.open('Funcontroll (3).png')
						st.image(resp2)
					if st.button("Técnicas para meditar no trabalho"):
						trab = Image.open('Funcontroll (4).png')
						st.image(trab)
					if st.button("Técnicas para meditar em casa"):
						casa = Image.open('Funcontroll (5).png')
						st.image(casa)
						casa2 = Image.open('Funcontroll (6).png')
						st.image(casa2)
					if st.button("Receitas de chá calmante"):
						cha = Image.open('Funcontroll.png')
						st.image(cha)
					if st.button("Melhores recomendações de Ervas"):
						erva = Image.open('Funcontroll (1).png')
						st.image(erva)
					if st.button("Consulte as lojas parceiras com cupom de desconto"):
						col1, col2 = st.columns((1,1))
						with col1:
							st.markdown(
						      """
						      ### ***Loja x***
						      - 10% de desconto para em remédios naturais
						      - cupom: FunControll10
						      """)  
						with col2:
							st.markdown(
						      """
						      ### ***Loja y***
						      - 5% de desconto em produtos naturais
						      - frete gratis
						      - cupom: TimeFunControll
						      """)
				elif task == "Psicólogos":
					st.subheader("Segue abaixo a lista de contatos de Psicólogos")
					col1, col2 = st.columns((1,1))
					with col1:
						st.markdown(
						      """
						      ### Psicóloga A
						      - Especializada em tratamento para estresse e ansiedade
						      - Duração das seções: 30 min
						      - Contato: (__) ____-____
						      """)  
					with col2:
						st.markdown(
						      """
						      ### Psicólogo B
						      - Especialista em psicologia social
						      - Duração das seções: 30 min
						      - Contato: (__) ____-____
						      """)
				else:
					st.write("Se você tem certeza que desej excluir a conta, basta clicar no botão abaixo")
					if st.checkbox("excluir"):
						create_usercolab()
						hashed_pswd = make_hashes(passwordcolab)
						result = excluir_colab(usernamecolab,check_hashes(passwordcolab,hashed_pswd))
						if result:
							st.success("conta excluida com sucesso")
			else:
				st.warning("Nome/Senha incorretos ou acesso negado")
				
#PÁGINA DO GESTOR
	elif choice == "Gestor":
		st.subheader("Página do Gestor")

		usernamegestor = st.sidebar.text_input("Nome")
		passwordgestor = st.sidebar.text_input("Senha",type='password')
		if st.sidebar.checkbox("Logar"):
			create_usergestor()
			hashed_pswd = make_hashes(passwordgestor)
			result = login_usergestor(usernamegestor,check_hashes(passwordgestor,hashed_pswd))
			if result:

				st.success("Bem vindo {}".format(usernamegestor))

				task = st.selectbox("Selecione o que deseja",["Página Inicial","Planner","Pagamento","Excluir conta"])
				if task == "Página Inicial":
					st.subheader("Na FunControll é possível ter controle de todas as funções dos colaboradores e a forma de distribuição delas, mediante ao tempo de trabalho")

				elif task == "Planner":
					st.markdown(""" <style> .font {                                          
                        font-size:30px ; font-family: 'Cooper Black'; color: #FF9633;} 
                        </style> """, unsafe_allow_html=True)
					st.markdown('<p class="font">A melhor forma de organizar as suas tarefas</p>', unsafe_allow_html=True)

                    #Tamplete Exemplo  
					st.subheader('Etapa 1: Download do Planner')
					image = Image.open("planner.jpg") 
					st.image(image,  caption='Faça o download sem modificar o nome')

                    #Download do Tamplete
					@st.cache
					def convert_df(df):
						return df.to_csv().encode('utf-8')
					df=pd.read_csv("Planner.csv")
					csv = convert_df(df)
					st.download_button(
						label="Download do Planner de tarefas",
						data=csv,
						file_name='Planner.csv',
						mime='text/csv',
						)
					
					#Modificar o templete 
					st.subheader('Etapa 2: Faça o upload do planner')
					uploaded_file = st.file_uploader("Após fazer o dowload, faça o upload do arquivo sem modifica-lo. Ele servirá como uma base de armazenamento para você.", type=['csv'])
					if uploaded_file is not None:
						Tasks=pd.read_csv(uploaded_file)
						Tasks['Comeco'] = Tasks['Comeco'].astype('datetime64')
						Tasks['Fim'] = Tasks['Fim'].astype('datetime64')
						
						grid_response = AgGrid(
							Tasks,
							editable=True, 
							height=300, 
							width='100%',
							)
							
						updated = grid_response['data']
						df = pd.DataFrame(updated) 
						
						#Gráfico
						st.subheader('Etapa 3: Gerando o Planner de Tarefas')
						Options = st.selectbox("Exibir gráfico de Gantt por:", ['Equipe','Porcentagem Concluida'],index=0)
						if st.button('Gerar gráfico'): 
							fig = px.timeline(
								df, 
								x_start="Comeco", 
								x_end="Fim", 
								y="Tarefa",
								color=Options,
								hover_name="Descricao da tarefa"
								)
							fig.update_yaxes(autorange="reversed")                 
							fig.update_layout(
								title='Planner de Tarefas',
								hoverlabel_bgcolor='#DAEEED',   
								bargap=0.2,
								height=600,              
								xaxis_title="",
								yaxis_title="",                   
								title_x=0.5,                                         
								xaxis=dict(
									tickfont_size=15,
									tickangle = 270,
									rangeslider_visible=True,
									side ="top",            
									showgrid = True,
									zeroline = True,
									showline = True,
									showticklabels = True,
									tickformat="%x\n",      
									)
								)
							
							fig.update_xaxes(tickangle=0, tickfont=dict(family='Rockwell', color='blue', size=15))
							st.plotly_chart(fig, use_container_width=True)  
							st.subheader('Bônus: exporte o gráfico de Gantt interativo para HTML e compartilhe com outras pessoas!') 
							buffer = io.StringIO()
							fig.write_html(buffer, include_plotlyjs='cdn')
							html_bytes = buffer.getvalue().encode()
							st.download_button(
								label='Export to HTML',
								data=html_bytes,
								file_name='Gantt.html',
								mime='text/html'
								) 
						else:
							st.write('---')
					else:
						st.warning('Você precisa fazer o upload do arquivo.')
				elif task == "Pagamento":
					st.subheader("Pagamentos")
					st.write('Segue abaixo o qrcode para pagamento')
					qrcode = Image.open('qrcode (2).png')
					st.image(qrcode, width=150)
					st.write('Ou acesse o link')
					url = 'https://www.sympla.com.br/evento-online/funcontroll/1780600?qrcode=true'
					if st.button('Abrir pagamento'):
						webbrowser.open_new_tab(url)
				else:
					st.write("Se você tem certeza que deseja excluir a conta, basta clicar no botão abaixo")
					if st.checkbox("excluir"):
						create_usergestor()
						hashed_pswd = make_hashes(passwordgestor)
						result = excluir_gestor(usernamegestor,check_hashes(passwordgestor,hashed_pswd))
						if result:
							st.success("conta excluida com sucesso")
			else:
				st.warning("Nome/Senha incorretos ou acesso negado")

# PÁGINA PARA SE CADASTRAR
	elif choice == "Cadastre-se":
		st.subheader("Faça parte do time FunControll")
		funcao = ["Colaborador","Gestor"]
		selecionar = st.sidebar.selectbox("Selecione a sua função",funcao)
		if selecionar == "Colaborador":
			colabCod = st.sidebar.text_input("Insira o código de Colaborador")
			if st.sidebar.checkbox("Verificar código"):
				create_colabCod()
				resultado = checacolabCod(colabCod,)
				if resultado:
					new_usercolab = st.text_input("Nome")
					new_passwordcolab = st.text_input("Senha",type='password')
					if st.button("Cadastre-se"):
						create_usercolab()
						add_usercolab(new_usercolab,make_hashes(new_passwordcolab))
						st.success("Seu cadastro foi realizado com sucesso")
						st.info("Agora é só entrar na função que pertence")
				else:
					st.warning("Código incorreto")
		if selecionar == "Gestor":
			gestorCod = st.sidebar.text_input("Insira o código do gestor")
			if st.sidebar.checkbox("Verificar código"):
				create_gestorCod()
				resultado2 = checagestorCod(gestorCod,)
				if resultado2:
					new_usergestor = st.text_input("Nome")
					new_passwordgestor = st.text_input("Senha",type='password')
					if st.button("Cadastre-se"):
						create_usergestor()
						add_usergestor(new_usergestor,make_hashes(new_passwordgestor))
						st.success("Seu cadastro foi realizado com sucesso")
						st.info("Agora é só entrar na função que pertence")
				else:
					st.warning("Código incorreto")


if __name__ == '__main__':
	main()