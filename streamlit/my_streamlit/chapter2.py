import streamlit as st 
st.title("NEW APP FOR WIDGETSS")

if st.button("create app"):
    st.success("your app is created")
    
add_app=st.checkbox("add ap in your project")
if add_app:
    st.write("your app is added in your project")
    
    
project_type=st.radio("choose your project type",["AI based","web base","agentic based"])
st.write(f"your project is {project_type}")

select=st.selectbox("select your priority",["ml","Django","chatbot"])
st.write(f"your priority is {select}")
temprature=st.slider("temperatur of generated text",0,13,3)
st.write(f"your temperature is {temprature}")

name=st.text_input("Enter your name")
if name:
    st.write(f"welcome {name} your project is on the way")
    
date_of_birth=st.date_input("select your data of birth ")
st.write(f"your date of birth : {date_of_birth} ")
