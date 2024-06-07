from pathlib import Path
import streamlit as st
import time
from utils import criar_chain_conversa, PASTA_ARQUIVOS
from login_page import *
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader


PASTA_ARQUIVOS = Path(__file__).parent / 'arquivos'

def chat_window():
    st.header('👾Bem vindo ao Chat PDF👾', divider=True)

    if not 'chain' in st.session_state:
        st.error('Faça upload de PDFs para começar')
        st.stop()

    chain = st.session_state['chain']
    memory = chain.memory

    mensagens = memory.load_memory_variables({})['chat_history']
    
    container = st.container()
    for mensagem in mensagens:
        chat = container.chat_message(mensagem.type)
        chat.markdown(mensagem.content)
    nova_mensagem = st.chat_input('Converse com seu pdf...')
    if nova_mensagem:
        chat = container.chat_message('human')
        chat.markdown(nova_mensagem)
        chat = container.chat_message('ai')
        chat.markdown('Gerando resposta')

        resposta = chain.invoke({'question': nova_mensagem})
        st.session_state['ultima_resposta'] = resposta

        st.rerun()

def sidebar():
    uploaded_pdfs = st.file_uploader(
        'Adicione seus arquivos pdf',
         type=['.pdf'], 
         accept_multiple_files=True
         )
    if not uploaded_pdfs is None:
        for arquivo in PASTA_ARQUIVOS.glob('*.pdf'):
            arquivo.unlink()
        for pdf in uploaded_pdfs:
            with open(PASTA_ARQUIVOS / pdf.name, 'wb') as f:
                f.write(pdf.read())
    label_botao = 'Iniciar ChatAi'
    if 'chain' in st.session_state:
        label_botao = 'Atualizar ChatAi'
    if st.button(label_botao, use_container_width=True):
        if len(list(PASTA_ARQUIVOS.glob('*.pdf'))) == 0:
            st.error('Adicione arquivos.pdf para iniciar o ChatAI ')
        else:
            st.success('Inicializando o ChatAi...')
            criar_chain_conversa()
            st.rerun()
   
def home_page():
    with st.sidebar:
        sidebar()
    chat_window()

def main():
    config = load_config()
   
    authenticator = stauth.Authenticate(
        config['credentials'],
        config['cookie']['name'],
        config['cookie']['key'],
        config['cookie']['expiry_days']
    )
  
    authenticator.login()

    if st.session_state["authentication_status"]:
        authenticator.logout("Logout", "sidebar")
        st.write(f'Welcome *{st.session_state["name"]}*')
        home_page()
    else:
        st.error("Você precisa fazer login primeiro!")
        st.stop()

if __name__ == '__main__':
    main()
