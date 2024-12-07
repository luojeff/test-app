from flask import Flask, render_template
import json

app = Flask(__name__)

# Global variable
app.config["x"] = 0
    
@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
