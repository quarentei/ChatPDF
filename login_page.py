import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader

def load_config():
    with open('config.yaml') as file:
        config = yaml.load(file, Loader=SafeLoader)
    return config

def main():
    config = load_config()

    authenticator = stauth.Authenticate(
        config['credentials'],
        config['cookie']['name'],
        config['cookie']['key'],
        config['cookie']['expiry_days']
    )

    try:
        authenticator.login()
    except stauth.LoginError as e:
        st.error(e)

    if st.session_state.get("authentication_status"):
        st.experimental_set_query_params(page="home")
        st.experimental_rerun()
    elif st.session_state.get("authentication_status") is False:
        st.error('Username/password is incorrect')
    elif st.session_state.get("authentication_status") is None:
        st.warning('Please enter your username and password')

if __name__ == "__main__":
    main()