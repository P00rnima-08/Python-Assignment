#Importing libraries
import google.generativeai as genai
import os

#Getting API key from environment variable  
api_key = os.getenv("GOOGLE_API_KEY")
#Configuring Gemini API
genai.configure(api_key=api_key)
#Initializing the model
model = genai.GenerativeModel("models/gemini-3-flash-preview")

#Function to query Gemini API
def query_api(prompt):
    try:
        response = model.generate_content(prompt)            #Generating response from Gemini model
        return response.text                                 #Returning the response
    except Exception as e:                                   #Error Handling
        return f"Error: {str(e)}"

#Main function 
if __name__ == "__main__":
    user_prompt = input("Enter your prompt: ")               #Taking the prompt as input from the user
    print("Querying Gemini API...")
    result = query_api(user_prompt)                          #Calling the function 
    print("\nResponse:")
    print(result)                                            #Printing the resut