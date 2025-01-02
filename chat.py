import streamlit as st
import google.generativeai as genai

# Gemini API key input in the sidebar
st.sidebar.title("Settings")
gemini_api_key = st.sidebar.text_input("Enter Gemini API Key", type="password")

# Configure the Gemini API key if provided
if gemini_api_key:
    genai.configure(api_key=gemini_api_key)

# Function to generate response using the Gemini model
def generate_response(message):
    try:
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(message)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"

# Function to generate summary using the Gemini model
def generate_summary(message):
    try:
        model = genai.GenerativeModel("gemini-1.5-flash")
        summary = model.generate_content(f"Summarize the following message:\n\n{message}")
        return summary.text
    except Exception as e:
        return f"Error: {str(e)}"

# Streamlit app layout
st.title("LangGraph Chatbot Response and Summarization")

message = st.text_area("Write your message here:")

if st.button("Get Response"):
    if gemini_api_key:
        response_text = generate_response(message)
        st.write("**Response:**", response_text)
    else:
        st.warning("Please enter your Gemini API Key!")

if st.button("Get Summary"):
    if gemini_api_key:
        summary_text = generate_summary(message)
        st.write("**Summary:**", summary_text)
    else:
        st.warning("Please enter your Gemini API Key!")
