import mysql.connector
import json
from mysql.connector import pooling


cnxpool = mysql.connector.pooling.MySQLConnectionPool(
    pool_name="mypool",
    pool_reset_session=True,
    host="localhost" ,
    port=3306,
    user="root",
    password="test123",
    database="website"
)

from flask import *

app = Flask(__name__)
app.secret_key = "test123"


@app.route("/")
def index():
    return render_template ("index.html")

@app.route("/signup",methods=["POST"])
def signup():
    conn1 = cnxpool.get_connection()
    cursor = conn1.cursor()
    name = request.form["name"]
    username = request.form["username"]
    password = request.form["password"]
    if username == '' or password == '':
        return redirect("/error?message=帳號密碼不得為空")
    signup_sql = "SELECT member.username FROM member WHERE username= %s;"
    signup_val = (username,)
    cursor.execute(signup_sql,signup_val)
    check_username = cursor.fetchall()
    if check_username == []:
        add_sql = "INSERT INTO member(name,username,password) VALUES (%s,%s,%s)"
        add_val = (name,username,password)
        cursor.execute(add_sql,add_val)
        cursor.close()
        conn1.commit()
        conn1.close()
        return redirect('/')
    elif check_username != []:
        return redirect("/error?message=帳號已經被註冊")
    else:
        return redirect("/error?message=預期外的錯誤")

@app.route("/signin", methods=["POST"])
def signin():
    conn2 = cnxpool.get_connection()
    cursor = conn2.cursor()
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
        session["username"]= main_data[1]
        return redirect("/member")
    except NameError:    
        return redirect("/error?message=帳號或密碼輸入錯誤")
    else:
        return redirect("/error?message=預期外的錯誤")
    finally:
        cursor.close()
        conn2.close()


@app.route("/member")
def member():
    if "name" in session:
        name = session["name"]
        return render_template("member.html",name = name)
    else:
        return redirect("/")

@app.route("/api/members")
def api_members():
    username = request.args.get("username", None)
    conn3 = cnxpool.get_connection()
    cursor = conn3.cursor()
    try:
        sql = "SELECT id,name,username FROM member WHERE username = %s"
        val = (username,)
        cursor.execute(sql,val)
        data = cursor.fetchone()
        if data == None:
            js_none = None 
            return json.dumps({"data":js_none})
        else:
            return json.dumps({"data":{"id":data[0],"name":data[1],"username":data[2]}},ensure_ascii=False)
    finally:
        cursor.close()
        conn3.close()

@app.route("/api/member", methods=["POST"])
def api_member():
    if "name" in session:
        new_name = request.get_json()
        conn4 = cnxpool.get_connection()
        cursor = conn4.cursor()
        check_name = session["username"]
        sql = "UPDATE member SET name=%s where username=%s"
        val = (new_name.get("name"),check_name)
        cursor.execute(sql,val)
        cursor.close()
        conn4.commit()
        conn4.close()
        return json.dumps({"ok":True})
    else:
        return json.dumps({"error":True})

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