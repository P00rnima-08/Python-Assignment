#Importing libraries
import os
import requests

#Getting API key from environment variable
API_TOKEN = os.environ.get("HUGGINGFACE_API_KEY")
#API endpoint
API_URL = "https://router.huggingface.co/v1/chat/completions"
#Requesting headers
headers = {
    "Authorization": f"Bearer {API_TOKEN}",
    "Content-Type": "application/json"                 #Specifying JSON format
}

#Function to query HuggingFace API
def query_api(prompt):
    try:
        payload = {
            "model": "openai/gpt-oss-20b",                       #Specifying the model
            "messages": [
                {"role": "user", "content": prompt}              #Sending user input
            ]
        }
        response = requests.post(API_URL, headers=headers, json=payload)       #Sending POST request
        data = response.json()                                                 #Converting response into JSON format 

        #Checking if the response is valid or not
        if "choices" in data:
            return data["choices"][0]["message"]["content"]       #Extracting text 
        else:
            return f"Error: {data}"                               #Returing error 

    except Exception as e:                                        #Error Handling
        return f"Error: {str(e)}"

#Main function 
if __name__ == "__main__":
    prompt = input("Enter your prompt: ")               #Taking prompt as input from the user 
    print("Querying Hugging Face API...")
    print("\nResponse:")
    print(query_api(prompt))                            #Calling the function