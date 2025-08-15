print("Hello! Welcome to Chatbot!!")

while True:
    user_input = input("You: ").lower()  # Convert to lowercase for easy matching

    if user_input in ["exit", "quit"]:
        print("ChatBot: Have a great day!")
        break

    elif "hello" in user_input or "hi" in user_input:
        print("ChatBot: Hello there! How can I help you?")

    elif "how are you" in user_input:
        print("ChatBot: I’m doing great, thanks for asking! What about you?")

    elif "your name" in user_input:
        print("ChatBot: I am a simple rule-based chatbot created in Python.")

    elif "time" in user_input:
        from datetime import datetime

        now = datetime.now().strftime("%H:%M:%S")
        print(f"ChatBot: The current time is {now}")

    elif "date" in user_input:
        from datetime import datetime

        today = datetime.now().strftime("%Y-%m-%d")
        print(f"ChatBot: Today's date is {today}")

    else:
        print("ChatBot: Sorry, I didn't understand that. Can you rephrase?")
