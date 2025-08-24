from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

quotes = [
    {"author": "Walt Disney", "quote": "The best way to get started is to quit talking and begin doing."},
    {"author": "Will Rogers", "quote": "Don't let yesterday take up too much of today."},
    {"author": "Vince Lombardi", "quote": "It's not whether you get knocked down, it's whether you get up."},
    {"author": "Steve Jobs", "quote": "If you are working on something exciting, it will keep you motivated."},
    {"author": "Bo Bennett", "quote": "Success is not in what you have, but who you are."},
    {"author": "Lord Godwill Taylor", "quote": "Life they say is not fair, learn to give yourself an unfair advantage."}
]

@app.route("/")
def home():
    quote = random.choice(quotes)
    return render_template("index.html", quote=quote)

@app.route("/api/quote")
def api_quote():
    return jsonify(random.choice(quotes))

if __name__ == "__main__":
    app.run(debug=True)