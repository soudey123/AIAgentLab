import os
import yaml
import streamlit as st
from crewai import Agent, Crew, Task, Process
from crewai_tools import YoutubeChannelSearchTool
from youtube_transcript_api import YouTubeTranscriptApi
import traceback

# Load configuration
def load_config(config_path="config.yaml"):
    try:
        with open(config_path, 'r') as file:
            return yaml.safe_load(file)
    except FileNotFoundError:
        st.error(f"Configuration file '{config_path}' not found.")
        return {}
    except yaml.YAMLError as e:
        st.error(f"Error parsing configuration file: {e}")
        return {}

# Initialize agents and tasks from configuration
def initialize_agents_and_tasks(config):
    agents = {}
    tasks = {}

    for agent_name, agent_config in config.get("agents", {}).items():
        agent_tools = [globals()[tool] for tool in agent_config.get("tools", []) if tool in globals()]
        agents[agent_name] = Agent(
            role=agent_config["role"],
            goal=agent_config["goal"],
            verbose=agent_config["verbose"],
            memory=agent_config["memory"],
            backstory=agent_config["backstory"],
            tools=agent_tools,
            allow_delegation=agent_config["allow_delegation"]
        )

    for task_name, task_config in config.get("tasks", {}).items():
        tasks[task_name] = Task(
            description=task_config["description"],
            expected_output=task_config.get("expected_output", ""),
            agent=agents.get(task_config["agent"]),
            tools=[globals()[tool] for tool in task_config.get("tools", []) if tool in globals()],
            output_file=task_config.get("output_file", "")
        )

    return agents, tasks

# Streamlit app
st.title("Content Creation Generator")

# Sidebar for OpenAI API Key and Model Selection
st.sidebar.header("OpenAI API Configuration")
api_key = st.sidebar.text_input("Enter OpenAI API Key", type="password", help="Your OpenAI API key for authentication.", key="api_key")
model = st.sidebar.selectbox(
    "Select GPT Model",
    ["gpt-4-turbo", "gpt-3.5-turbo", "gpt-4", "text-davinci-003"],
    help="Choose the model to use for content generation.",
    key="model"
)

if api_key:
    os.environ["OPENAI_API_KEY"] = api_key
else:
    st.sidebar.warning("Please enter your OpenAI API key to proceed.")

os.environ["GPT_MODEL"] = model

# Sidebar for topic and channel input
st.sidebar.header("YouTube Video Search")
topic = st.sidebar.text_input("Enter Topic of Interest", help="Provide a topic to search for relevant YouTube videos.", key="topic")
channel_name = st.sidebar.text_input("Enter YouTube Channel Name", help="Provide the name of the YouTube channel to narrow the search.", key="channel_name")

# Load configuration
config = load_config()

# Initialize agents and tasks
agents, tasks = {}, {}
try:
    if api_key:
        youtube_tool = YoutubeChannelSearchTool()
        agents, tasks = initialize_agents_and_tasks(config)
except Exception as e:
    st.error(f"Failed to initialize agents or tasks: {traceback.format_exc()}")

# Crew setup
if api_key and agents and tasks:
    my_crew = Crew(
        agents=list(agents.values()),
        tasks=list(tasks.values()),
        verbose=True,
        process=Process.sequential,
        memory=True,
        cache=True,
        max_rpm=100,
        share_crew=True
    )
else:
    my_crew = None

# Execute crew tasks
if st.sidebar.button("Run Crew Tasks", key="run_crew_tasks"):
    if not api_key:
        st.error("Please provide your OpenAI API key to run tasks.")
    elif not (topic and channel_name):
        st.error("Please provide both a topic and a channel name to execute the crew's tasks.")
    elif my_crew:
        with st.spinner("Executing tasks..."):
            try:
                inputs = {'topic': topic}
                result = my_crew.kickoff(inputs=inputs)
                if result:
                    st.success("Crew tasks completed successfully!")

                    # Inspect and render the result content dynamically
                    st.subheader("Raw Result")
                    st.json(result.dict())

                    # Extract and display outputs for specific agents
                    task_outputs = result.dict().get("tasks_output", [])
                    for task_output in task_outputs:
                        agent_role = task_output.get("agent", "")
                        raw_data = task_output.get("raw", "")

                        if agent_role == "Blog Writer":
                            st.subheader("Blog Content")
                            st.markdown(f"```markdown\n{raw_data}\n```")
                        elif agent_role == "LinkedIn Post Creator":
                            st.subheader("LinkedIn Content")
                            st.markdown(f"```markdown\n{raw_data}\n```")
                        elif agent_role == "Twitter Content Creator":
                            st.subheader("Twitter Content")
                            st.markdown(f"```markdown\n{raw_data}\n```")
                        else:
                            st.subheader(f"Other Content ({agent_role})")
                            st.markdown(f"```markdown\n{raw_data}\n```")
                else:
                    st.error("No results were returned from the tasks.")
            except Exception as e:
                st.error(f"Unexpected error: {traceback.format_exc()}")
    else:
        st.error("Agents and tasks are not properly initialized. Please check your configuration and API key.")
