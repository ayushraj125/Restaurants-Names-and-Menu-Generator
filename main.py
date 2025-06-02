import streamlit as st
import deepinfra_langchain  # Your module with the generate function

st.title("Restaurant Name Generator")


cuisine = st.selectbox("Pick a Cuisine", ("", "Indian", "Italian", "Mexican", "Arabic", "American"))

# Adding a button to trigger generation
if st.button("Generate Restaurant Name and Menu") and cuisine:
    response = deepinfra_langchain.generate_restaurant_name_and_items(cuisine)
    st.header(response['restaurant_name'].strip())
    
    menu_items = [item.strip() for item in response['menu_items'].split(",")]
    st.write("**Menu Items**")
    for item in menu_items:
        st.write("-", item)
elif cuisine == "":
    st.info("Please select a cuisine to get started.")
