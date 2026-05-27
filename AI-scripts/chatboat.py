# Simple Rule-Based Chatbot

print("Chatbot: Hello! I am your chatbot. Type 'bye' to exit.")

while True:
    user_input = input("You: ").lower()   # Get user input

    if user_input == "bye":
        print("Chatbot: Goodbye! Have a great day!")
        break

    elif "hello" in user_input or "hi" in user_input:
        print("Chatbot: Hello! How can I help you?")

    elif "how are you" in user_input:
        print("Chatbot: I'm doing well, thanks for asking!")

    elif "name" in user_input:
        print("Chatbot: My name is PyBot.")

    elif "age" in user_input:
        print("Chatbot: I don't have an age. I'm just code!")

    elif "who made you" in user_input:
        print("Chatbot: I was created by Archana.")

    else:
        print("Chatbot: Sorry, I didn't understand that.")
