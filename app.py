API_URL = "https://z3btxq6gum8uwx2e.us-east-1.aws.endpoints.huggingface.cloud"
import requests
import streamlit as st

headers = {
    "Accept": "application/json",
    "Authorization": "Bearer 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",
    "Content-Type": "application/json" 
}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

st.title("GPT-enhanced Finance Assistant")
tab1, tab2 = st.tabs(["Private Advisory", "WebSupplementation"])

with tab1:
    st.write("Financial Advisor")

    # Check if 'output_text' exists in session_state
    if 'output_text' not in st.session_state:
        st.session_state.output_text = ""

    st.write("OUT TEXT: ", st.session_state.output_text)

    with st.form(key='my_form'):
        col1, col2 = st.columns([3, 1])

        with col1:
            text_test = st.text_input("", key="private_advisory_input")

        with col2:
            submit_button = st.form_submit_button("Submit")

    def process_request():
        st.session_state.output_text = "PROCESSING..."
        input_prompt = st.session_state.private_advisory_input
        outtext = query({
            "inputs": input_prompt
        })
        st.session_state.output_text = outtext[0]["output"]

    if submit_button:
        process_request()

with tab2:
    st.write("WebSupplementation Advisor")

    # Check if 'wesup_output_text' exists in session_state
    if 'wesup_output_text' not in st.session_state:
        st.session_state.wesup_output_text = ""

    st.write("OUT TEXT: ", st.session_state.wesup_output_text)

    with st.form(key='wesup_form'):
        col1, col2 = st.columns([3, 1])

        with col1:
            wesup_text_test = st.text_input("", key="wesup_input")

        with col2:
            wesup_submit_button = st.form_submit_button("Submit")

    def process_wesup_request():
        st.session_state.wesup_output_text = "PROCESSING..."
        input_prompt = st.session_state.wesup_input
        outtext = query({
            "inputs": input_prompt
        })
        st.session_state.wesup_output_text = outtext[0]["output"]

    if wesup_submit_button:
        process_wesup_request()
