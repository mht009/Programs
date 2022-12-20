import pyttsx3

engine = pyttsx3.init()
# engine.say("Hello, World")
# engine.runAndWait()

engine.setProperty("rate", 150)

name = input("Enter your name: ")
engine.say(f"Namaste {name}, How are you?")
engine.runAndWait()