from flask import Flask, render_template

import random

app = Flask(__name__)

def generate_caption(mood):
    mood = mood.lower().strip()

    if mood == "sad":
        captions = [
            "You are beautiful, it's okay to feel sad sometimes 💙",
            "Even sad days have their own beauty 🌧️",
            "Be gentle with yourself today 💫"
        ]
    elif mood == "happy":
        captions = [
            "Living my happy moment 💫",
            "Smiling for no reason today ☀️",
            "Happiness looks good on me 💛"
        ]
    else:
        captions = [
            f"In my {mood} era ✨",
            f"Feeling {mood} today 🌙",
            f"A little bit of {mood} energy 💖"
        ]

    return random.choice(captions)
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/<mood>")
def mood_page(mood):
    caption = generate_caption(mood)
    return render_template("result.html", mood = mood, caption = caption)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=False)