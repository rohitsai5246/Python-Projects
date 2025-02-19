import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

# Initialize text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    """Function to make the assistant speak"""
    engine.say(text)
    engine.runAndWait()

def listen():
    """Function to listen and recognize voice"""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        try:
            audio = recognizer.listen(source, timeout=5)
            command = recognizer.recognize_google(audio).lower()
            print(f"You said: {command}")
            return command
        except sr.UnknownValueError:
            print("Sorry, I didn't understand that.")
            return None
        except sr.RequestError:
            print("Could not connect to the recognition service.")
            return None
        except Exception as e:
            print(f"Error: {e}")
            return None

def respond(command):
    """Function to handle commands"""
    if command in ["hello", "hi"]:
        speak("Hello! How can I help you?")
    elif "time" in command:
        now = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The current time is {now}")
    elif "date" in command:
        today = datetime.datetime.now().strftime("%B %d, %Y")
        speak(f"Today's date is {today}")
    elif "search" in command:
        query = command.replace("search", "").strip()
        if query:
            speak(f"Searching for {query} on Google")
            webbrowser.open(f"https://www.google.com/search?q={query}")
        else:
            speak("What would you like to search for?")
    else:
        speak("Sorry, I don't understand that command.")

# Main loop
if __name__ == "__main__":
    speak("Hello! I am your voice assistant. How can I assist you?")
    while True:
        command = listen()
        if command:
            if "exit" in command or "stop" in command:
                speak("Goodbye!")
                break
            respond(command)
