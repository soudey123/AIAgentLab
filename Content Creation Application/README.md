# Content Creation Generator 📄✨

A Streamlit application that leverages CrewAI and OpenAI's GPT models to automatically generate multi-platform content based on YouTube video analysis.

## Features
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
