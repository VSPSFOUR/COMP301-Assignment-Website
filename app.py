import streamlit as st
import requests
import os
# from auther import auth_required, login_page, register_page, logout

# Hugging Face API setup
API_URL = "https://z3btxq6gum8uwx2e.us-east-1.aws.endpoints.huggingface.cloud"
headers = {
    "Accept": "application/json",
    "Authorization": "Bearer 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",
    "Content-Type": "application/json"
}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

st.title("Llama-enhanced Finance Assistant")

# Initialize session state for login
# if 'logged_in' not in st.session_state:
#     st.session_state.logged_in = False

# Authentication sidebar
# if not st.session_state.logged_in:
#     auth_option = st.sidebar.radio("Choose an option", ["Login", "Register"])
#     if auth_option == "Login":
#         login_page()
#     else:
#         register_page()
# else:
#     st.sidebar.write(f"Welcome, {st.session_state.username}!")
#     if st.sidebar.button("Logout"):
#         logout()

# @auth_required

def main_app():
    # User context (now associated with the logged-in user)
    if 'user_context' not in st.session_state:
        st.session_state.user_context = {
            'age': 30,
            'income': 50000,
            'savings': 10000,
            'risk_tolerance': "Medium"
        }

    # Sidebar for user context
    st.sidebar.header("User Context")
    st.session_state.user_context['age'] = st.sidebar.slider("Age", 18, 100, st.session_state.user_context['age'])
    st.session_state.user_context['income'] = st.sidebar.number_input("Annual Income (ZAR)", min_value=0, value=st.session_state.user_context['income'])
    st.session_state.user_context['savings'] = st.sidebar.number_input("Current Savings (ZAR)", min_value=0, value=st.session_state.user_context['savings'])
    st.session_state.user_context['risk_tolerance'] = st.sidebar.select_slider("Risk Tolerance", options=["Low", "Medium", "High"], value=st.session_state.user_context['risk_tolerance'])

    user_context = f"User is {st.session_state.user_context['age']} years old, with an annual income of ZAR {st.session_state.user_context['income']}, current savings of ZAR {st.session_state.user_context['savings']}, and a {st.session_state.user_context['risk_tolerance'].lower()} risk tolerance."

    # Main content

    st.header("Private Advisory")
    query_input = st.text_input("Enter your finance-related query:")
    
    if st.button("Search"):
        # prompt = f"As a finance expert, please answer the following query: {query_input}"
        prompt = f"As a finance expert, answer the following query with context that the {user_context}: {query_input}"

        response = query({"inputs": prompt})
        st.write("Answer:", response[0]["output"][0])
        
        
        
    # Disclaimer
    st.sidebar.markdown("---")
    st.sidebar.write("Disclaimer: This app provides general information and is not a substitute for professional financial advice.")

if __name__ == "__main__":
    main_app()
