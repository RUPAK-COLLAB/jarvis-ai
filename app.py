
from flask import Flask, request, jsonify, render_template_string

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>JARVIS AI BACKEND</h1>
    <p>System is online!</p>
    """

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    message = data.get("message", "")

    reply = "I received your message: " + message

    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)
