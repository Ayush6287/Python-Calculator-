import pyttsx3

# Initialize the TTS engine
engine = pyttsx3.init()

# Optional: Customize speech properties
engine.setProperty('rate', 150)  # Speed in words per minute
engine.setProperty('volume', 0.9)  # Volume (0.0 to 1.0)

# Text to speak
text = "Hello! This is a text-to-speech example in Python."

# Speak the text
engine.say(text)
engine.runAndWait()  # Wait for speech to complete
