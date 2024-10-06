
import streamlit as st

# Title of the app
st.title("COMP301 - Project - Fine-Tuned LLM")
st.write("Financial Advisor")

# Sidebar menu
st.sidebar.title("Sidebar Menu")
st.sidebar.button("Button in Sidebar")
st.sidebar.slider("Slider in Sidebar")

# Check if there is a previous output
if 'output_text' not in st.session_state:
    st.session_state.output_text = ""

# Display the output text first
st.write("OUT TEXT: ", st.session_state.output_text)

# Create a form to align the input and button
with st.form(key='my_form'):
    # Create two columns within the form
    col1, col2 = st.columns([3, 1])  # You can adjust the ratios to control the width

    # Place input text box in the first column
    with col1:
        text_test = st.text_input("")

    # Place button in the second column (to the right of the input box)
    with col2:
        submit_button = st.form_submit_button("Submit")

# Update output text when the button is pressed
if submit_button:
    st.session_state.output_text = text_test  # Update output text
