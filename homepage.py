import streamlit as st

st.title("Used Yamaha U1 - $7,000")
st.subheader("Purchased 2013, made in Japan")
col1, col2 = st.columns(2)

with col1:
    st.write("This piano was purchased in 2013 and is in excellent condition. The piano was last tuned three years ago.")
    st.write("This piano would be great for any beginner for its clear sound and compact size.")
    st.write("The piano comes with the matching bench (which opens to reveal storage area).")
    st.write("As a bonus, we will add the piano light as a freebie.")
    st.write("For more pictures, please check out the navigation for the pictures tab!")

    st.subheader("Please contact me if interested!")

    st.markdown('<a href="mailto:kaylaxu@gmail.com">Click here to email me!</a>', unsafe_allow_html=True)

with col2:
    st.image('/workspaces/sell_piano/images/full_picture.jpg')
    st.image('/workspaces/sell_piano/images/free_light.jpg')
