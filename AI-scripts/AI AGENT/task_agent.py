import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Configure Gemini API with your key
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Instantiate Gemini model
model = genai.GenerativeModel("gemini-1.5-flash")

# Read task from file
def read_task(filepath):
    with open(filepath, 'r') as f:
        return f.read()

# Make a call to Gemini AI with a prompt to categorize our task
def summarize_task(tasks):
    prompt = f"""
    You are an expert task planning agent.
    Given a list of tasks, categorize them into 3 priority buckets:
      - High Priority
      - Medium Priority
      - Low Priority

    Here is the list of tasks:
    {tasks}

    Return the responses in this format:
    High Priority:
    - Task 1
    - Task 2

    Medium Priority:
    - Task 1
    - Task 2

    Low Priority:
    ....
    """
    response = model.generate_content(prompt)
    return response.text

if __name__ == "__main__":
    task_text = read_task("tasks.txt")
    summary = summarize_task(task_text)
    print("\nTask Summary:\n", summary)
    print("-" * 30) 