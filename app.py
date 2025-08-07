
from flask import Flask, render_template, session, redirect, url_for
import random

app = Flask(__name__)
app.secret_key = 'secret_key'

# 3 deste kart oluştur
suits = ['♥', '♦', '♣', '♠']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
deck = [f"{rank}{suit}" for rank in ranks for suit in suits] * 3

def deal_cards(num_players=2):
    random.shuffle(deck)
    hands = {f"Player {i+1}": sorted(deck[i*14:(i+1)*14]) for i in range(num_players)}
    return hands

@app.route("/")
def index():
    hands = deal_cards(2)
    return render_template("index.html", hands=hands)

if __name__ == "__main__":
    app.run(debug=True)
