# src/data_models.py

from dataclasses import dataclass
from typing import List, Optional
from datetime import datetime
import pickle
import yaml
import os

def load_data_models_config():
    with open('config/data_models.yaml', 'r') as f:
        return yaml.safe_load(f)

@dataclass
class Article:
    title: str
    authors: List[str]
    journal: str
    abstract: str
    publication_date: datetime
    keywords: List[str]
    url: str
    discipline: str
    citation_count: Optional[int] = None

class UserProfile:
    def __init__(self, discipline: str, interests: List[str], 
                 preferred_journals: List[str] = None,
                 reading_history: List[str] = None):
        self.discipline = discipline
        self.interests = interests
        self.preferred_journals = preferred_journals or []
        self.reading_history = reading_history or []
        
        config = load_data_models_config()
        self.storage_config = config['user_profile']['storage']
    
    def save_profile(self):
        filename = self.storage_config['filename']
        with open(filename, 'wb') as f:
            pickle.dump(self, f)
    
    @classmethod
    def load_profile(cls):
        config = load_data_models_config()
        filename = config['user_profile']['storage']['filename']
        if os.path.exists(filename):
            with open(filename, 'rb') as f:
                return pickle.load(f)
        return None