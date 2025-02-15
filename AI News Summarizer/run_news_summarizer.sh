#!/bin/bash

# Set path to your project directory
cd /Users/samdey87/Documents/GitHub/AIAgentLab/AI\ News\ Summarizer

# Activate your Python environment if you're using one
# source /path/to/your/venv/bin/activate

# Set Python path
export PYTHONPATH="${PYTHONPATH}:/Users/samdey87/Documents/GitHub/AIAgentLab/AI\ News\ Summarizer"

# Run the script
python3 src/news_summarizer.py

# Log the execution (optional)
echo "News summarizer ran at $(date)" >> /Users/samdey87/Documents/GitHub/AIAgentLab/AI\ News\ Summarizer/logs/cron.log