from flask import *

app = Flask(__name__)
app.secret_key = "test123"

@app.route("/")
def index():
    return render_template ("index.html")

@app.route("/signin", methods=["POST"])
def signin():
    username = request.form["username"]
    password = request.form["password"]
    if username == "test" and password == "test":
        session["name"]= username
        return redirect("/member")
    elif username == "" or password == "":
        return redirect("/error?message=請輸入帳號、密碼")
    elif username != "test" or password != "test":
        return redirect("/error?message=帳號、或密碼輸入錯誤")
    else:
        return redirect("/error?message=預期外的錯誤")


@app.route("/member")
def member():
    if "name" in session:
        return render_template("member.html")
    else:
        return redirect("/")

@app.route("/error")
def error():
    message = request.args.get("message")
    return render_template("error.html",message = message)

@app.route("/signup")
def signup():
    del session["name"]
    return redirect("/")

if __name__ == "__main__":
    app.run(port=3000)