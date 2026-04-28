import streamlit as st
#Title of App
st.title("My first streamlit app")
#Adding text
st.write(Hello! Creating a simple web application using streamlit library")

#Text input
names=st.text_input("Enter your name:")
#number input
age=st.text_input("Enter your age:")

#display a message when button is clicked
if st.button("submit"):
 st.write("Hello,{name}! Welcome to streamlit.")
