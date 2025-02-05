import streamlit as st
from test1 import get_links, get_content

tab1, tab2 = st.tabs(["Links", "Content"])


with tab1:
    st.write("Enter University Name")

    st.text_input("university name", key="name", value=None)

    if st.button("Submit", key="1"):
        links = get_links(st.session_state.name)
        for link in links:
            st.write(link)


with tab2:
    st.write("Enter link related to university courses")

    st.text_input("link", key="link", value=None)

    if st.button("Submit", key="2"):
        content = get_content(st.session_state.link)
        for text in content:
            st.write(text)