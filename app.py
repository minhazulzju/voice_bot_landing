# Basic Flask app for landing page with three chat mode options
from flask import Flask, render_template

app = Flask(__name__)


URLS = {
    "voice_bot": "https://chatgpt.com/c",
    "abstract": "https://voice-bot-delta.vercel.app/",
    "cartoonish_mode": "https://gglabs.kikiz.ai/?mode=call",
    "human_realistic_voice_bot": "https://studio.d-id.com/agents/share?id=v2_agt_-QvaV_gx&key=WVhWMGFEQjhOamsyTTJNNFpUYzJNalkwWXpFMk16Y3pZakF5WWpFMk9sOW5lalZsZDNsemVXeFZUbFoxU2kxWVVFNHdOZz09",
}


@app.route("/")
def landing():
    return render_template("index.html", urls=URLS)


if __name__ == "__main__":
    app.run(debug=True)
