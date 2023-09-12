from flask import Flask, render_template
import requests as r
import random
import pprint

API_KEY = "Bearer wKkYeJvglLvyiW2YeOc4"
API_URL = "https://the-one-api.dev/v2"

app = Flask(__name__)


# returns data concerning 9 random characters from lord of the rings
def get_random_characters():
    response = r.get(API_URL + "/character",
                     headers={"Authorization": API_KEY})
    response.raise_for_status()
    data = response.json()['docs']
    random_characters = []
    for _ in range(9):
        character = random.choice(data)
        random_characters.append(character)
    return random_characters


# returns a random quote from the Lord of the Rings movies
def get_random_quote():
    response = r.get(API_URL + "/quote",
                     headers={"Authorization": API_KEY})
    response.raise_for_status()
    data = response.json()['docs']
    random_quote = random.choice(data)
    quote_id = random_quote['id']

    response = r.get(API_URL + "/quote/" + quote_id,
                     headers={"Authorization": API_KEY})
    response.raise_for_status()
    quote = response.json()['docs'][0]
    return quote


def get_quote_character(character_id):
    response = r.get(API_URL + "/character/" + character_id,
                     headers={"Authorization": API_KEY})
    response.raise_for_status()
    character = response.json()['docs'][0]
    return character['name']


def get_quote_movie(movie_id):
    response = r.get(API_URL + "/movie/" + movie_id,
                     headers={"Authorization": API_KEY})
    response.raise_for_status()
    movie = response.json()['docs'][0]
    return movie['name']


@app.route('/')
def home():
    random_characters = get_random_characters()
    random_quote = get_random_quote()
    quote = random_quote['dialog']
    quote_character = get_quote_character(random_quote['character'])
    quote_movie = get_quote_movie(random_quote['movie'])
    return render_template("index.html", characters=random_characters,
                           quote=quote, character=quote_character,
                           movie=quote_movie)


if __name__ == "__main__":
    app.run(debug=True)
