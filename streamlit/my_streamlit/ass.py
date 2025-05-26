import streamlit as st

st.title("YOUR FAVOURITE PRIGRAMMING LANGUAGE PIKER")
progmming=st.selectbox("choose your favourite language",["python","java","javascript","c++"])
st.write(f"you choooce {progmming} is execellent  choice")
st.success("you language choose")