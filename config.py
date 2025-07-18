import os
from dotenv import load_dotenv

load_dotenv()

class DefaultConfig:
    """Configuration for the bot."""
    
    PORT = 8000
    APP_ID = os.environ.get("MICROSOFT_APP_ID", "")
    APP_PASSWORD = os.environ.get("MICROSOFT_APP_PASSWORD", "")
    
    # Azure AI Service Configuration
    AI_SERVICE_ENDPOINT = os.environ.get("MICROSOFT_AI_SERVICE_ENDPOINT", "")
    AI_SERVICE_KEY = os.environ.get("MICROSOFT_API_KEY", "")