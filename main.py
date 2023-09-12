from flask import Flask, requests, redirect, render_template
import requests as r
API_KEY = "Bearer wKkYeJvglLvyiW2YeOc4"
API_URL = "https://the-one-api.dev/v2/"

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")
