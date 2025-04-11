import os
from dotenv import load_dotenv

load_dotenv()

# API Keys - Using environment variables
HUGGINGFACE_API_KEY = os.getenv('HUGGINGFACE_API_KEY')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY') 
