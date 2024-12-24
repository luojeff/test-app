from flask import Flask, render_template, request
from query_db import get_db_connection
import json

app = Flask(__name__)
    
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        return "button pressed"
    
    return render_template("index.html")

@app.route("/query", methods=["GET", "POST"])
def query():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM test_table;")
    data = cur.fetchall()
    cur.close()
    conn.close()

    return render_template("index.html", li=data)
    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
