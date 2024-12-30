import streamlit as st
from datetime import datetime
from src.tools import ResearchTools

# Set up the app configuration
st.set_page_config(page_title="Research Article Finder", layout="wide")
st.title("Research Article Finder")

# Sidebar for user inputs
st.sidebar.header("Search Criteria")

# Predefined topics
topic_choices = [
    "Machine Learning",
    "Artificial Intelligence",
    "Data Science",
    "Healthcare Analytics",
    "Physics",
    "Biology",
    "Mathematics",
    "Engineering",
    "Economics",
    "Other (Specify below)"
]

# Topic selection
selected_topic = st.sidebar.selectbox("Select a topic:", topic_choices)

# Custom topic input if "Other" is selected
if selected_topic == "Other (Specify below)":
    custom_topic = st.sidebar.text_input("Enter your custom topic:")
    query = custom_topic.strip() if custom_topic else ""
else:
    query = selected_topic

# Date range inputs
start_date = st.sidebar.date_input("Start date", value=datetime(2023, 1, 1))
end_date = st.sidebar.date_input("End date", value=datetime.now())

# Validation for date range
if start_date > end_date:
    st.error("Start date cannot be after the end date. Please adjust the date range.")
    st.stop()

# Number of articles to fetch
max_results = st.sidebar.slider("Number of articles to fetch:", min_value=1, max_value=50, value=20)

# Search button to fetch articles
if st.sidebar.button("Search Articles"):
    with st.spinner("Fetching articles..."):
        try:
            # Fetch articles using ResearchTools
            articles = ResearchTools.search_google_scholar(query, start_date, end_date, max_results)

            # Check if articles are found
            if not articles:
                st.warning("No articles found. Please adjust your search criteria.")
            else:
                # Sort articles by citation count in descending order
                articles.sort(key=lambda x: x.citation_count or 0, reverse=True)

                # Display articles in a tabular format
                st.write(f"### Articles for topic: {query}")
                st.write("Below is the list of articles matching your search criteria:")

                # Prepare table data
                table_data = []
                for article in articles:
                    title = article.title or "Unknown Title"
                    journal = article.journal or "Unknown Journal"
                    year = article.publication_date.year if article.publication_date else "Unknown Year"
                    citations = article.citation_count or 0
                    link = article.url or "#"
                    clickable_link = f"[Read Here]({link})"
                    table_data.append([title, journal, year, citations, clickable_link])

                # Render articles in a table
                st.write(
                    """
                    <style>
                    table {
                        width: 100%;
                        border-collapse: collapse;
                    }
                    th, td {
                        border: 1px solid #ddd;
                        text-align: left;
                        padding: 8px;
                    }
                    th {
                        background-color: #f2f2f2;
                    }
                    </style>
                    """,
                    unsafe_allow_html=True,
                )

                # Convert table data into markdown format
                table_header = "| Title | Journal & Authors | Published Year | Citations | Link |\n|-------|---------|----------------|-----------|------|"
                table_rows = "\n".join(
                    f"| {row[0]} | {row[1]} | {row[2]} | {row[3]} | {row[4]} |"
                    for row in table_data
                )
                st.markdown(f"{table_header}\n{table_rows}", unsafe_allow_html=True)
        except Exception as e:
            st.error(f"An error occurred while fetching articles: {e}")

# Footer
st.sidebar.write("---")
st.sidebar.info("Powered by SERPAPI and Streamlit.")