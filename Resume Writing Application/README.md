# Resume Tailoring AI Assistant 📄✨

## Overview
This Jupyter notebook implements an AI-powered resume tailoring tool using CrewAI, Streamlit, and OpenAI's language models. The application helps job seekers create personalized resumes and interview preparation materials.

## Key Features
- Generates tailored resumes based on job postings
- Creates custom interview preparation materials
- Utilizes multiple AI agents for comprehensive analysis
- Supports different GPT models
- Allows downloading of generated materials

## Prerequisites
Before running the notebook, ensure you have the following:
- Python 3.8+
- Streamlit
- CrewAI
- OpenAI API Key
- Serper API Key

## Required Libraries
- `streamlit`
- `crewai`
- `crewai_tools`
- `python-docx`
- `reportlab`
- `io`
- `tempfile`

## API Keys Needed
1. **OpenAI API Key**: For language model processing
   - Obtain from [OpenAI Platform](https://platform.openai.com/)
2. **Serper API Key**: For web searching capabilities
   - Obtain from [Serper.dev](https://serper.dev/)

## Workflow
1. Configure API keys
2. Input job posting URL
3. Provide GitHub profile URL
4. Upload your current resume
5. Generate tailored materials

## Recommended Model Selection
- `gpt-3.5-turbo`: Fast and cost-effective
- `gpt-4`: More advanced reasoning
- `gpt-4o`: Latest and most capable model

## Ethical Use Statement
This tool is designed to assist job seekers in presenting their best professional selves. Always ensure the generated content accurately represents your skills and experiences.

## Troubleshooting
- Verify API keys are correct
- Check internet connectivity
- Ensure all required libraries are installed

## Limitations
- Requires active internet connection
- Quality of output depends on input quality
- AI-generated content should be reviewed and personalized

---

**Note**: This is an experimental tool. Always review and customize the generated
