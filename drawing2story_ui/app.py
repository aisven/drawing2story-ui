from flask import Flask, render_template, request, flash
from voice_interface.speech_to_text import speech_to_text
import base64
import utils

app = Flask(__name__)
app.secret_key = "SECRET_KEY_3643"


@app.route("/")
def start():
    return render_template("start.html")


@app.route("/welcome", methods=["POST", "GET"])
def welcome():
    return render_template("welcome.html")


@app.route("/leave", methods=["POST", "GET"])
def leave():
    return render_template("leave.html")


@app.route("/upload", methods=["POST", "GET"])
def upload():
    if request.method == "POST":
        # Get the uploaded file
        drawing_image = request.files["drawingImage"]
        # Load to the variable to show on the page
        drawing_image_data = base64.b64encode(drawing_image.read()).decode("utf-8")
        # process the file here
        numbers_of_animals, animal_class = utils.animal_detection(drawing_image_data)
        return render_template(
            "confirmation.html",
            drawing_image=drawing_image_data,
            animal_class=animal_class,
            n_animals=numbers_of_animals,
        )
    elif request.method == "GET":
        return render_template("upload.html")
    return render_template("upload.html")


@app.route("/confirmation", methods=["POST", "GET"])
def confirmation():
    return render_template("confirmation.html")


@app.route("/stt", methods=["POST"])
def transcribe():
    if request.method == "POST":
        # transcribe the audio
        try:
            text = speech_to_text(duration=5, lang="en-US")
        except Exception:
            text = "I'm having trouble understanding your response."
            return render_template("transcription.html", text=text, label="neutral")
        # sentiment analysis
        sentiment, label = utils.sentiment_analysis(text)
        # get the animal class from the submitted form
        animal_class = request.form.get("animal_class")
        n_animals = request.form.get("n_animals")
        if label == "positive":
            # generate the story
            text = utils.generate_story(n_animals, animal_class)
        elif label == "negative":
            text = "I am sorry for the mistake. Let's try it again!"
        else:
            text = "I'm having trouble understanding your response."
        return render_template("transcription.html", text=text, label=label)


if __name__ == "__main__":
    app.run(debug=True)
