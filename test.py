from flask import Flask, render_template, request
import json

app = Flask(__name__)

# Global variable
napp.config["x"] = 0
    
@app.route("/", methods=["GET", "POST"])
def index():
    valu = 0;
    if request.method == "POST":
        valu = 5
    
    return render_template("index.html", val=valu)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
