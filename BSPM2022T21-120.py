from flask import Flask, render_template, request, redirect, send_from_directory
import pyodbc as odbc
import os
import googlemaps


app = Flask(__name__,template_folder='templates')
connection_string = (
    r'Driver=ODBC Driver 17 for SQL Server;'
    r'Server=tcp:wardp.database.windows.net,1433;'
    r'Database=project;'
    r'UID=ward;'
    r'PWD=Wa246810;'
    r'MARS_Connection=yes;'
    r'APP=yourapp'
    )



def get_first():
    conn = odbc.connect(connection_string)
    cursor = conn.cursor()
    first = "SELECT first_name FROM Login WHERE email=?"
    result = cursor.execute(first, (get_email(),)).fetchone()
    return result[0]


def get_last():
    conn = odbc.connect(connection_string)
    cursor = conn.cursor()
    last = "SELECT last_name FROM Login WHERE email=?"
    result = cursor.execute(last, (get_email(),)).fetchone()
    return result[0]



########################################## Cancel_Order #################
@app.route('/', methods=['POST', 'GET'])
def Cancel_Order():
    if request.method == 'POST':

        if request.form.get("Delete"):
            first_name = request.form["first_name"]
            last_name = request.form["last_name"]
            email = request.form["email"]
            conn = odbc.connect(connection_string)
            cursor = conn.cursor()

            delete = "DELETE FROM history WHERE first_name=? AND last_name=? AND email_d=? AND status=? AND email_p=?"
            cursor.execute(delete, (first_name, last_name, email, 'Waiting to approve', get_email(),))
            conn.commit()

            delete_ = "DELETE FROM Order_Doc WHERE first_name=? AND last_name=? AND email_p=? AND email_d=? AND status=?"
            cursor.execute(delete_, (get_first_(), get_last(), get_email(), email, 'Waiting to approve',))
            conn.commit()

            update = "UPDATE Login SET count_ = ? WHERE first_name =? AND last_name =? AND email =?"
            cursor.execute(update, (check_count_(first_name, last_name, email)-1, first_name, last_name, email,))
            conn.commit()

            return redirect('/Cancel_Order')

    else:
        headings = ("First Name", "Last Name", "Email-D", "Status")
        conn = odbc.connect(connection_string)
        cursor = conn.cursor()
        order = "SELECT first_name,last_name,email_d,status FROM history WHERE email_p =? AND status=?"
        result = cursor.execute(order, (get_email(), 'Waiting to approve',)).fetchall()
        return render_template('Cancel_Order_P.html', headings=headings, data=result)


if __name__ == '__main__':
    app.debug = True
    app.env = "development"
    app.run(host="localhost", port=5000)