import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY')


def get_bot_response(message):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=message,
        temperature=0.5,
        max_tokens=60,
        top_p=1.0,
        frequency_penalty=0.5,
        presence_penalty=0.0,
        stop=["You:"]
    )
    # return the text of the completion
    return response.choices[0].text.strip()


def chat_loop():
    print("Hal: Hello! How can I assist you today?")

    while True:
        user_message = input("You: ")
        if user_message.lower() in ["quit", "bye", "goodbye", "see you"]:
            print("Hal: Goodbye!")
            break
        else:
            bot_response = get_bot_response(user_message)
            print(f"Hal: {bot_response}")


if __name__ == "__main__":
    chat_loop()
