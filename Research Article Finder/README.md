# AI Research Article Finder

This project is a Streamlit-based application that helps users find research articles based on topics of interest, date range, and other criteria. It uses SERPAPI to fetch articles from Google Scholar and optionally processes the results using GPT models.

---

## 1. Project Structure

```plaintext
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

```

## 2. Features

- **Search Research Articles**: Fetch articles from Google Scholar based on a topic, start date, and end date.

- **Customizable Topics**: Select predefined topics or input your custom topic.

- **Date Range Search**: Filter articles based on a specified date range.

- **Optional GPT Integration**: Use GPT models to rank or process articles.

- **Streamlit Interface**: User-friendly web app built with Streamlit.

- **Dynamic Table**: Display search results in a sortable, tabular format with clickable links.


### 3. Requirements

To run this application, ensure you have the following installed:

1. Python 3.7 or higher
2. Required Python packages (specified in requirements.txt)

Install dependencies using:

```pip install -r requirements.txt```


### 4. Running the Application

1. Clone this repository:

```
git clone <repository-url>
cd <repository-folder>
```

2. Install the dependencies:

```pip install -r requirements.txt```

3. Set up your API keys:

- SERPAPI: Add your SERPAPI API key in tools.py.

- OpenAI (optional): Add your OpenAI API key in tools.py for GPT processing.

**Note: Create .env file to store API keys in accordance with better coding practice.**

4. Run the Streamlit app:
```streamlit run app.py```

5. Open your browser and navigate to the local URL provided (e.g., http://localhost:8501).


### 5. Configuration Files

- **data_models.yaml:** Defines the data structure for articles and user profiles.

- **tools.yaml:** Configures tools such as SERPAPI and GPT.

- **agents.yaml:** Specifies the roles and tasks for AI agents.

- **tasks.yaml:** Details the tasks and their relationships with agents.


### 6. Future Improvements

* **Preferred Journal Selection:** Add an option to filter articles by preferred journals.

* **Author Information:** Include author details in search results.

* **Advanced GPT and LLMs Processing:** Enhance article ranking and relevance scoring using GPT or other LLMs.

* **Export Feature:** Allow users to download the article table as a CSV.


### 7. License

This project is licensed under the MIT License.


### 8. Contributing

Contributions are welcome! Please fork the repository and submit a pull request.


### 9. Contact

For questions or support, feel free to open an issue or reach out via GitHub.
