import os
import time

# --- CONFIGURATION ---
# Set to True to test without paying for OpenAI
MOCK_MODE = True 

# Your Real Azure API (From your deployment)
AZURE_API_URL = "http://industrial-defect-api.eastus.azurecontainer.io/predict"

def inspect_component_tool(image_path):
    """
    The 'Tool' that the Agent uses to see the world.
    """
    print(f"\n[TOOL] 📸 Agent is activating Azure Computer Vision API...")
    print(f"[TOOL] 📡 Sending image: {image_path} to Cloud Endpoint...")
    
    # Simulate API Latency
    time.sleep(1.5)
    
    # In a real scenario, we would do: requests.post(AZURE_API_URL, ...)
    # For this demo, we return a simulated Azure response
    return {
        "prediction": "dent",
        "confidence": 0.94,
        "location": "upper_right_quadrant",
        "action_required": "FAIL_QC"
    }

def run_agent_workflow(user_command):
    print(f"------------------------------------------------")
    print(f"👤 USER: \"{user_command}\"")
    print(f"------------------------------------------------")
    
    # 1. The 'Brain' (LLM) interprets the command
    print(f"🤖 AGENT: Thinking... (Analyzing intent)")
    time.sleep(1)
    
    if "check" in user_command.lower() or "scan" in user_command.lower():
        print(f"🤖 AGENT: Decided to use tool -> [inspect_component]")
        
        # 2. Agent calls the tool
        result = inspect_component_tool("/images/batch_404.jpg")
        
        # 3. Agent interprets result
        print(f"🤖 AGENT: Received Data -> {result}")
        print(f"🤖 AGENT: Final Verdict -> The component failed QC due to a {result['prediction']} with {result['confidence']*100}% confidence.")
    else:
        print("🤖 AGENT: I am not sure what to do. I can only inspect components.")

if __name__ == "__main__":
    # Test the Agent
    run_agent_workflow("Please check this component for any defects.")