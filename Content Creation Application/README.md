##Content Creation Generator
A Streamlit application that leverages CrewAI and OpenAI's GPT models to automatically generate multi-platform content based on YouTube video analysis.
Features

YouTube channel and topic-based content search
Automated content generation for multiple platforms:

Blog posts
LinkedIn posts
Twitter content


Configurable AI agents and tasks through YAML
Support for multiple OpenAI GPT models
Real-time content generation and display

Prerequisites

Python 3.7+
OpenAI API key
Required Python packages:

streamlit
crewai
crewai_tools
youtube_transcript_api
pyyaml



Installation

Clone the repository:

bashCopygit clone <repository-url>
cd content-generator

Install required packages:

bashCopypip install -r requirements.txt

Create a config.yaml file in the root directory with your agent and task configurations.

Configuration
OpenAI API Setup

Provide your OpenAI API key through the Streamlit interface
Select from available GPT models:

gpt-4-turbo
gpt-3.5-turbo
gpt-4
text-davinci-003



YAML Configuration
The application uses a YAML configuration file to define agents and tasks. Example structure:
yamlCopyagents:
  agent_name:
    role: "Agent Role"
    goal: "Agent Goal"
    verbose: true
    memory: true
    backstory: "Agent Backstory"
    tools: []
    allow_delegation: true

tasks:
  task_name:
    description: "Task Description"
    expected_output: "Expected Output Format"
    agent: "agent_name"
    tools: []
    output_file: "output.txt"
Usage

Start the Streamlit application:

bashCopystreamlit run app.py

In the sidebar:

Enter your OpenAI API key
Select the desired GPT model
Enter a topic of interest
Specify a YouTube channel name


Click "Run Crew Tasks" to generate content
View the generated content in different sections:

Blog Content
LinkedIn Content
Twitter Content
Other generated content



Error Handling
The application includes comprehensive error handling for:

Missing API keys
Configuration file errors
Task execution failures
Invalid inputs

Output
The application displays generated content in markdown format, organized by platform type. Results can be viewed directly in the Streamlit interface.
Limitations

Requires active internet connection
API rate limits apply based on your OpenAI subscription
YouTube content accessibility depends on video availability and permissions

Contributing
Contributions are welcome! Please feel free to submit a Pull Request.
License
[Add your license information here]
