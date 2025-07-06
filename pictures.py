import streamlit as st

st.title("More Pictures")

st.image('full_picture.jpg', caption='Full picture')
st.image('inside.jpg', caption='Inside piano')
st.image('keys_uncovered.jpg', caption='Keys')
st.image('keys_cover.jpg', caption='Keyboard cover (included)')
st.image('side.jpg', caption='Side view')
st.image('the_whole_thing.jpg', caption='Full view with pedals')

st.subheader("Please contact me if interested!")

st.markdown('<a href="mailto:kaylaxu@gmail.com">Click here to email me!</a>', unsafe_allow_html=True)