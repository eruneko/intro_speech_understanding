import speech_recognition

def transcribe_wavefile(filename, language='en'):
    '''
    Use sr.Recognizer.AudioFile(filename) as the source,
    recognize from that source,
    and return the recognized text.
    
    @params:
    filename (str) - the filename from which to read the audio
    language (str) - the language of the audio (optional; default is English)
    
    @returns:
    text (str) - the recognized speech
    '''
       r = speech_recognition.Recognizer()
       
       with speech_recognition.AudioFile(filename) as source:
            audio = r.record(sorce)
            text = r.recogniza_google(audio,language=language)
            
       return text