import streamlit as st
import pandas


st.set_page_config(layout="wide")

st.header("The Best Company")
st.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit, "
         "sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. "
         "Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. "
         "Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. "
         "Excepteur sint occaecat cupidatat non proident, "
         "sunt in culpa qui officia deserunt mollit anim id est laborum.")

st.subheader("Our Team")

col1, col2, col3 = st.columns(3)

# Use Pandas to read the data.csv and separate information using ";"

df = pandas.read_csv("data.csv")

with col1:
    for index, row in df[:4].iterrows():
        # Another way to do the next 2 lines below in a single line:
        # st.subheader(f'{row["first name"].title()} {row["last name"].title()}')
        full_name = str(row["first name"] +" "+row["last name"])
        st.subheader(full_name.title())
        st.write(row["role"])
        st.image("images/" + row["image"])

with col2:
    for index, row in df[4:8].iterrows():
        full_name = str(row["first name"] +" "+row["last name"])
        st.subheader(full_name.title())
        st.write(row["role"])
        st.image("images/" + row["image"])

with col3:
    for index, row in df[8:].iterrows():
        full_name = str(row["first name"] +" "+row["last name"])
        st.subheader(full_name.title())
        st.write(row["role"])
        st.image("images/" + row["image"])
