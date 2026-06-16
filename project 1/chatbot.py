# Simple AI hiRule-Based Chatbot

print("Chatbot: Hello! I am a simple rule-based chatbot.")

while True:
    user = input("You: ").lower()

    # Handle greetings
    if user == "hello" or user == "hi":
        print("Chatbot: Hello! How can I help you?")

    elif "how are you" in user:
        print("Chatbot: I am fine. What about you?")

    elif "your name" in user:
        print("Chatbot: I am a simple AI chatbot.")

    # Exit command
    elif user == "bye" or user == "exit":
        print("Chatbot: Goodbye! Have a nice day.")
        break

    # Default response
    else:
        print("Chatbot: Sorry, I don't understand that.")