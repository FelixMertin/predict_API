import os
from dotenv import load_dotenv

load_dotenv()
class Config(object):
    API_KEY = os.getenv('API_KEY')
    print(f"This is the API Key {API_KEY}")
