import streamlit as st

st.set_page_config(
	page_title = "Homepage",
	page_icon = "👋"
)

st.title("Hi Paru! 👋")
st.markdown("""
This is the dashboard you wanted. Hope you like this :) ✨

👈 Use the sidebar to navigate
""")

from common import *
common_styles()