import os
from github import Github
import difflib
from openai import OpenAI, APIError

# Load environment variables
openai_api_key = os.getenv("OPENAI_API_KEY")
github_api_key = os.getenv("GITHUB_API_KEY")

# Check if environment variables are set
if openai_api_key is None or github_api_key is None:
    raise ValueError("Please set the environment variables OPENAI_API_KEY and GITHUB_API_KEY.")

# Initialize OpenAI client with the API key
client = OpenAI(api_key=openai_api_key)

github = Github(github_api_key)

def compare_code(old_code, new_code):
    differ = difflib.Differ()
    diff = differ.compare(old_code.splitlines(), new_code.splitlines())
    return '\n'.join(diff)

def generate_title(code_changes):
    # Use OpenAI API to generate a title
    prompt = f"Code changes:\n{code_changes}\n\nTitle:"
    response = client.completions.create(
        model="text-davinci-002",
        prompt=prompt,
        max_tokens=30
    )
    return response.choices[0].text.strip()


# Example: Fetch a repo, compare code
repo_name = "ammarateya/github_openai"
repo = github.get_repo(repo_name)
old_code = repo.get_contents("hello_world.py").decoded_content.decode("utf-8")
with open('hello_world.py', 'r') as file:
    new_code = file.read()

# Compare code
code_changes = compare_code(old_code, new_code)

# Generate title
title = generate_title(code_changes)

print(f"Code Changes:\n{code_changes}")
print(f"\nGenerated Title: {title}")
