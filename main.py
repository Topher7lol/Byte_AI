import requests
from bs4 import BeautifulSoup
import random

def search_google(query):
    url = f"https://www.google.com/search?q={query}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        search_results = soup.find_all("div", class_="BNeawe vvjwJb AP7Wnd")
        results = [result.get_text() for result in search_results]
        return results
    else:
        return None

def respond_to_greeting(greeting):
    greetings = ["Hi!", "Hello!", "Hey there!", "Hi, how can I help you?", "Hello! What can I do for you today?"]
    return random.choice(greetings)

def respond_to_inquiry():
    inquiries = ["I'm doing well, thank you!", "Feeling good, thanks for asking!", "I'm here and ready to assist!", "All systems are functioning smoothly, thanks!"]
    return random.choice(inquiries)

def main():
    print("Welcome to Byte AI!")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["hi", "hello", "hey", "howdy"]:
            print("Byte AI:", respond_to_greeting(user_input))
        elif user_input.lower() in ["how are you?", "how are you doing?", "what's up?", "how's it going?"]:
            print("Byte AI:", respond_to_inquiry())
        elif user_input.lower() == 'exit':
            print("Goodbye!")
            break
        else:
            results = search_google(user_input)
            if results:
                for i, result in enumerate(results, 1):
                    print(f"Byte AI - Result {i}: {result}")
            else:
                print("Byte AI: Error - Unable to retrieve search results.")

if __name__ == "__main__":
    main()
