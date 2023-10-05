import streamlit as st
import streamlit_authenticator as stauth
import numpy as np

CONTROL_WARNING = False

def auth(user, pwd):
    return user == "thiago" and pwd == "123"

def error_login(usr, pwd):
    if not usr and not pwd:
        st.warning("Digite um usuário e senha!!")
        return False
    return True


class ApplicationWeb:
    def login_page(self):
        st.image("app/assets/_img/rpg_cut_down.jpeg")
        st.markdown("# D&D Online Generator")
        st.markdown("#")

        username = None
        password = None


        with st.form("Login"):

            username = st.text_input("Usuário")
            password = st.text_input("Senha", type="password")

            st.form_submit_button("Entrar", on_click=error_login, args=(username, password), type="primary")

        st.button("Registrar",type="secondary")

        if username and password:
            if auth(username, password):
                ...
            else:
                st.title("Acesso negado")

        st.write("by tlsabara")

    def form_page(self):
        st.image("app/assets/_img/ficha_pp.jpeg")
        st.title("Ficha de personagem")
        with st.form("Ficha de personagem"):
            tb_info, tb_person, tb_stats, tb_hist = st.tabs(["Info", "Personalidade", "Stats", "Histórico"])

            # Aba de Informações
            tb_info.text_input("Nome do personagem")
            tb_info.text_input("Nome do Jogador")
            tb_info.text_input("Classe do personagem")
            tb_info.text_input("Antecedente")
            tb_info.text_input("Tendencia")
            tb_info.text_input("Raça")
            tb_info.text_input("Nível")

            # Aba de personalidade
            tb_person.text_area("Traços de personalidade")
            tb_person.text_area("Ideais")
            tb_person.text_area("Vinculos")
            tb_person.text_area("Defeitos")
            tb_person.text_area("Caracteríisticas e Traços")
            tb_person.text_area("Outras Proficiências e Idiomas",height=300)

            # Aba de Histórico
            tb_hist.text_area("Histórico do personagem")

            st.form_submit_button("Cadastrar Personagem", type="primary")

runner = ApplicationWeb()
runner.login_page()
# runner.form_page()
