import streamlit as st
from PIL import Image
import string
import random
import pandas as pd




# Security
#passlib,hashlib,bcrypt,scrypt
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
# DB Management
import sqlite3 
conn = sqlite3.connect('datateste.db')
c = conn.cursor()
# DB  Functions
def create_usergestor():
	c.execute('CREATE TABLE IF NOT EXISTS usergestor(usernamegestor TEXT, passwordgestor TEXT)')
def create_usercolab():
	c.execute('CREATE TABLE IF NOT EXISTS usercolab(usernamecolab TEXT,passwordcolab TEXT)')
def create_gestorCod():
	c.execute('CREATE TABLE IF NOT EXISTS gestorCod(gestorCod TEXT)')
def create_colabCod():
	c.execute('CREATE TABLE IF NOT EXISTS colabCod(colabCod TEXT)')
def create_cadastro():
	c.execute('CREATE TABLE IF NOT EXISTS cadastro(nome TEXT,ramo TEXT,colab integer)')

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
def add_cadastro(nome,ramo,colab):
	c.execute('INSERT INTO cadastro(nome,ramo,colab) VALUES (?,?,?)',(nome,ramo,colab))
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
def view_all_cadastro():
	c.execute('SELECT * FROM cadastro')
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
			new_nome = st.text_input(label = "Nome da empresa")
			new_ramo = st.selectbox(label = "Ramo da Empresa", options = ['Indústria', 'Comércio', 'Serviço','Outro'])
			new_colab = st.number_input(label = "Quantidade de colaboradores", format = "%d",step=1)
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
				create_cadastro()
				add_cadastro(new_nome,new_ramo,new_colab)	
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
				if task == "Excluir conta":
					if st.checkbox("excluir"):
						create_usercolab()
						hashed_pswd = make_hashes(passwordcolab)
						result = excluir_colab(usernamecolab,check_hashes(passwordcolab,hashed_pswd))
						if result:
							st.success("conta excluida com sucesso")
			else:
				st.info('Senha incorreta ou acesso negado')
				
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

				task = st.selectbox("Selecione o que deseja",["Página Inicial","Planner","Análise dos usuários Cadastrados","Pagamento","Excluir conta"])
				if task == "Excluir conta":
					if st.checkbox("excluir"):
						create_usergestor()
						hashed_pswd = make_hashes(passwordgestor)
						result = excluir_gestor(usernamegestor,check_hashes(passwordgestor,hashed_pswd))
						if result:
							st.success("conta excluida com sucesso")
			else:
				st.info('Senha incorreta ou acesso negado')
				

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
					st.info("Código incorreto")
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
					st.info("Código incorreto")


if __name__ == '__main__':
	main()
