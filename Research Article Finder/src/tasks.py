# src/tasks.py

from crewai import Task
import yaml
from .data_models import UserProfile

def load_tasks_config():
    with open('config/tasks.yaml', 'r') as f:
        return yaml.safe_load(f)

def create_tasks(agents: dict, user_profile: UserProfile):
    config = load_tasks_config()
    tasks = []
    
    for task_id, task_config in config['tasks'].items():
        description = task_config['description_template'].format(
            discipline=user_profile.discipline,
            interests=user_profile.interests
        )
        
        # Provide a valid string for expected_output
        expected_output = "A list of relevant articles or recommendations based on the user's profile."

        tasks.append(Task(
            description=description,
            agent=agents[task_config['agent']],
            expected_output=expected_output  # Pass a valid string
        ))
    
    return tasks