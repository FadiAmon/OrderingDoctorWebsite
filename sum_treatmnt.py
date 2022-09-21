from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3 as sql

app = Flask(__name__)


@app.route("/")
@app.route("/index")
def index():
    con = sql.connect("db_web.db")
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("select * from users")
    data = cur.fetchall()
    return render_template("index.html", datas=data)


@app.route("/Patient_R")
def Patient_R():
    con = sql.connect("db_web.db")
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("select * from users")
    data = cur.fetchall()
    return render_template("Patient_R.html", datas=data)

@app.route("/sum_of_tr")
def sum_of_tr():
    con = sql.connect("db_web.db")
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("select * from users")
    data = cur.fetchall()
    return render_template("sum_of_tr.html", datas=data)

@app.route("/show_sum_tr")
def show_sum_tr():
    con = sql.connect("db_web.db")
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("select * from users")
    data = cur.fetchall()
    return render_template("show_sum_tr.html", datas=data)
@app.route("/add_user", methods=['POST', 'GET'])
def add_user():
    if request.method == 'POST':
        First_Name = request.form['First_Name']
        Last_Name= request.form['Last_Name']
        uname = request.form['uname']
        contact = request.form['contact']
        sum=request.form['sum']
        con = sql.connect("db_web.db")
        cur = con.cursor()
        cur.execute("insert into users(first_name,last_name,email_p,CONTACT,SUM) values (?,?,?,?,?)", (First_Name ,Last_Name,uname, contact,sum))
        con.commit()
        flash('Appointment Added', 'success')
        return redirect(url_for("index"))
    return render_template("add_user.html")


@app.route("/edit_user2/<string:uid>", methods=['POST', 'GET'])
def edit_user2(uid):
    if request.method == 'POST':
        sum = request.form['sum']
        con = sql.connect("db_web.db")
        cur = con.cursor()
        cur.execute("update users set SUM=? where UID=?", (sum,  uid))
        con.commit()
        flash('246546', 'success')
        return redirect(url_for("index"))
    con = sql.connect("db_web.db")
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("select * from users where UID=?", (uid,))
    data = cur.fetchone()
    return render_template("edit_user2.html", datas=data)






if __name__ == '__main__':
    app.secret_key = 'admin123'
    app.run(debug=True)
