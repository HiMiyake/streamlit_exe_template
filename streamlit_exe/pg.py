import streamlit as st

st.set_page_config(page_title="myApp", layout="wide")


pages = {
    "Top": [
        st.Page("pages/home.py", title="Home", icon="🏠", default=True),
    ],
    "Others": [
        st.Page("pages/page1.py", title="Page1", icon="📥"),
        st.Page("pages/page2.py", title="Page2", icon="💻"),
        st.Page("pages/page3.py", title="Page3", icon="📈"),
    ],
}

pg = st.navigation(pages=pages, expanded=True)
pg.run()
