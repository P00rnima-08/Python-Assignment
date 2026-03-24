import os
import cohere

api_key = os.environ.get("COHERE_API_KEY")

co = cohere.ClientV2(api_key=api_key)

def query_api(prompt):
    try:
        response = co.chat(
            model="command-a-03-2025",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500,
            temperature=0.7
        )
        return response.message.content[0].text
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    prompt = input("Enter your prompt: ")
    print("Querying Cohere API...")
    print("\nResponse:")
    print(query_api(prompt))