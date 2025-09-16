import streamlit as st

# col1 , col2 , col3 , col4 , col5 = st.columns (5 , gap="small", vertical_alignment="center")
#
# with col1:
#     st.header("Colum 1")
#
#     st.write("random content")
# with col2:
#     st.header("Colum 2")
#
#     st.write("random content")
# with col3:
#     st.header("Colum 3")
#
#     st.write("random content")
# with col4:
#     st.header("Colum 4")
#
#     st.write("random content")

#SIDEBAR
# st.sidebar.header("Sidebar")
#
# st.sidebar.write("This is a sidebar")
#
# st.sidebar.selectbox("Choose one option " , ["Option 1" , "Option 2", "Option 3"])
#
# st.sidebar.radio("Go to" , ["Home" , "Data" , "Settings"])

with st.form("my_form", clear_on_sumbit=True):
    name = st.text_input("Name")
    age = st.slider('Age', min_value=0, max_value=100)
    email = st.text_input('Email')
    bio = st.text_area("Short bio")
    terms = st.chechkbox("I agree to terms and ...")

    submit_button = st.form_submit_button(label="Submit")

if submit_button:
    st.write(f'Name:{name}')
    st.write(f'Age:{age}')
    st.write(f'Email:{email}')
    st.write(f'DESC:{bio}')

    if terms:
        st.write("you agree to terms ")
    else:
        st.write("You didn't")