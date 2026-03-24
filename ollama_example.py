#Importing libraries
import subprocess
import os
#Model name
MODEL_NAME = "phi" 

#Function to run Ollama locally
def query_api(prompt):
    try:
        result = subprocess.run(
            ["ollama", "run", MODEL_NAME, prompt],
            capture_output=True,                     #Capturing the output
            text=True,                               #Ensuring the response is in text format
            encoding="utf-8",
            check=True                               #Raise error is command fails
        )
        return result.stdout.strip()                 #Returning the output
    except subprocess.CalledProcessError as e:       #Error Handling
        return f"Error: {e.stderr}"

#Main function
if __name__ == "__main__":
    user_prompt = input("Enter your prompt: ")       #Taking prompt as imput from the user
    print("Querying Ollama...")
    result = query_api(user_prompt)                  #Calling the function 
    print("\nResponse:")
    print(result)