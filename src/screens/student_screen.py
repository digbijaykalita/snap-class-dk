import streamlit as st
from src.ui.base_layout import style_background_dashboard

def student_screen():
    st.header('Student Screen')

    style_background_dashboard()


    if st.button('Back'):
        st.session_state['login_type'] = None
        st.rerun()