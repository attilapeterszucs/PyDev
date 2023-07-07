import speech_recognition as sr
import webbrowser
import subprocess


def open_program(program_name):
    subprocess.run(['open', '-a', program_name])


def open_website(website_name):
    webbrowser.open(website_name)


def listen_and_execute():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        print(f"You said: {text}")

        if "open" in text and "browser" in text:
            open_website("https://www.google.com")
        elif "open" in text and "text editor" in text:
            open_program("TextEdit")
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand what you said.")
    except sr.RequestError as e:
        print(f"Error connecting to the API: {e}")


if __name__ == "__main__":
    listen_and_execute()

