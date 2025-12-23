# 📊 Data Intelligence App

> AI-Powered Business Intelligence Platform with Multi-Agent System

A comprehensive data analytics and business intelligence application built with Streamlit and powered by PandasAI's multi-agent system. This application enables users to connect to multiple data sources, perform exploratory data analysis, and leverage AI for intelligent insights.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.29+-red.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

## 🎯 Features

### 📁 Multi-Source Data Connectivity
- **File Upload**: CSV, Excel (XLSX/XLS), JSON, Parquet
- **Database Connections**: PostgreSQL, MySQL, SQLite, SQL Server
- **REST API Integration**: Connect to external APIs with authentication support
- **Sample Datasets**: Pre-loaded sample data for quick testing

### 🤖 Multi-Agent AI System
- **Statistical Agent**: Automated statistical analysis and metrics
- **Pattern Recognition Agent**: Correlation analysis and trend detection
- **Insight Generation Agent**: Automated insights and data profiling
- **Predictive Agent**: Forecasting and predictive analytics
- **Natural Language Agent**: Query data using plain English

### 🔍 Exploratory Data Analysis
- **Data Overview**: Comprehensive dataset profiling
- **Statistical Summary**: Descriptive statistics for all columns
- **Data Quality Assessment**: Missing data, duplicates, outliers detection
- **Correlation Analysis**: Identify relationships between variables
- **Distribution Analysis**: Visualize data distributions

### 📈 Advanced Visualizations
- **Interactive Charts**: Line, Bar, Scatter, Box, Histogram, Area
- **Statistical Plots**: Heatmaps, Correlation matrices, Pair plots
- **3D Visualizations**: 3D scatter plots for multi-dimensional analysis
- **Customizable**: Multiple configuration options for each chart type

### 📊 Automated Reporting
- **Comprehensive Reports**: Generate detailed analysis reports
- **Multiple Formats**: HTML, Markdown, PDF support
- **Customizable Sections**: Choose which sections to include
- **Downloadable**: Export reports for sharing

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/Data-Intelligence-App.git
   cd Data-Intelligence-App
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv

   # On Windows
   venv\Scripts\activate

   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application

```bash
streamlit run app.py
```

The application will open in your default web browser at `http://localhost:8501`

## 📖 Usage Guide

### 1. Loading Data

#### From Files
1. Navigate to **"Data Sources"** → **"File Upload"** tab
2. Upload your CSV, Excel, JSON, or Parquet file
3. Give your dataset a name
4. Click **"Load Dataset"**

#### From Database
1. Navigate to **"Data Sources"** → **"Database"** tab
2. Select your database type
3. Enter connection details (host, port, database, credentials)
4. Write your SQL query
5. Click **"Connect & Execute"**

#### From API
1. Navigate to **"Data Sources"** → **"API"** tab
2. Enter the API endpoint URL
3. Configure authentication if required
4. Click **"Fetch Data"**

#### Sample Data
1. Navigate to **"Data Sources"** → **"Sample Data"** tab
2. Choose from available sample datasets
3. Click **"Load Sample"**

### 2. Exploratory Data Analysis

1. Navigate to **"Exploratory Analysis"**
2. Explore different tabs:
   - **Overview**: Dataset structure and column information
   - **Statistics**: Descriptive statistics for numeric columns
   - **Data Quality**: Missing data, duplicates, outliers
   - **Correlations**: Correlation matrix and analysis
   - **Distributions**: Distribution plots and statistics

### 3. AI-Powered Analysis

1. Navigate to **"AI Analysis"**
2. Enter your question in natural language, for example:
   - "What are the top 5 products by sales?"
   - "Show me the correlation between age and income"
   - "What's the average revenue by region?"
   - "Identify outliers in the price column"
   - "Generate a summary of key insights"
3. Click **"Analyze"**
4. View the results, visualizations, and insights

### 4. Creating Visualizations

1. Navigate to **"Visualizations"**
2. Select visualization type from the dropdown
3. Configure the chart:
   - Select columns for X and Y axes
   - Choose grouping/color options
   - Adjust settings (bins, aggregations, etc.)
4. The chart will update interactively

### 5. Generating Reports

1. Navigate to **"Reports"**
2. Select sections to include in your report
3. Choose output format (HTML, Markdown, PDF)
4. Click **"Generate Report"**
5. Download the generated report

## 🏗️ Project Structure

```
Data-Intelligence-App/
│
├── app.py                          # Main Streamlit application
├── requirements.txt                # Python dependencies
├── README.md                      # This file
│
├── src/                           # Source modules
│   ├── __init__.py
│   ├── data_connectors.py         # Data source connectors
│   ├── multi_agent_system.py     # AI multi-agent system
│   ├── exploratory_analysis.py   # EDA functionality
│   ├── visualizations.py         # Visualization engine
│   └── report_generator.py       # Report generation
│
└── data/                          # Data directory
    ├── uploaded/                  # Uploaded files
    └── exports/                   # Exported reports
```

## 🔧 Configuration

### Database Drivers

For database connectivity, ensure you have the appropriate drivers installed:

- **PostgreSQL**: `psycopg2-binary` (included in requirements.txt)
- **MySQL**: `pymysql` (included in requirements.txt)
- **SQL Server**: `pyodbc` (requires ODBC Driver 17 for SQL Server)
- **SQLite**: Built-in with Python

### API Keys

If using PandasAI with LLM integration, set your API key as an environment variable:

```bash
export PANDASAI_API_KEY="your-api-key-here"
```

Or create a `.env` file:

```
PANDASAI_API_KEY=your-api-key-here
```

## 🤖 Multi-Agent System

The application uses a sophisticated multi-agent system for data analysis:

### Agent Types

1. **Statistical Agent**
   - Calculates descriptive statistics
   - Performs aggregations (mean, median, sum, etc.)
   - Handles statistical queries

2. **Pattern Recognition Agent**
   - Identifies correlations and relationships
   - Detects trends in time series data
   - Recognizes data patterns

3. **Insight Generation Agent**
   - Generates automated insights
   - Performs data profiling
   - Identifies data quality issues

4. **Predictive Agent**
   - Time series forecasting
   - Trend analysis
   - Anomaly detection

5. **Natural Language Agent**
   - Processes natural language queries
   - Handles general data questions
   - Provides flexible query interface

## 📊 Visualization Types

| Visualization | Best For | Key Features |
|--------------|----------|--------------|
| Line Chart | Time series, trends | Multiple series, grouping |
| Bar Chart | Categorical comparisons | Aggregations, grouping |
| Scatter Plot | Relationships, correlations | Trendlines, color/size encoding |
| Box Plot | Distribution, outliers | Group comparisons |
| Histogram | Distribution analysis | Adjustable bins, marginal plots |
| Heatmap | Correlations, matrices | Color scales, annotations |
| Pie Chart | Proportions, composition | Top N categories |
| Area Chart | Cumulative trends | Stacked areas |
| 3D Scatter | Multi-dimensional analysis | 3-axis visualization |
| Pair Plot | Multi-variable relationships | Matrix of scatter plots |

## 🛠️ Advanced Features

### Custom Data Transformations

The application supports various data transformations:
- Filtering and sorting
- Group-by aggregations
- Missing data imputation
- Outlier detection and handling

### Export Capabilities

- Export processed datasets
- Download analysis results
- Save visualizations
- Generate comprehensive reports

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Powered by [PandasAI](https://github.com/gventuri/pandas-ai)
- Visualizations by [Plotly](https://plotly.com/)
- Data processing with [Pandas](https://pandas.pydata.org/)

## 📧 Support

For support, please open an issue in the GitHub repository or contact the maintainers.

## 🗺️ Roadmap

- [ ] Cloud storage integration (AWS S3, Google Cloud Storage, Azure Blob)
- [ ] Advanced machine learning models
- [ ] Real-time data streaming
- [ ] Collaborative features
- [ ] Custom dashboard builder
- [ ] Scheduled reports
- [ ] Data pipeline automation
- [ ] Enhanced security features
- [ ] Multi-user support
- [ ] API endpoints for programmatic access

## 📚 Documentation

For detailed documentation on each component:

- [Data Connectors](docs/data_connectors.md)
- [Multi-Agent System](docs/multi_agent_system.md)
- [Visualization Guide](docs/visualizations.md)
- [API Reference](docs/api_reference.md)

---

**Built with ❤️ using Streamlit and PandasAI**
