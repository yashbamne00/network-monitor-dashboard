from flask import Flask, render_template
import json

app = Flask(__name__, static_url_path="", static_folder=".", template_folder=".")

@app.route("/")
def home():
  with open("data.json", "r") as f:
    metric = json.load(f)
  return render_template("index.html", data=metric)

if __name__ == "__main__":
  app.run()