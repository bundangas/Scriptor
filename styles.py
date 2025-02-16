import streamlit as st

def apply_custom_styles():
    st.markdown("""
        <style>
        #MainMenu {visibility: hidden;}
        header {visibility: hidden;}
        footer {visibility: hidden;}

        .main {
            padding: 2rem;
        }
        .stButton>button {
            width: 100%;
            margin-bottom: 1rem;
            padding: 0.5rem;
            border-radius: 5px;
        }
        .section-box {
            background-color: #f8f9fa;
            padding: 1rem;
            border-radius: 5px;
            margin-bottom: 1rem;
            border: 1px solid #dee2e6;
        }
        .copy-button {
            float: right;
            padding: 0.25rem 0.5rem;
            font-size: 0.875rem;
        }
        h1 {
            color: #1e88e5;
            text-align: center;
            margin-bottom: 2rem;
        }
        h3 {
            color: #424242;
            margin-bottom: 1rem;
        }
        .footer {
            position: fixed;
            bottom: 0;
            left: 0;
            right: 0;
            background-color: #f8f9fa;
            padding: 1rem;
            font-size: 0.8rem;
            border-top: 1px solid #dee2e6;
            display: flex;
            justify-content: space-between;
        }
        .footer-left {
            color: #666;
        }
        .footer-right {
            color: #666;
            font-style: italic;
        }
        .stTextArea>div>div {
            min-height: 150px !important;
            max-height: 200px !important;
        }
        .stSelectbox {
            margin-bottom: 1rem;
        }
        </style>
    """, unsafe_allow_html=True)

def add_footer():
    st.markdown("""
        <div class="footer">
            <div class="footer-left">Feito por Lucas Nascimento Brito Faccioli</div>
            <div class="footer-right">Deus seja louvado</div>
        </div>
    """, unsafe_allow_html=True)