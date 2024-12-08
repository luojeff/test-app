from flask import Flask, render_template, request
import json

app = Flask(__name__)

# Global variable
app.config["x"] = 0
    
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        return "Submitted!"
    
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
