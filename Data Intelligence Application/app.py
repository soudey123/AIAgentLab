"""
Data Intelligence App - AI-Powered Business Intelligence Platform
Built with Streamlit and PandasAI Multi-Agent System
"""

import streamlit as st
import pandas as pd
import os
from pathlib import Path

# Configure page
st.set_page_config(
    page_title="Data Intelligence App",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Create necessary directories
Path("data/uploaded").mkdir(parents=True, exist_ok=True)
Path("data/exports").mkdir(parents=True, exist_ok=True)

# Import modules
from src.data_connectors import DataConnector
from src.multi_agent_system import DataAnalysisAgent
from src.exploratory_analysis import ExploratoryAnalysis
from src.visualizations import VisualizationEngine

# Initialize session state
if 'datasets' not in st.session_state:
    st.session_state.datasets = {}
if 'current_dataset' not in st.session_state:
    st.session_state.current_dataset = None
if 'analysis_history' not in st.session_state:
    st.session_state.analysis_history = []

def main():
    """Main application entry point"""

    # Sidebar
    with st.sidebar:
        st.title("📊 Data Intelligence App")
        st.markdown("---")

        # Navigation
        page = st.radio(
            "Navigation",
            ["🏠 Home", "📁 Data Sources", "🔍 Exploratory Analysis",
             "🤖 AI Analysis", "📈 Visualizations", "📊 Reports"]
        )

        st.markdown("---")

        # Dataset selector
        if st.session_state.datasets:
            st.subheader("Active Datasets")
            dataset_names = list(st.session_state.datasets.keys())
            selected = st.selectbox(
                "Select Dataset",
                dataset_names,
                index=dataset_names.index(st.session_state.current_dataset)
                if st.session_state.current_dataset in dataset_names else 0
            )
            st.session_state.current_dataset = selected

            # Dataset info
            df = st.session_state.datasets[selected]
            st.metric("Rows", df.shape[0])
            st.metric("Columns", df.shape[1])
        else:
            st.info("No datasets loaded. Start by connecting to a data source!")

    # Main content area
    if page == "🏠 Home":
        show_home()
    elif page == "📁 Data Sources":
        show_data_sources()
    elif page == "🔍 Exploratory Analysis":
        show_exploratory_analysis()
    elif page == "🤖 AI Analysis":
        show_ai_analysis()
    elif page == "📈 Visualizations":
        show_visualizations()
    elif page == "📊 Reports":
        show_reports()

def show_home():
    """Home page"""
    st.title("Welcome to Data Intelligence App 🚀")

    st.markdown("""
    ### Your AI-Powered Business Intelligence Platform

    This application leverages **multi-agent AI systems** to provide comprehensive data analysis capabilities:

    #### 🎯 Key Features:

    - **📁 Multiple Data Sources**: Connect to CSV, Excel, SQL databases, APIs, and more
    - **🤖 AI-Powered Analysis**: Multi-agent system for intelligent data exploration
    - **🔍 Exploratory Analysis**: Automated statistical analysis and data profiling
    - **📈 Advanced Visualizations**: Interactive charts and dashboards
    - **💡 Natural Language Queries**: Ask questions about your data in plain English
    - **📊 Automated Reporting**: Generate comprehensive analysis reports

    #### 🚀 Getting Started:

    1. **Connect Data**: Go to "Data Sources" to import or connect to your data
    2. **Explore**: Use "Exploratory Analysis" for automated insights
    3. **Ask Questions**: Use "AI Analysis" to query your data using natural language
    4. **Visualize**: Create interactive visualizations in "Visualizations"
    5. **Report**: Generate comprehensive reports in "Reports"

    ---
    """)

    # Quick stats
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Datasets Loaded", len(st.session_state.datasets))
    with col2:
        total_rows = sum(df.shape[0] for df in st.session_state.datasets.values())
        st.metric("Total Rows", f"{total_rows:,}")
    with col3:
        st.metric("Analyses Performed", len(st.session_state.analysis_history))
    with col4:
        st.metric("Status", "🟢 Active")

    st.markdown("---")

    # Recent activity
    if st.session_state.analysis_history:
        st.subheader("📋 Recent Analysis History")
        for i, analysis in enumerate(reversed(st.session_state.analysis_history[-5:])):
            with st.expander(f"Analysis {len(st.session_state.analysis_history) - i}: {analysis.get('type', 'Unknown')}"):
                st.write(f"**Dataset**: {analysis.get('dataset', 'N/A')}")
                st.write(f"**Time**: {analysis.get('timestamp', 'N/A')}")
                st.write(f"**Query**: {analysis.get('query', 'N/A')}")

def show_data_sources():
    """Data sources connection page"""
    st.title("📁 Data Sources")

    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "📄 File Upload", "🗄️ Database", "🌐 API", "☁️ Cloud Storage", "📊 Sample Data"
    ])

    with tab1:
        st.subheader("Upload Data Files")
        connector = DataConnector()

        uploaded_file = st.file_uploader(
            "Choose a file",
            type=['csv', 'xlsx', 'xls', 'json', 'parquet'],
            help="Upload CSV, Excel, JSON, or Parquet files"
        )

        if uploaded_file:
            try:
                df = connector.load_file(uploaded_file)

                dataset_name = st.text_input(
                    "Dataset Name",
                    value=uploaded_file.name.split('.')[0]
                )

                if st.button("Load Dataset"):
                    st.session_state.datasets[dataset_name] = df
                    st.session_state.current_dataset = dataset_name
                    st.success(f"✅ Dataset '{dataset_name}' loaded successfully!")
                    st.rerun()

                # Preview
                st.subheader("Preview")
                st.dataframe(df.head(10), use_container_width=True)

            except Exception as e:
                st.error(f"Error loading file: {str(e)}")

    with tab2:
        st.subheader("Connect to Database")
        connector = DataConnector()

        db_type = st.selectbox(
            "Database Type",
            ["PostgreSQL", "MySQL", "SQLite", "SQL Server"]
        )

        col1, col2 = st.columns(2)
        with col1:
            host = st.text_input("Host", value="localhost")
            database = st.text_input("Database Name")
            username = st.text_input("Username")
        with col2:
            port = st.number_input("Port", value=5432 if db_type == "PostgreSQL" else 3306)
            password = st.text_input("Password", type="password")

        query = st.text_area(
            "SQL Query",
            value="SELECT * FROM table_name LIMIT 1000",
            height=100
        )

        if st.button("Connect & Execute"):
            try:
                df = connector.load_from_database(
                    db_type, host, port, database, username, password, query
                )
                dataset_name = st.text_input("Dataset Name", value=f"{database}_data")

                if dataset_name:
                    st.session_state.datasets[dataset_name] = df
                    st.session_state.current_dataset = dataset_name
                    st.success(f"✅ Connected and loaded {len(df)} rows!")
                    st.dataframe(df.head(), use_container_width=True)
            except Exception as e:
                st.error(f"Connection error: {str(e)}")

    with tab3:
        st.subheader("Connect to REST API")
        connector = DataConnector()

        url = st.text_input("API URL", placeholder="https://api.example.com/data")

        col1, col2 = st.columns(2)
        with col1:
            method = st.selectbox("Method", ["GET", "POST"])
            auth_type = st.selectbox("Authentication", ["None", "API Key", "Bearer Token"])
        with col2:
            if auth_type == "API Key":
                api_key = st.text_input("API Key", type="password")
            elif auth_type == "Bearer Token":
                token = st.text_input("Token", type="password")

        if st.button("Fetch Data"):
            try:
                df = connector.load_from_api(url, method, auth_type)
                dataset_name = st.text_input("Dataset Name", value="api_data")

                if dataset_name:
                    st.session_state.datasets[dataset_name] = df
                    st.session_state.current_dataset = dataset_name
                    st.success(f"✅ API data loaded successfully!")
                    st.dataframe(df.head(), use_container_width=True)
            except Exception as e:
                st.error(f"API error: {str(e)}")

    with tab4:
        st.subheader("Connect to Cloud Storage")
        st.info("🚧 Cloud storage connectors (AWS S3, Google Cloud Storage, Azure Blob) coming soon!")

    with tab5:
        st.subheader("Load Sample Datasets")
        connector = DataConnector()

        sample_datasets = {
            "Iris Dataset": "iris",
            "Titanic Dataset": "titanic",
            "Sales Data": "sales",
            "Customer Analytics": "customers"
        }

        selected_sample = st.selectbox("Choose Sample Dataset", list(sample_datasets.keys()))

        if st.button("Load Sample"):
            try:
                df = connector.load_sample_data(sample_datasets[selected_sample])
                st.session_state.datasets[selected_sample] = df
                st.session_state.current_dataset = selected_sample
                st.success(f"✅ Sample dataset '{selected_sample}' loaded!")
                st.rerun()
            except Exception as e:
                st.error(f"Error: {str(e)}")

def show_exploratory_analysis():
    """Exploratory data analysis page"""
    st.title("🔍 Exploratory Data Analysis")

    if not st.session_state.current_dataset:
        st.warning("Please load a dataset first from the Data Sources page.")
        return

    df = st.session_state.datasets[st.session_state.current_dataset]
    eda = ExploratoryAnalysis(df)

    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "📊 Overview", "📈 Statistics", "🔍 Data Quality", "🔗 Correlations", "📉 Distributions"
    ])

    with tab1:
        st.subheader("Dataset Overview")
        eda.show_overview()

    with tab2:
        st.subheader("Statistical Summary")
        eda.show_statistics()

    with tab3:
        st.subheader("Data Quality Report")
        eda.show_data_quality()

    with tab4:
        st.subheader("Correlation Analysis")
        eda.show_correlations()

    with tab5:
        st.subheader("Distribution Analysis")
        eda.show_distributions()

def show_ai_analysis():
    """AI-powered analysis page"""
    st.title("🤖 AI-Powered Analysis")

    if not st.session_state.current_dataset:
        st.warning("Please load a dataset first from the Data Sources page.")
        return

    df = st.session_state.datasets[st.session_state.current_dataset]

    st.markdown("""
    ### Ask Questions About Your Data in Natural Language

    The multi-agent AI system will analyze your data and provide intelligent insights.

    **Example queries:**
    - "What are the top 5 products by sales?"
    - "Show me the correlation between age and income"
    - "What's the average revenue by region?"
    - "Identify outliers in the price column"
    - "Generate a summary of customer segments"
    """)

    # Initialize agent
    agent = DataAnalysisAgent(df)

    # Query input
    query = st.text_area(
        "Enter your question:",
        height=100,
        placeholder="E.g., What are the key insights from this dataset?"
    )

    col1, col2, col3 = st.columns([1, 1, 4])
    with col1:
        analyze_btn = st.button("🔍 Analyze", type="primary")
    with col2:
        clear_btn = st.button("🗑️ Clear")

    if analyze_btn and query:
        with st.spinner("AI agents are analyzing your data..."):
            try:
                result = agent.analyze(query)

                # Save to history
                from datetime import datetime
                st.session_state.analysis_history.append({
                    'type': 'AI Analysis',
                    'dataset': st.session_state.current_dataset,
                    'query': query,
                    'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    'result': result
                })

                # Display results
                st.success("✅ Analysis Complete!")

                st.subheader("Results")
                st.markdown(result.get('explanation', 'No explanation available'))

                if 'data' in result and result['data'] is not None:
                    st.subheader("Data")
                    st.dataframe(result['data'], use_container_width=True)

                if 'visualization' in result and result['visualization'] is not None:
                    st.subheader("Visualization")
                    st.pyplot(result['visualization'])

                if 'insights' in result:
                    st.subheader("Key Insights")
                    for insight in result['insights']:
                        st.info(f"💡 {insight}")

            except Exception as e:
                st.error(f"Analysis error: {str(e)}")
                st.info("💡 Tip: Try rephrasing your question or check if the column names are correct.")

def show_visualizations():
    """Visualizations page"""
    st.title("📈 Interactive Visualizations")

    if not st.session_state.current_dataset:
        st.warning("Please load a dataset first from the Data Sources page.")
        return

    df = st.session_state.datasets[st.session_state.current_dataset]
    viz_engine = VisualizationEngine(df)

    viz_type = st.selectbox(
        "Select Visualization Type",
        [
            "Line Chart", "Bar Chart", "Scatter Plot", "Box Plot",
            "Histogram", "Heatmap", "Pie Chart", "Area Chart",
            "3D Scatter", "Pair Plot"
        ]
    )

    viz_engine.create_visualization(viz_type)

def show_reports():
    """Reports generation page"""
    st.title("📊 Automated Reports")

    if not st.session_state.current_dataset:
        st.warning("Please load a dataset first from the Data Sources page.")
        return

    df = st.session_state.datasets[st.session_state.current_dataset]

    st.subheader("Generate Comprehensive Analysis Report")

    report_options = st.multiselect(
        "Select Report Sections",
        [
            "Executive Summary",
            "Data Overview",
            "Statistical Analysis",
            "Data Quality Assessment",
            "Correlation Analysis",
            "Key Insights",
            "Visualizations",
            "Recommendations"
        ],
        default=["Executive Summary", "Data Overview", "Key Insights"]
    )

    report_format = st.radio("Report Format", ["HTML", "PDF", "Markdown"])

    if st.button("Generate Report", type="primary"):
        with st.spinner("Generating comprehensive report..."):
            try:
                from src.report_generator import ReportGenerator

                generator = ReportGenerator(df)
                report = generator.generate_report(report_options, report_format)

                st.success("✅ Report generated successfully!")

                if report_format == "HTML":
                    st.components.v1.html(report, height=600, scrolling=True)
                elif report_format == "Markdown":
                    st.markdown(report)

                # Download button
                st.download_button(
                    label="📥 Download Report",
                    data=report,
                    file_name=f"analysis_report_{st.session_state.current_dataset}.{report_format.lower()}",
                    mime="text/html" if report_format == "HTML" else "text/markdown"
                )

            except Exception as e:
                st.error(f"Report generation error: {str(e)}")

if __name__ == "__main__":
    main()
