import streamlit as st

from configs import get_config
import json
from utils import criar_chain_conversa,PASTA_ARQUIVOS

def config_page():
    st.header('Pagina de configuração do Bot', divider=True)

    model_name = st.text_input('Modifique o Modelo', value=get_config('model_name'))
    retrieval_search_type = st.text_input('Modifique o tipo de Restrieval', value=get_config('retrieval_search_type'))
    retrieval_kwarg = st.text_input('Modifique os paramentos de Retriveval', value=get_config('retrieval_kwarg'))
    prompt = st.text_area('Modifique o prompt padrão', height=500, value=get_config('prompt'))
    
    if st.button('Salvar parâmentros', use_container_width=True):
        retrieval_kwarg = json.loads(retrieval_kwarg.replace("'", '"'))
        st.session_state['model_name'] = model_name
        st.session_state['retrieval_search_type'] = retrieval_search_type
        st.session_state['retrieval_kwarg'] = retrieval_kwarg
        st.session_state['prompt'] = prompt
        st.rerun()

    if st.button('Atualizando ChatAo', use_container_width=True):
        if len(list(PASTA_ARQUIVOS.glob('*.pdf'))) == 0:
            st.error('Adicione arquivos.pdf para iniciar o ChatAI ')
        else:
            st.success('Inicializando o ChatAi...')
            criar_chain_conversa()
            st.rerun()



config_page()