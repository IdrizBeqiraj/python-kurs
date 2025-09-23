import pandas as pd

book_df = pd.read_csv('bestsellers_with_categories_2022_03_27.csv')

st.title('Bestselling book analysis')
st.write("This is a simple app for ......")

#sidebar

st.sidebar.header("add a new book")
with st.sidebar.form("book form"):
    new_name = st.text_input("Book Name")
    new_author = st.text_input("Author name")
    new_user_rating = st.slider("user rating", 0.5 , 5.0 , 0.0 , 0.1)
    new_reviews = st.number_input("Num Inputs", min_value=0, step=1)
    new_price = st.number_input("Price", min_value)