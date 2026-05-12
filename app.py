from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    message = None
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        message = (
            "Login is a placeholder for now. "
            f"You submitted username: {username or '(empty)'}"
        )

    return render_template("login.html", message=message)


if __name__ == "__main__":
    # Run a local dev server
    app.run(debug=True, host="0.0.0.0", port=5000)

