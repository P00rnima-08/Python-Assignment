#Importing libraries
from groq import Groq
import os

#Initializing Groq client with API key
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

#Function to query Groq API
def query_api(prompt):
    try:
        chat_completion = client.chat.completions.create(          #Creating chat response 
            messages=[{"role": "user", "content": prompt}],        #Sending the user prompt
            model="llama-3.1-8b-instant",                          #Specifying the model
            max_tokens=500,                                        #Limiting the response length
        )
        return chat_completion.choices[0].message.content          #Extracting the actual AI response text
    except Exception as e:                                         #Error Handling
        return f"Error: {str(e)}"

#Main function 
if __name__ == "__main__":
    prompt = input("Enter your prompt: ")                          #Taking prompt as input from the user
    print("Querying Groq API...")
    print("\nResponse:")
    print(query_api(prompt))                                       #Calling the function 