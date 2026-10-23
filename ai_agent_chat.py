"""
AI anime waifu agent chat
"""

import 
import json, os, datetime
from pathlib import Path
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
gemini_api_key = os.environ["GEMINI_API_KEY"]
discord_token = os.environ["DISCORD_TOKEN"]
owner_id = os.environ["OWNER_ID"]

# Set up Gemini API key
gemini.api_key = gemini_api_key