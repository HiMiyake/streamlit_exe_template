# --- import ---
# standard library
import datetime

# pip
import streamlit as st

# my libralies


# --- main ---
st.title("Home Page")
st.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
