from string import Template
import pyttsx3
# from gtts import gTTS
import os
def text_to_speech(text):
    # Initialize the text-to-speech engine
    engine = pyttsx3.init()

    # Set properties (optional)
    engine.setProperty('rate', 150)  # Speed of speech
    engine.setProperty('volume', 0.9)  # Volume level (0.0 to 1.0)

    # Speak the given text
    engine.say(text)

    # Wait for the speech to finish
    engine.runAndWait()

if __name__ == "__main__":
    # Get input from the user
    user_input = input("Enter the text you want to convert to speech: ")

    # Call the text_to_speech function with the user's input
    text_to_speech(user_input)
