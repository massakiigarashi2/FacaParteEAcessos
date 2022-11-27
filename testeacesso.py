import streamlit as st
from PIL import Image
import string
import random
import pandas as pd
from datetime import date, datetime

# Security
#passlib,hashlib,bcrypt,scrypt
import hashlib
def make_hashes(password):
	return hashlib.sha256(str.encode(password)).hexdigest()

def check_hashes(password,hashed_text):
	if make_hashes(password) == hashed_text:
		return hashed_text
	return False
# DB Management
import sqlite3 
con = sqlite3.connect('datateste.db')
c = con.cursor()
# DB  Functions
def create_usertable():
	c.execute('CREATE TABLE IF NOT EXISTS userstable(username TEXT,password TEXT)')


def add_userdata(username,password):
	c.execute('INSERT INTO userstable(username,password) VALUES (?,?)',(username,password))
	con.commit()

def login_user(username,password):
	c.execute('SELECT * FROM userstable WHERE username =? AND password = ?',(username,password))
	data = c.fetchall()
	return data


def view_all_users():
	c.execute('SELECT * FROM userstable')
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
			input_name = st.text_input(label = "Nome da empresa")
			input_occupation = st.selectbox(label = "Ramo da Empresa", options = ['Indústria', 'Comércio', 'Serviço','Outro'])
			input_age = st.number_input(label = "Quantidade de colaboradores", format = "%d",step=1)
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
			a = st.selectbox('Plano desejado:',['Plano Básico','Plano Premium'])
			b = st.selectbox('Forma de Pagamento:',['Pix','Cartão de Crédito','Boleto'])
			input_button_submit = st.form_submit_button("enviar")
			if input_button_submit:
				def x(size=6, chars=string.ascii_uppercase + string.digits):
					return ''.join(random.choice(chars) for _ in range(size))
				def y(size=4, chars=string.ascii_uppercase + string.digits):
					return ''.join(random.choice(chars) for _ in range(size))
							
				col1, col2 = st.columns ((1,1))
				with col1:
					st.write('Código para gestor:')
					st.info(x())
				with col2:
					st.write('Código para colaboradores:')
					st.info(y()) 

# PAGINA DO COLABORADOR
	if choice == "Colaborador":
		st.subheader("Página do Colaborador")

		username = st.sidebar.text_input("Nome")
		password = st.sidebar.text_input("Senha",type='password')
		if st.sidebar.checkbox("Logar"):
			create_usertable()
			hashed_pswd = make_hashes(password)

			result = login_user(username,check_hashes(password,hashed_pswd))
			if result:

				st.success("Bem vindo {}".format(username))

				task = st.selectbox("Selecione o que deseja",["Página Inicial","Planner de Tarefas","Relaxar","Psicólogos"])
				if task == "Página Inicial":
					st.write("Na FunControll é possível ter controle de todas as funções mediante ao tempo de trabalho")
					st.write("Segue abaixo um formulário a ser preenchido com as funções que se deseja fazer")
					st.button("Formulário de Funções - VER COMO DIRECIONAR")
						

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
				else:
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
				st.warning("Nome/Senha incorretos")

#PÁGINA DO GESTOR
	elif choice == "Gestor":
		st.subheader("Página do Gestor")

		username = st.sidebar.text_input("Nome")
		password = st.sidebar.text_input("Senha",type='password')
		if st.sidebar.checkbox("Logar"):
			create_usertable()
			hashed_pswd = make_hashes(password)

			result = login_user(username,check_hashes(password,hashed_pswd))
			if result:

				st.success("Bem vindo {}".format(username))

				task = st.selectbox("Selecione o que deseja",["Página Inicial","Planner","Análise dos usuários Cadastrados","Pagamento"])
				if task == "Página Inicial":
					st.subheader("Na FunControll é possível ter controle de todas as funções dos colaboradores e a forma de distribuição delas, mediante ao tempo de trabalho")

				elif task == "Planner":
					st.subheader("Planner")
				elif task == "Análise dos usuários Cadastrados":
					st.subheader("Quantidade de usuários cadastrados")
					user_result = view_all_users()
					clean_db = pd.DataFrame(user_result,columns=["Nome","Senha"])
					st.dataframe(clean_db)
				else:
					st.subheader("Pagamentos")
					uploaded_file = 'pagamento.csv' 
					pagamento = pd.read_csv(uploaded_file)
					st.subheader(pagamento)
					today = date.today()
					st.subheader(today)
				
			else:
				st.warning("Nome/Senha incorretos")

# PÁGINA PARA SE CADASTRAR
	elif choice == "Cadastre-se":
		st.subheader("Faça parte do time FunControll")
		new_user = st.text_input("Nome")
		new_password = st.text_input("Senha",type='password')
		new_codigo = st.text_input("Insira abaixo o código fornecido para colaborador ou gestor")

		if st.button("Cadastre-se"):
			create_usertable()
			add_userdata(new_user,make_hashes(new_password))
			st.success("Seu cadastro foi realizado com sucesso")
			st.info("Agora é só entrar na função que pertence")
