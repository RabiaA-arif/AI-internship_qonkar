import streamlit as st

st.title("MY STREAMLIT")
st.subheader("come from streamlit")
st.text("welcome your streamlit app")
st.write("write your query here")


food=st.selectbox("Your favourite food",["fries","Biryani","Halwa"])

st.write(f"hah your choice is nice:> {food}")

st.success(f"Your choice {food} is done")