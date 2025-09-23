import pandas as pd
import streamlit as st
import plotly.express as px


book_df = pd.read_csv('bestsellers_with_categories_2022_03_27.csv')

st.title('Bestselling Book Analysis')
st.write("This is a simple app for analyzing bestselling books.")


st.sidebar.header("Add a New Book")
with st.sidebar.form("book_form"):
    new_name = st.text_input("Book Name")
    new_author = st.text_input("Author Name")
    new_user_rating = st.slider("User Rating", 0.5, 5.0, 3.0, 0.1)
    new_reviews = st.number_input("Number of Reviews", min_value=0, step=1)
    new_price = st.number_input("Price", min_value=1, step=1)
    new_year = st.number_input("Year", min_value=2009, max_value=2025)
    new_genre = st.selectbox("Genre", book_df['Genre'].unique())
    submit_button = st.form_submit_button(label="Add Book")

    if submit_button:
        new_data = {
            'Name': new_name,
            'Author': new_author,
            'User Rating': new_user_rating,
            'Reviews': new_reviews,
            'Price': new_price,
            'Year': new_year,
            'Genre': new_genre
        }

        book_df = pd.concat([book_df, pd.DataFrame([new_data])], ignore_index=True)

        book_df.to_csv('bestsellers_with_categories_2022_03_27.csv', index=False)

        st.sidebar.success("New book has been added!")
