from flask import Flask, request
import json

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "Bot aktif!"

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    print("Gelen veri:", data)

    comment = data.get("comment", "")
    if "BUY" in comment:
        print("AL sinyali geldi!")
        # Buraya Binance AL emri yazılacak
    elif "SELL" in comment:
        print("SAT sinyali geldi!")
        # Buraya Binance SAT emri yazılacak

    return "OK", 200

if __name__ == "__main__":
    app.run(debug=True)
