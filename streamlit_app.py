import streamlit as st

pages = {
    "Homepage": [
        st.Page("homepage.py", title="Home")
    ],
    "Pictures": [
    st.Page("pictures.py", title="Pictures"),
    ]
}

pg = st.navigation(pages)

pg.run()