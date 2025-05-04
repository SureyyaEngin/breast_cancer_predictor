import streamlit as st
import pickle
import pandas as pd

def main():
    st.set_page_config(
        page_title="Breast Cancer Predictor",
        page_icon=":femaile-doctor",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    st.write("Hello World")
    


if __name__ == '__main__':
    main()