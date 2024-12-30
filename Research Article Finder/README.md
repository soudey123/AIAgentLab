# AI Research Article Finder

This project is a Streamlit-based application that helps users find research articles based on topics of interest, date range, and other criteria. It uses SERPAPI to fetch articles from Google Scholar and optionally processes the results using GPT models.

---

## Project Structure

.
├── config/                    # Configuration files
│   ├── data_models.yaml       # Data models for articles and user profiles
│   ├── tools.yaml             # Tool definitions and configurations
│   ├── agents.yaml            # Agent definitions and configurations
│   └── tasks.yaml             # Task definitions for agents
├── src/                       # Source code for core components
│   ├── data_models.py         # Data models for the application
│   ├── tools.py               # Tools for interacting with APIs (e.g., SERPAPI, GPT)
│   ├── agents.py              # Agents for handling tasks and logic
│   └── tasks.py               # Task execution and management logic
├── app.py                     # Main Streamlit app
├── requirements.txt           # Python dependencies


## Features
Search Research Articles: Fetch articles from Google Scholar based on a topic, start date, and end date.
Customizable Topics: Select predefined topics or input your custom topic.
Date Range Search: Filter articles based on a specified date range.
Optional GPT Integration: Use GPT models to rank or process articles.
Streamlit Interface: User-friendly web app built with Streamlit.
Dynamic Table: Display search results in a sortable, tabular format with clickable links.
Requirements

### To run this application, ensure you have the following installed:

Python 3.7 or higher
Required Python packages (specified in requirements.txt)
Install dependencies using:

bash
Copy code
pip install -r requirements.txt
Running the Application
Clone this repository:

bash
Copy code
git clone <repository-url>
cd <repository-folder>
Install the dependencies:

bash
Copy code
pip install -r requirements.txt
Set up your API keys:

SERPAPI: Add your SERPAPI API key in tools.py.
OpenAI (optional): Add your OpenAI API key in tools.py for GPT processing.
Run the Streamlit app:

bash
Copy code
streamlit run app.py
Open your browser and navigate to the local URL provided (e.g., http://localhost:8501).

Configuration Files
data_models.yaml: Defines the data structure for articles and user profiles.
tools.yaml: Configures tools such as SERPAPI and GPT.
agents.yaml: Specifies the roles and tasks for AI agents.
tasks.yaml: Details the tasks and their relationships with agents.
Future Improvements
Preferred Journal Selection: Add an option to filter articles by preferred journals.
Author Information: Include author details in search results.
Advanced GPT Processing: Enhance article ranking and relevance scoring using GPT.
Export Feature: Allow users to download the article table as a CSV.
License
This project is licensed under the MIT License.

Contributing
Contributions are welcome! Please fork the repository and submit a pull request.

Contact
For questions or support, feel free to open an issue or reach out via GitHub.