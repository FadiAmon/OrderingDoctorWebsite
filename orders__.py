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

email = 'qoq@gmail.com'

@app.route('/')
def Orders_History():
    headings = ("First_Name", "Last_Name", "status", "Doctor Note")
    conn = odbc.connect(connection_string)
    cursor = conn.cursor()
    order = "SELECT first_name,last_name,status,notes FROM history WHERE email_p =?"
    result = cursor.execute(order, (get_email(),)).fetchall()
    return render_template('Orders_History.html', headings=headings, data=result)

def get_email():
    global email
    return email

if __name__ == '__main__':
    app.debug = True
    app.env = "development"
    app.run(host="localhost", port=5000)