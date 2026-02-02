from flask import Flask, jsonify
import json
import os

app = Flask(__name__)

@app.route("/api/liste")
def liste():
    with open("output/shab_zefix_adressen.json", encoding="utf-8") as f:
        return jsonify(json.load(f))

@app.route("/healthz")
def healthz():
    return "ok"

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 10000))
    )
