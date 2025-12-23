# 🚀 Quick Start Guide

Get up and running with Data Intelligence App in 5 minutes!

## Step 1: Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/Data-Intelligence-App.git
cd Data-Intelligence-App

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

## Step 2: Run the Application

```bash
streamlit run app.py
```

The app will automatically open in your browser at `http://localhost:8501`

## Step 3: Load Sample Data

1. Click on **"Data Sources"** in the sidebar
2. Go to the **"Sample Data"** tab
3. Select "Iris Dataset" or "Sales Data"
4. Click **"Load Sample"**

## Step 4: Explore Your Data

### Try Exploratory Analysis
1. Click **"Exploratory Analysis"** in the sidebar
2. Navigate through the tabs:
   - **Overview**: See dataset structure
   - **Statistics**: View statistical summaries
   - **Data Quality**: Check for missing data and outliers
   - **Correlations**: Explore relationships between variables
   - **Distributions**: Visualize data distributions

### Ask AI Questions
1. Click **"AI Analysis"** in the sidebar
2. Try these example questions:
   - "What are the average values for each numeric column?"
   - "Show me the correlation between variables"
   - "What are the key insights from this dataset?"
   - "Show me the top 10 records"

### Create Visualizations
1. Click **"Visualizations"** in the sidebar
2. Select a chart type (e.g., "Scatter Plot")
3. Choose your X and Y axes
4. Customize colors and size
5. View your interactive chart!

### Generate a Report
1. Click **"Reports"** in the sidebar
2. Select report sections
3. Choose format (HTML recommended for first try)
4. Click **"Generate Report"**
5. Download your comprehensive analysis report

## Step 5: Load Your Own Data

### Upload a File
1. Go to **"Data Sources"** → **"File Upload"**
2. Upload your CSV, Excel, JSON, or Parquet file
3. Give it a name
4. Click **"Load Dataset"**
5. Start analyzing!

### Connect to a Database
1. Go to **"Data Sources"** → **"Database"**
2. Select your database type
3. Enter connection details
4. Write a SQL query
5. Click **"Connect & Execute"**

## Tips for Best Experience

### Data Preparation
- Ensure your data has column headers
- Remove special characters from column names if possible
- Check for consistent data types within columns

### Performance
- For large datasets (>100K rows), consider filtering or sampling first
- Start with simple visualizations before complex ones
- Use the data quality check to identify issues early

### AI Queries
- Be specific in your questions
- Mention column names explicitly
- Start with simple questions and build complexity

### Visualizations
- Choose the right chart type for your data
- Use color encoding to add dimensions to your analysis
- Enable trendlines for scatter plots to see relationships

## Example Workflows

### Workflow 1: Quick Data Profiling
1. Load data → 2. Go to Exploratory Analysis → 3. Review all tabs → 4. Generate report

### Workflow 2: Finding Correlations
1. Load data → 2. Exploratory Analysis → Correlations tab → 3. Create scatter plot of correlated variables

### Workflow 3: AI-Powered Insights
1. Load data → 2. AI Analysis → 3. Ask "What are the key insights?" → 4. Ask follow-up questions based on results

### Workflow 4: Custom Dashboard
1. Load data → 2. Create multiple visualizations → 3. Screenshot or export each → 4. Compile in report

## Troubleshooting

### Import Errors
```bash
# Reinstall dependencies
pip install -r requirements.txt --upgrade
```

### Database Connection Issues
- Verify your database credentials
- Check if the database server is running
- Ensure firewall allows connections
- For SQL Server, install ODBC Driver 17

### Performance Issues
- Reduce dataset size by filtering
- Close other browser tabs
- Restart the Streamlit app
- Use simpler visualizations

## Next Steps

- Explore advanced features in the README.md
- Connect to your production databases
- Set up scheduled data refreshes
- Customize the code for your specific needs
- Share insights with your team using reports

## Need Help?

- Check the full README.md for detailed documentation
- Open an issue on GitHub
- Review the source code in the `src/` directory

---

**Happy Analyzing! 📊**
