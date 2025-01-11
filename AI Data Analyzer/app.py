import streamlit as st
import pandas as pd
import openai
import plotly.express as px
import time

# Set page config with custom theme
st.set_page_config(
    page_title="AI Data Analyzer",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .stButton>button {
        width: 100%;
        background-color: #ff4b4b;
        color: white;
    }
    .stTextInput>div>div>input {
        background-color: #f0f2f6;
    }
    </style>
    """, unsafe_allow_html=True)

# Title with emoji and styling
st.title("🤖 AI Data Analyzer")
st.markdown("### Transform your data insights with AI 📊")

# Sidebar for configuration
with st.sidebar:
    st.header("⚙️ Configuration")
    api_key = st.text_input("Enter OpenAI API Key", type="password")
    uploaded_file = st.file_uploader("Upload your CSV file 📁", type="csv")
    
    if api_key:
        st.success("API Key set successfully! ✅")

# Main content area
if uploaded_file is not None:
    # Load and display data with loading animation
    with st.spinner('Loading data...'):
        df = pd.read_csv(uploaded_file)
        time.sleep(1)  # Simulate processing
    
    st.success("Data loaded successfully! 🎉")
    
    # Data preview in an expander
    with st.expander("Preview Data 👀"):
        st.dataframe(df.head())
        st.info(f"Total rows: {len(df)} | Total columns: {len(df.columns)}")
    
    # Query input with placeholder
    user_query = st.text_area(
        "Ask anything about your data 💭",
        placeholder="Example: What are the main trends in this dataset?",
        height=100
    )
    
    if st.button("Analyze 🔍"):
        if not api_key:
            st.error("Please enter your OpenAI API key in the sidebar! ⚠️")
        else:
            try:
                # Loading animation while processing
                with st.spinner('AI is analyzing your data...'):
                    #client = OpenAI(api_key=api_key)
                    openai.api_key = api_key
                    
                    # Create context about the data
                    data_info = f"""
                    Columns in dataset: {', '.join(df.columns)}
                    Data sample: {df.head(3).to_string()}
                    Data description: {df.describe().to_string()}
                    """
                    
                    # Get AI response
                    #response = client.chat.completions.create(
                    response = openai.ChatCompletion.create(
                        model="gpt-4-turbo",
                        messages=[
                            {"role": "system", "content": "You are a data analysis expert. Provide clear, concise insights about the data."},
                            {"role": "user", "content": f"Data information: {data_info}\n\nUser query: {user_query}"}
                        ]
                    )
                    
                    # Display response in a nice box
                    st.markdown("### 🤖 AI Analysis")
                    st.markdown(f">{response.choices[0].message.content}", unsafe_allow_html=True)
                    
                    # Generate a relevant visualization if possible
                    if len(df.columns) >= 2:
                        st.markdown("### 📈 Visualization")
                        fig = px.line(df, x=df.columns[0], y=df.columns[1], title="Data Trend")
                        st.plotly_chart(fig, use_container_width=True)
                
                st.balloons()  # Celebration effect!
                
            except Exception as e:
                st.error(f"An error occurred: {str(e)} ❌")
                
else:
    # Welcome message when no file is uploaded
    st.info("👆 Please upload a CSV file to get started!")
    
# Footer
st.markdown("---")
st.markdown("Made with ❤️ by Sam Dey")
