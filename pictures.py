import streamlit as st

st.title("More Pictures")

st.image('/workspaces/sell_piano/images/full_picture.jpg', caption='Full picture')
st.image('/workspaces/sell_piano/images/inside.jpg', caption='Inside piano')
st.image('/workspaces/sell_piano/images/keys_uncovered.jpg', caption='Keys')
st.image('/workspaces/sell_piano/images/keys_cover.jpg', caption='Keyboard cover (included)')
st.image('/workspaces/sell_piano/images/side.jpg', caption='Side view')
st.image('/workspaces/sell_piano/images/the_whole_thing.jpg', caption='Full view with pedals')

st.subheader("Please contact me if interested!")

st.markdown('<a href="mailto:kaylaxu@gmail.com">Click here to email me!</a>', unsafe_allow_html=True)