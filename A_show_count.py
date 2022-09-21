from flask import Flask, render_template, request, redirect, send_from_directory
import sqlite3
import os
import pyodbc as odbc

app = Flask(__name__,template_folder='templates')

currentdirectory = os.path.dirname(os.path.abspath(__file__))
# conn = sqlite3.connect('database.db')
# conn.execute('CREATE TABLE items (name TEXT, price INT)')
APP_ROOT = os.path.dirname(os.path.abspath(__file__))

connection_string = (
    r'Driver=ODBC Driver 17 for SQL Server;'
    r'Server=tcp:wardp.database.windows.net,1433;'
    r'Database=project;'
    r'UID=ward;'
    r'PWD=Wa246810;'
    r'MARS_Connection=yes;'
    r'APP=yourapp'
    )

@app.route('/', methods=['POST','GET'])
def calc_count():
    if request.method == 'POST':
        if request.form.get("calc_count"):

            headings=['Patinet\'s name', 'Email','Order_count']
            print("button works")
            result = ret_result()
            print(result)
            return render_template('show_count_A.html', headings=headings, data=result)

    else:
        return render_template('show_count_A.html')


def ret_result():
    doctor = "Doctor"
    conn = odbc.connect(connection_string)
    cursor = conn.cursor()
    result = "SELECT first_name,email,count_o FROM Login WHERE D_P_A = ?"
    result = cursor.execute(result, (doctor,)).fetchall()
    conn.commit()
    return result
#@app.route('/')
#def Main():
    #return render_template('Main.html')


if __name__ == '__main__':
    app.debug = True
    app.run()
