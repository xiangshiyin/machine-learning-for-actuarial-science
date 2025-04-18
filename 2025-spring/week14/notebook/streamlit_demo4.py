import streamlit as st

# Add a selectbox to the sidebar:
add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?", ("Email", "Home phone", "Mobile phone")
)

# Add a slider to the sidebar:
add_slider = st.sidebar.slider("Select a range of values", 0.0, 100.0, (25.0, 75.0))

min_value, max_value = add_slider

st.write(f"You selected: {add_selectbox}")
st.write(f"Selected range: {min_value} to {max_value}")
