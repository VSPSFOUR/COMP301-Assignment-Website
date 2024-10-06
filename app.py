
API_URL = "https://z3btxq6gum8uwx2e.us-east-1.aws.endpoints.huggingface.cloud"
import requests
headers = {
	"Accept" : "application/json",
	"Authorization": "Bearer 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",
	"Content-Type": "application/json" 
}
def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()

import streamlit as st

st.title("COMP301 - Project - Fine-Tuned LLM")
st.write("Financial Advisor")

# st.sidebar.title("Sidebar Menu")
# st.sidebar.button("Button in Sidebar")
# st.sidebar.slider("Slider in Sidebar")

if 'output_text' not in st.session_state:
    st.session_state.output_text = ""

st.write("OUT TEXT: ", st.session_state.output_text)

with st.form(key='my_form'):
    col1, col2 = st.columns([3, 1])  

    with col1:
        text_test = st.text_input("")

    with col2:
        submit_button = st.form_submit_button("Submit")
        
        
        
def process_request():
    input_prompt = text_test
    outtext = query({
	"inputs": input_prompt}
)
    st.session_state.output_text = outtext[0]["output"][0]
    
    
if submit_button:
    # st.session_state.output_text = text_test  # Update output text
    process_request()




