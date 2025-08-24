from flask import Flask, render_template, jsonify
import random, requests

app = Flask(__name__)

# Local quotes
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

@app.route("/about")
def about():
    return render_template("about.html")

# Local API
@app.route("/api/quote")
def api_quote():
    return jsonify(random.choice(quotes))

# External Zenquotes API
@app.route("/api/zenquotes")
def api_zenquotes():
    try:
        res = requests.get("https://zenquotes.io/api/random", timeout=5)
        res.raise_for_status()
        data = res.json()[0]  # zenquotes returns a list
        return jsonify({
            "author": data.get("a", "Unknown"),
            "quote": data.get("q", "No content")
        })
    except Exception as e:
        print("Quote API Error:", e)
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)