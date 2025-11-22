# main.py
from agents import researcher_model, concierge_model
# REMOVED: from google.generativeai.types import Content, Part (Not needed for text-only)

# --- SIMULATED MEMORY (Concept: Sessions) ---
user_profile = {
    "name": "Alex",
    "location": "San Francisco",
    "likes": ["Jazz music", "Spicy food", "History museums"],
    "dislikes": ["Loud clubs", "Hiking"]
}

def run_weekender_agent():
    print(f"--- Starting Weekender Agent for {user_profile['name']} ---")
    
    # Step 1: Define the Goal
    user_request = "I want to go out this Saturday afternoon/evening."
    print(f"User Request: {user_request}")

    # Step 2: Researcher Agent (Finds facts)
    print("\n--- Phase 1: Researching ---")
    # We enable automatic function calling so the agent uses the tools itself
    chat = researcher_model.start_chat(enable_automatic_function_calling=True)
    
    research_prompt = f"""
    Find out the weather for this Saturday in {user_profile['location']}.
    Also find 3 events happening this Saturday in {user_profile['location']} that might match: {user_profile['likes']}.
    """
    
    # Send message and wait for it to loop through tools
    research_response = chat.send_message(research_prompt)
    raw_data = research_response.text
    
    # A quick check to see if it actually found anything
    print(f"Research Found: {raw_data[:200]}...") 

    # Step 3: Concierge Agent (Synthesizes)
    print("\n--- Phase 2: Planning Itinerary ---")
    
    final_prompt = f"""
    Here is the Research Data:
    {raw_data}

    Here is the User Profile:
    {user_profile}

    Create a final itinerary for {user_profile['name']}.
    """
    
    final_response = concierge_model.generate_content(final_prompt)
    
    print("\n" + "="*30)
    print("FINAL ITINERARY")
    print("="*30)
    print(final_response.text)

if __name__ == "__main__":
    run_weekender_agent()