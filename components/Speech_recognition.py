import speech_recognition as sr
import streamlit as st

def transcribe_from_mic(device_index=1, phrase_time_limit=15, pause_threshold=1.5, language="en-US"):
    r = sr.Recognizer()
    r.pause_threshold = pause_threshold
    mic = sr.Microphone(device_index=device_index)
    
    with mic as source:
        r.adjust_for_ambient_noise(source)
        # Show "Listening..." message
        listening_placeholder = st.empty()
        listening_placeholder.info("🎙️ Listening... Please speak now.")
        
        audio = r.listen(source, phrase_time_limit=phrase_time_limit)
        listening_placeholder.empty()  # Clear message after recording
    
    try:
        text = r.recognize_google(audio, language=language)
        return text
    except sr.UnknownValueError:
        return "Sorry, I could not understand the audio."
    except sr.RequestError as e:
        return f"Could not request results; {e}"



#transcription = transcribe_from_mic()
#print(transcription)