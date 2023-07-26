import speech_recognition as sr
import pyttsx3
import datetime
import random
import os
import pywhatkit

def speak(text):
    # Function to speak the response using text-to-speech
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    # Set female voice (you can try different indices for different voices)
    engine.setProperty('voice', voices[1].id)
    engine.say(text)
    engine.runAndWait()

def listen():
    # Function to listen to the user's voice command and return the text
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        user_input = recognizer.recognize_google(audio)
        print("You:", user_input)
        return user_input.lower()
    except sr.UnknownValueError:
        print("Sorry, I didn't get that.")
        return ""
    except sr.RequestError:
        print("Could not connect to the service. Please try again later.")
        return ""

def get_time():
    # Function to get the current time and return a response
    now = datetime.datetime.now()
    time_str = now.strftime("%I:%M %p")
    response = f"The current time is {time_str}."
    return response

def get_greeting():
    # Function to get a random greeting and return a response
    greetings = ["Hello!", "Hi there!", "Hey!", "Greetings!"]
    response = random.choice(greetings)
    return response

def search_web(query):
    # Function to perform a web search using pywhatkit
    pywhatkit.search(query)
    response = "Sure, let me look that up for you."
    return response

def main():
    # Main function for the Alexa chatbot
    print("Alexa: Hello! I'm your Python-based Alexa. You can start chatting with me now!")
    while True:
        user_input = listen()
        if "alexa" in user_input:
            user_input = user_input.replace("alexa", "")
            if "time" in user_input:
                response = get_time()
            elif "hello" in user_input or "hi" in user_input:
                response = get_greeting()
            elif "search" in user_input:
                query = user_input.replace("search", "")
                response = search_web(query)
            else:
                response = "Sorry, I'm still learning and I don't know how to respond to that."
        else:
            response = "You can start your command by saying 'Alexa'."

        if user_input.lower() in ["exit", "quit", "bye"]:
            print("Alexa: Goodbye!")
            break

        speak("Alexa: " + response)


if __name__ == "__main__":
    main()
