# Imports


# Read API keys


# Initialize Groq client


# Select model


# Chat function
def chat():

    # Welcome message

    
    # Conversation history (list)


    # Inifinite loop
    while True:
    
        # User input


        # Check for the exit condition (exit, quit, end)


        # Add user input to conversation history


        # Build a prompt using conversation history
        try:

            # Get the Groq response


            # extract the output text



            # print the output text


            # add the ai message into the conversation history as an object with a role


        except Exception as e:

            # Add an exception message
            print(f"AI: Sorry, I encountered an error: {str(e)}")

# run the chatbot
if __name__ == "__main__":
    chat()