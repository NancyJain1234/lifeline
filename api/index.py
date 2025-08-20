from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

# Vercel needs this handler
def handler(event, context):
    return app(event, context)
