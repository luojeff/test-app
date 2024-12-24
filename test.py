from flask import Flask, render_template, request
from query_db import get_db_connection
import json

app = Flask(__name__)
    
@app.route("/", methods=["GET", "POST"])
def index():
    print(request.method)
    return render_template("index.html")

@app.route("/query", methods=["GET", "POST"])
def query():
    conn = get_db_connection()
    cur = conn.cursor()

    print (request.method)

    if request.method == 'POST':
        cur.execute("INSERT INTO test_table(name, age) VALUES (%s, %s);", (request.form.get("name"), request.form.get("age")))
        conn.commit()
        print("Post executed!")

    cur.execute("SELECT * FROM test_table;")
    data = cur.fetchall()

    cur.close()
    conn.close()

    return render_template("index.html", li=data)
    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
