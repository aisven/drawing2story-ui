import speech_recognition as sr
#import pyaudio


def speech_to_text(duration=5, lang="de-DE"):
	init_rec = sr.Recognizer()
	with sr.Microphone() as source:
		print("Let's speak!")
		audio_data = init_rec.record(source, duration=5)
		print("Recognizing your text.............")
		text = init_rec.recognize_google(audio_data, language=lang)
	return text
    
    
if __name__ == "__main__":
	transcript = speech_to_text()
	print(transcript)
	
