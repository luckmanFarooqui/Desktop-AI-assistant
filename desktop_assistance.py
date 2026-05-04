import speech_recognition as sr
import pyttsx3
import openai
import os
import requests
import smtplib
import wikipedia
import webbrowser

# Initialize Text-to-Speech
engine = pyttsx3.init()

def speak(text):
    """Convert text to speech"""
    engine.say(text)
    engine.runAndWait()

# Initialize Speech Recognition
recognizer = sr.Recognizer()

def recognize_speech():
    """Listen to user's voice and convert it to text"""
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            print("Sorry, I didn't understand that.")
            return None
        except sr.RequestError:
            print("Could not request results. Check your internet connection.")
            return None

# OpenAI API Setup (Replace with your actual API key)
openai.api_key = "your-openai-api-key"

def chat_with_gpt(prompt):
    """Send prompt to OpenAI and get response"""
    client = openai.OpenAI()
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content


def open_application_website(command):
    """Open common applications based on voice command"""
    if "chrome" in command:
        os.system("start chrome")
        speak("Opening Google Chrome")
    elif "notepad" in command:
        os.system("notepad")
        speak("Opening Notepad")
    elif "calculator" in command:
        os.system("calc")
        speak("Opening Calculator")
    elif "open youtube" in command:
        webbrowser.open("https://www.youtube.com")
        speak("Opening YouTube")    
    elif "open google" in command:
        webbrowser.open("https://www.google.com")
        speak("Opening Google")
    elif "open gmail" in command or "open gmail" in command:
        webbrowser.open("https://www.gmail.com")
        speak("Opening Gmail")
    elif "open facebook" in command:
        webbrowser.open("https://www.facebook.com")
        speak("Opening Facebook")    
    elif "open whatsapp" in command:
        webbrowser.open("https://www.whatsapp.com")
        speak("Opening whatsapp")         
    else:
        speak("Sorry, I don't know how to open that.")

# Main Program Loop
if __name__ == "__main__":
    speak("Hello, I am your AI assistant. How can I help you Atul?")
    
    while True:
        command = recognize_speech()
        
        if command:
            if "exit" in command or "quit" in command:
                speak("Have a good day!")
                break
            elif "open" in command:
                open_application_website(command)
            else:
                response = chat_with_gpt(command)
                print("AI:", response)
                speak(response)
