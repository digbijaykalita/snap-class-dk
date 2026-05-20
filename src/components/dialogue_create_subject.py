import streamlit as st
from src.database.db import create_subject

@st.dialog('Create new subject')
def create_subject_dialogue(teacher_id):
    st.write('Enter the details of the new subject')
    sub_id = st.text_input('Subject code', placeholder='CS101')
    sub_name = st.text_input('Subject name', placeholder='Introduction to CS')
    sub_section = st.text_input('Section', placeholder='Batch A')

    if st.button('Create subject', type='primary', width='stretch'):
        if sub_id and sub_name and sub_section:
            try:
                create_subject(sub_id, sub_name, sub_section, teacher_id)
                st.toast('Subject created successfully!')
                st.rerun()
            except Exception as e:
                st.error(f'Error : {str(e)}')
        else:
            st.warning('Please field all the fields')


