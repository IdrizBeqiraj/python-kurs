import streamlit as st


if  st.checkbox("Click me"):
    st.write("The button has been clicked")

if  st.button("Click mee"):
    st.write("The button has been clicked")

user_input = st.text_input("enter a text", "Sample Text")

st.write("You entered:" , user_input)

age = st.number_input ("Enter a number", min_value=0, max_value=100)
st.write(f"Your Age is : {age}")

if st.button("Succes"):
    st.success("Operation was successful")

