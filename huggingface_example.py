import os
import requests

# Get API key from environment variable
API_TOKEN = os.environ.get("HUGGINGFACE_API_KEY")

API_URL = "https://router.huggingface.co/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {API_TOKEN}",
    "Content-Type": "application/json"
}

def query_api(prompt):
    """Query Hugging Face API with a prompt"""
    try:
        payload = {
            "model": "openai/gpt-oss-20b",
            "messages": [
                {"role": "user", "content": prompt}
            ]
        }

        response = requests.post(API_URL, headers=headers, json=payload)
        data = response.json()

        # FIX: Extract only the AI response text
        if "choices" in data:
            return data["choices"][0]["message"]["content"]
        else:
            return f"Error: {data}"

    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    prompt = input("Enter your prompt: ")
    print("Querying Hugging Face API...")
    print("\nResponse:")
    print(query_api(prompt))