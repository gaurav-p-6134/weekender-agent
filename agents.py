import os
import google.generativeai as genai
from dotenv import load_dotenv
from tools import tools_list

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# --- AGENT 1: THE RESEARCHER (Fast & Efficient) ---
researcher_model = genai.GenerativeModel(
    # UPDATED: Using the 2.0 Flash model available in your list
    model_name='models/gemini-2.0-flash', 
    tools=tools_list,
    system_instruction="""
    You are a Research Agent. Your job is to find specific information about events and weather.
    You DO NOT make recommendations. You only gather facts using your tools.
    """
)

# --- AGENT 2: THE CONCIERGE (High Quality Reasoning) ---
concierge_model = genai.GenerativeModel(
    # UPDATED: Using the powerful 2.5 Pro model for better writing
    model_name='models/gemini-2.5-pro',
    system_instruction="""
    You are 'Weekender', a top-tier travel concierge.
    You will receive raw research data and User Preferences.
    Your goal: Create a polite, enthusiastic weekend itinerary.
    If the weather is bad, suggest indoor alternatives.
    Always explain WHY you picked an event based on their preferences.
    """
)