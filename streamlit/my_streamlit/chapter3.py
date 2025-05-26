import streamlit as st 
st.title("VOTING MACHINE FOR PROJECTS")

col1,col2=st.columns(2)

with col1:
    st.header("software project")
    vote1=st.button("vote for software project")
    st.image("https://www.coderus.com/wp-content/uploads/fly-images/996776/different-types-of-software-coderus-branded-image-1400x9999.jpg",width=300)
    
with col2:
    st.header("Hardware projects")
    vote2=st.button("vote for hardware projects")
    st.image("https://cdn.educba.com/academy/wp-content/uploads/2019/12/Types-of-computer-Hardware.jpg")
if vote1:
    st.success("you vote for software project")
    
if vote2:
    st.success("you vote for hardware projects")
    
    
    
name=st.sidebar.text_input("Enter your name")
project=st.sidebar.selectbox("choose your project options",["AI based","harware based","Django based"])

st.write(f"welcome  {name}  your {project} is selected")

with st.expander("steps of creating proejct"):
    st.write(""" 
            1. create folder 
            2. create virtual environment
            3. activate virtual environment    
            4. install streamlit
            5.create python file
             
             """)
st.markdown("## welcome to Rabia project")
st.markdown("> quotes")