#Importing libraries
import os
import cohere

#Getting API key from environment variable
api_key = os.environ.get("COHERE_API_KEY")
#Initializing Cohere client with API key
co = cohere.ClientV2(api_key=api_key)

#Function to query Cohere API 
def query_api(prompt):
    try:
        response = co.chat(                                    #Sending chat request
            model="command-a-03-2025",                         #Specifying the model name
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500                                     #Limiting the reponse 
        )
        return response.message.content[0].text                #Extracting the actual AI response text
    except Exception as e:                                     #Error Handling 
        return f"Error: {str(e)}"

#Main function 
if __name__ == "__main__":
    prompt = input("Enter your prompt: ")                      #Taking the prompt as input from the user
    print("Querying Cohere API...")
    print("\nResponse:")
    print(query_api(prompt))                                   #Calling the function 