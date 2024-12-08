from flask import Flask, render_template, request
import json

app = Flask(__name__)
app.config["nam"] = "Jeffrey"
    
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if app.config["nam"] == "Jeffrey":
            app.config["nam"] = "Kelly"
        else:
            app.config["nam"] = "Jeffrey"    
    
    return render_template("index.html", name = app.config["nam"])

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
