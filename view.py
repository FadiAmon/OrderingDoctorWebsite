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

@app.route('/')
def View_orders():
    headings = ("First Name-P", "Last Name-P", "Email-P", "Email-D", "Status")
    conn = odbc.connect(connection_string)
    cursor = conn.cursor()
    order = "SELECT first_name,last_name,email_p,email_d,status FROM Order_Doc"
    result = cursor.execute(order).fetchall()
    return render_template('Admin_View_Orders.html', headings=headings, data=result)


if __name__ == '__main__':
    app.debug = True
    app.env = "development"
    app.run(host="localhost", port=5000)