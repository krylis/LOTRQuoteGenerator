from flask import Flask, redirect, render_template
import requests as r
import random

API_KEY = "Bearer wKkYeJvglLvyiW2YeOc4"
API_URL = "https://the-one-api.dev/v2/character"

app = Flask(__name__)


# returns data concerning 9 random character from lord of the rings
def get_ten_random_characters():
    response = r.get(API_URL, headers={"Authorization": API_KEY})
    response.raise_for_status()
    data = response.json()['docs']
    random_characters = []
    for _ in range(9):
        character = random.choice(data)
        random_characters.append(character)
    return random_characters


@app.route('/')
def home():
    random_characters = get_ten_random_characters()
    return render_template("index.html", characters=random_characters)


if __name__ == "__main__":
    app.run()
