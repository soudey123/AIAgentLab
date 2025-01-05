import streamlit as st
import pandas as pd
from openai import OpenAI
import requests

# Set page configuration
st.set_page_config(page_title="AI Data Analyzer", layout="wide")

# App title
st.title("AI Data Analyzer")

# Sidebar for API Key input
st.sidebar.header("Configuration")
api_provider = st.sidebar.selectbox("Select API Provider", ["OpenAI", "Gemini", "Claude", "Grok", "Perplexity"])
api_key = st.sidebar.text_input(f"Enter your {api_provider} API Key", type="password")

# Initialize OpenAI client
client = None

# Function to set API keys based on the provider
def set_api_key(provider, key):
    global client
    if provider == "OpenAI":
        client = OpenAI(api_key=key)
    elif provider == "Gemini":
        # Placeholder for Gemini API setup
        st.sidebar.info("Gemini API setup in progress.")
    elif provider == "Claude":
        # Placeholder for Claude API setup
        st.sidebar.info("Claude API setup in progress.")
    elif provider == "Grok":
        # Placeholder for Grok API setup
        st.sidebar.info("Grok API setup in progress.")
    elif provider == "Perplexity":
        # Placeholder for Perplexity API setup
        st.sidebar.info("Perplexity API setup in progress.")

if api_key:
    set_api_key(api_provider, api_key)

# Upload data file
uploaded_file = st.file_uploader("Upload your data file (CSV, Excel, or TXT):", type=["csv", "xlsx", "xls", "txt"])

def load_data(file):
    """Load data from uploaded file."""
    if file.name.endswith(".csv"):
        return pd.read_csv(file)
    elif file.name.endswith(".xlsx") or file.name.endswith(".xls"):
        return pd.read_excel(file)
    elif file.name.endswith(".txt"):
        return pd.read_csv(file, delimiter="\t")
    else:
        st.error("Unsupported file format.")
        return None

if uploaded_file:
    try:
        data = load_data(uploaded_file)
        st.write("### Data Preview")
        st.dataframe(data.head())

        st.write("### Data Analysis")
        query = st.text_area("Enter your analysis query:", "E.g., Summarize the dataset, find correlation, etc.")

        if st.button("Analyze Data"):
            if not api_key:
                st.error("Please enter your API Key in the sidebar.")
            else:
                try:
                    if api_provider == "OpenAI":
                        prompt = f"Analyze the following dataset and answer the query.\n\nDataset:\n{data.head(10).to_csv(index=False)}\n\nQuery:\n{query}"
                        response = client.chat.completions.create(
                            model="gpt-4",
                            messages=[
                                {"role": "system", "content": "You are a helpful data analysis assistant."},
                                {"role": "user", "content": prompt}
                            ],
                            max_tokens=1500,
                            temperature=0.7
                        )
                        st.write("### Analysis Result")
                        st.write(response.choices[0].message.content.strip())
                    elif api_provider in ["Gemini", "Claude", "Grok", "Perplexity"]:
                        st.error(f"Support for {api_provider} API provider is under development.")
                    else:
                        st.error("Invalid API provider selected.")
                except Exception as e:
                    st.error(f"An error occurred: {e}")
    except Exception as e:
        st.error(f"Failed to load data: {e}")

# Footer
st.sidebar.markdown("---")
st.sidebar.markdown("Developed by [Your Name]")
st.sidebar.markdown("Source Code: [GitHub Repository](https://github.com/yourusername/ai-data-analyzer)")
