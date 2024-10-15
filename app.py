import streamlit as st
import requests
import os
import pandas as pd
import yfinance as yf
import plotly.graph_objects as go
from auther import auth_required, login_page, register_page, logout

# Hugging Face API setup
API_URL = "https://z3btxq6gum8uwx2e.us-east-1.aws.endpoints.huggingface.cloud"
headers = {
    "Accept": "application/json",
    "Authorization": f"Bearer {os.getenv('HUGGINGFACE_API_KEY')}",
    "Content-Type": "application/json"
}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

def get_stock_data(ticker, period='1y'):
    stock = yf.Ticker(ticker)
    hist = stock.history(period=period)
    return hist

def plot_stock_data(data, ticker):
    fig = go.Figure(data=[go.Candlestick(x=data.index,
                open=data['Open'],
                high=data['High'],
                low=data['Low'],
                close=data['Close'])])
    fig.update_layout(title=f"{ticker} Stock Price", xaxis_title="Date", yaxis_title="Price")
    return fig

st.title("GPT-enhanced Finance Assistant")

# Initialize session state for login
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

# Authentication sidebar
if not st.session_state.logged_in:
    auth_option = st.sidebar.radio("Choose an option", ["Login", "Register"])
    if auth_option == "Login":
        login_page()
    else:
        register_page()
else:
    st.sidebar.write(f"Welcome, {st.session_state.username}!")
    if st.sidebar.button("Logout"):
        logout()

@auth_required
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
    st.session_state.user_context['income'] = st.sidebar.number_input("Annual Income ($)", min_value=0, value=st.session_state.user_context['income'])
    st.session_state.user_context['savings'] = st.sidebar.number_input("Current Savings ($)", min_value=0, value=st.session_state.user_context['savings'])
    st.session_state.user_context['risk_tolerance'] = st.sidebar.select_slider("Risk Tolerance", options=["Low", "Medium", "High"], value=st.session_state.user_context['risk_tolerance'])

    user_context = f"User is {st.session_state.user_context['age']} years old, with an annual income of ${st.session_state.user_context['income']}, current savings of ${st.session_state.user_context['savings']}, and a {st.session_state.user_context['risk_tolerance'].lower()} risk tolerance."

    # Main content
    tab1, tab2, tab3 = st.tabs(["Web Supplementation", "Private Advisory", "Stock Analysis"])

    with tab1:
        st.header("Web Supplementation")
        query_input = st.text_input("Enter your finance-related query:")
        if st.button("Search"):
            prompt = f"As a finance expert, please answer the following query: {query_input}"
            response = query({"inputs": prompt})
            st.write("Answer:", response[0]['generated_text'])

    with tab2:
        st.header("Private Advisory")
        advice_query = st.text_area("What financial advice do you need?")
        if st.button("Get Advice"):
            prompt = f"{user_context}\n\nAs a personal finance assistant, please provide advice on the following: {advice_query}"
            response = query({"inputs": prompt})
            st.write("Advice:", response[0]['generated_text'])

    with tab3:
        st.header("Stock Analysis")
        ticker = st.text_input("Enter stock ticker (e.g., AAPL for Apple):")
        if st.button("Analyze"):
            data = get_stock_data(ticker)
            st.plotly_chart(plot_stock_data(data, ticker))
            
            prompt = f"Provide a brief analysis of {ticker} stock based on recent performance."
            response = query({"inputs": prompt})
            st.write("Analysis:", response[0]['generated_text'])

    # Disclaimer
    st.sidebar.markdown("---")
    st.sidebar.write("Disclaimer: This app provides general information and is not a substitute for professional financial advice.")

if __name__ == "__main__":
    main_app()