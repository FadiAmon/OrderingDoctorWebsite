from flask import Flask, render_template, request, redirect, send_from_directory
import sqlite3
import os

app = Flask(__name__,template_folder='templates')

currentdirectory = os.path.dirname(os.path.abspath(__file__))
# conn = sqlite3.connect('database.db')
# conn.execute('CREATE TABLE items (name TEXT, price INT)')
APP_ROOT = os.path.dirname(os.path.abspath(__file__))



@app.route('/', methods=['POST', 'GET'])
def Order_Doc():
    if request.method == 'POST':

        if request.form.get("Approval"):
            conn = sqlite3.connect('database (1).db')
            cursor = conn.cursor()
            first_name = request.form["first_name"]
            last_name = request.form["last_name"]
            email = request.form["email"]
            status_ = 'Approval'

            update_ = "UPDATE Order_Doc SET APR = ? WHERE first_name =? AND last_name =? AND email_p =?"
            cursor.execute(update_, (status_, first_name, last_name, email,))
            conn.commit()
            return redirect('/')

        elif request.form.get("DisApproval"):
            conn = sqlite3.connect('database (1).db')
            cursor = conn.cursor()
            first_name = request.form["first_name"]
            last_name = request.form["last_name"]
            email = request.form["email"]
            status_ = 'DisApproval'

            update_ = "UPDATE Order_Doc SET APR = ? WHERE first_name =? AND last_name =? AND email_p =?"
            cursor.execute(update_, (status_, first_name, last_name, email,))
            conn.commit()
            return redirect('/')

    else:
        headings = ("First_Name", "Last_Name", "Email", "Status","APR")
        conn = sqlite3.connect('database (1).db')
        cursor = conn.cursor()
        order = "SELECT first_name,last_name,email_p,status,apr FROM Order_Doc WHERE email_d = ?"
        result = cursor.execute(order, ("eekk@gmail.com",)).fetchall()
        return render_template('Order_Doc.html', headings=headings, data=result)


if __name__ == '__main__':
    app.debug = True
    app.run()