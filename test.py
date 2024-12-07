from flask import Flask
import json

app = Flask(__name__)

xx = 10
    
@app.route("/data", methods=["GET"])
def index():
    mydict = {"data": x}
    return json.dumps(mydict)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
