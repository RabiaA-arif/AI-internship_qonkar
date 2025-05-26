import streamlit as st
from datetime import date 
st.title("MINI CALCULATOR ON USING STREAMLIT GUI")
date_of_birth=st.date_input("Enter your data of birthfor age calculation")
today=date.today()
if date_of_birth:
    age=today.year - date_of_birth.year
    if(today.month,today.day)< (date_of_birth.month,date_of_birth.day):
        age-=1
        st.write(f"your age is {age} ")
