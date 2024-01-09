import speech_recognition as sr
from gtts import gTTS
import os
import pyaudio

# Function to capture speech and convert to text
def speech_to_text():
    """
    Captures speech from the microphone and converts it to text.
    
    Returns:
        str: The recognized text from speech.
    """
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening... Please speak.")
        try:
            audio = recognizer.listen(source, timeout=5)
            print("Processing...")
            text = recognizer.recognize_google(audio)
            print(f"Recognized Text: {text}")
            return text
        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")
            return None
        except sr.RequestError as e:
            print(f"Request Error: {e}")
            return None

# Function to convert text to female voice and play it
def text_to_female_voice(text, output_audio_path="female_voice.mp3"):
    """
    Converts text to a female voice and plays the audio.
    
    Parameters:
        text (str): The input text to convert to speech.
        output_audio_path (str): Path to save the generated speech audio file.
    """
    if not text:
        print("No text provided for speech synthesis.")
        return
    
    print("Generating female voice...")
    tts = gTTS(text=text, lang='en', tld='com.au')  # Use Australian English for a distinct female voice
    tts.save(output_audio_path)
    print(f"Audio saved as {output_audio_path}. Playing the audio...")
    os.system(f"start {output_audio_path}")  # For Windows users. Use 'afplay' for Mac or 'xdg-open' for Linux.

# Main process
def main():
    # Step 1: Convert speech to text
    recognized_text = speech_to_text()
    
    # Step 2: Convert text to a female voice and play it
    if recognized_text:
        text_to_female_voice(recognized_text)

if __name__ == "__main__":
    main()
