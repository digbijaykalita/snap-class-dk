import streamlit as st  


def style_background_home():
    st.markdown(
        """
        <style>
                .stApp {
                    background: #5865f2 !important;
                }

                .stApp div[data-testid="stColumn"]{
                    background-color: #e0e3ff !important;
                    padding: 2.5rem !important;
                    border-radius: 5rem !important;
                }
        </style>
        """,unsafe_allow_html=True
    )

def style_background_dashboard():
    st.markdown(
        """
        <style>
                .stApp {
                    background: #e0e3ff !important;
                }
        </style>
        """,unsafe_allow_html=True
    )


def style_base_layout():
    st.markdown(
        """
        <style>

            @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis:YEAR@1979&display=swap');
            @import url('https://fonts.googleapis.com/css2?family=Outfit&display=swap');


            /* Hide top toolbar */

            #MainMenu, footer, header {
                visibility: hidden;
            }

            .block-container {
                padding-top: 1.5rem !important;
            }

            h1 {
                font-family: 'Climate Crisis', sans-serif !important;
                font-size: 3.5rem !important;
                line-height: 1.1 !important;   
                margin-bottom: 0rem !important;
            }

            h2 {
                font-family: 'Climate Crisis', sans-serif !important;
                font-size: 2rem !important;
                
                line-height: 0.9 !important;   
                margin-bottom: 0rem !important;
            }

            h3, h4, p {
                font-family: 'Outfit', sans-serif !important;
            }

            button { 
                border-radius: 1.5rem !important;      
                background-color: #5865f2 !important; 
                padding: 10px 20px !important;
                color: white !important;
                border: none !important;
                transition: transform 0.25s ease-in-out !important;
            }

            button[kind="secondary"] {
                border-radius: 1.5rem !important; 
                background-color: #eb459e !important;  
                padding: 10px 20px !important;
                color: white !important;    
                border: none !important;
                transition: transform 0.25s ease-in-out !important;
            }

            button[kind="tertiary"] {
                border-radius: 1.5rem !important;   
                padding: 10px 20px !important;
                color: white !important;    
                background-color: black !important;
                border: none !important;
                transition: transform 0.25s ease-in-out !important;
            }

            button:hover {
                transform: scale(1.05) !important;
            }


        </style>
        """,unsafe_allow_html=True
    )