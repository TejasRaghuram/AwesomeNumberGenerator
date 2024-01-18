import streamlit as st
import random

if st.button('Generate Random Number'):
    st.write(random.randint(1, 10))
