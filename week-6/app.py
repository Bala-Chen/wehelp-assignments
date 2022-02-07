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
    cursor.execute('SELECT member.username FROM member;')
    check_username = cursor.fetchall()
    if (username,) in check_username :
        return redirect("/error?message=帳號已經被註冊")
    elif (username,) not in check_username :
        sql = "INSERT INTO member(name,username,password) VALUES (%s,%s,%s)"
        val = (name,username,password)
        cursor.execute(sql,val)
        connection.commit()
        return redirect('/')
    else:
        return redirect("/error?message=預期外的錯誤")

@app.route("/signin", methods=["POST"])
def signin():
    username = request.form["username"]
    password = request.form["password"]
    try:
        sql = "SELECT * FROM member WHERE username = %s AND password = %s"
        val = (username,password)
        cursor.execute(sql,val)
        verify_account = cursor.fetchall()
        for data in verify_account:
            main_data = list(data) 
        session["name"]= main_data[1]
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