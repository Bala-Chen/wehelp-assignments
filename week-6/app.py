import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    port="3306",
    user="root",
    password="test123",
    database="website"
)
cursor = connection.cursor()

from flask import *

app = Flask(__name__)
app.secret_key = "test123"

@app.route("/")
def index():
    return render_template ("index.html")

@app.route("/signup",methods=["POST"])
def signup():
    name = request.form["name"]
    username = request.form["username"]
    password = request.form["password"]
    signup_sql = "SELECT member.username FROM member WHERE username= %s;"
    signup_val = (username,)
    cursor.execute(signup_sql,signup_val)
    check_username = cursor.fetchall()
    if check_username == []:
        add_sql = "INSERT INTO member(name,username,password) VALUES (%s,%s,%s)"
        add_val = (name,username,password)
        cursor.execute(add_sql,add_val)
        connection.commit()
        return redirect('/')
    elif check_username != []:
        return redirect("/error?message=帳號已經被註冊")
    else:
        return redirect("/error?message=預期外的錯誤")

@app.route("/signin", methods=["POST"])
def signin():
    username = request.form["username"]
    password = request.form["password"]
    try:
        signin_sql = "SELECT member.name,username,password FROM member WHERE username = %s AND password = %s"
        signin_val = (username,password)
        cursor.execute(signin_sql,signin_val)
        verify_account = cursor.fetchall()
        for data in verify_account:
            main_data = list(data) 
        session["name"]= main_data[0]
        return redirect("/member")
    except NameError:    
        return redirect("/error?message=帳號或密碼輸入錯誤")
    else:
        return redirect("/error?message=預期外的錯誤")


@app.route("/member")
def member():
    if "name" in session:
        name = session["name"]
        return render_template("member.html",name = name)
    else:
        return redirect("/")

@app.route("/error")
def error():
    message = request.args.get("message")
    return render_template("error.html",message = message)

@app.route("/signout")
def signout():
    del session["name"]
    return redirect("/")

if __name__ == "__main__":
    app.run(port=3000)