# To install: pip install SpeechRecognition pyaudio
# Note: pyaudio installation can be tricky on some systems.

import speech_recognition as sr

def speech_to_text():
    """Transcribes spoken audio from the microphone to text."""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Please say something...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        print("You said: " + text)
    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio.")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")

if __name__ == "__main__":
    speech_to_text()