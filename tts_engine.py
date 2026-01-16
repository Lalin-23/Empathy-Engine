from gtts import gTTS

def synthesize_speech(text, filename="static/output.mp3"):
    tts = gTTS(text=text, lang="en")
    tts.save(filename)


