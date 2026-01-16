from flask import Flask, render_template, request
from emotion_detector import detect_emotion
from voice_mapper import map_voice_params
from tts_engine import synthesize_speech

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    emotion = None
    params = None

    if request.method == "POST":
        text = request.form["text"]
        emotion, intensity = detect_emotion(text)
        params = map_voice_params(emotion, intensity)

        synthesize_speech(text)

    return render_template("index.html", emotion=emotion, params=params)

if __name__ == "__main__":
    app.run(debug=True)

