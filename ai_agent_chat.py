"""
AI anime waifu agent chat
"""

import 
import json, os, datetime
from pathlib import Path
import discord
from anthropic import AsyncAnthropic

# Set up Anthropic API key
anthropic.api_key = os.getenv("ANTHROPIC_API_KEY")

# Define the model and system prompt
model = "claude-3-5-sonnet-20260319"
