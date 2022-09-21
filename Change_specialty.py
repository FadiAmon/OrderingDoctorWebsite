import pypyodbc as odbc
from flask import Flask, render_template, request, redirect, send_from_directory



app = Flask(__name__,template_folder='templates')

DRIVER_NAME = 'SQL SERVER'
SERVER_NAME = 'WARD'
DATABASE_NAME = 'project'

connection_string = f"""
    DRIVER={{{DRIVER_NAME}}};
    SERVER={SERVER_NAME};
    DATABASE={DATABASE_NAME};
    Trust_connection=yes;
"""


message_____ = ''


def get_first():
    conn = odbc.connect(connection_string)
    cursor = conn.cursor()
    first = "SELECT first_name FROM Login WHERE email=?"
    result = cursor.execute(first, ('tot@gmail.com',)).fetchone()
    return result[0]


def get_last():
    conn = odbc.connect(connection_string)
    cursor = conn.cursor()
    last = "SELECT last_name FROM Login WHERE email=?"
    result = cursor.execute(last, ('tot@gmail.com',)).fetchone()
    return result[0]


@app.route('/', methods=['POST', 'GET'])
def Change_Specialty():
    if request.method == 'POST':
        if request.form.get("Change"):
            specialty = request.form["specialty"]
            if specialty == '':
                __error____()
            else:
                reset___message_____()
                conn = odbc.connect(connection_string)
                cursor = conn.cursor()

                update = "UPDATE Login SET D_P_A = ? WHERE first_name =? AND last_name =? AND email =?"
                cursor.execute(update, (specialty, get_first(), get_last(), 'tot@gmail.com',))
                conn.commit()
            return redirect('/')

        elif request.form.get("Back"):
            reset___message_____()
            return Doctor()
    else:
        print(1)
        headings = ("First_Name", "Last_Name", "Email", "Doctor")
        conn = odbc.connect(connection_string)
        cursor = conn.cursor()
        specialty_ = "SELECT first_name,last_name,email,D_P_A FROM Login WHERE email = ?"
        result = cursor.execute(specialty_, ('tot@gmail.com',)).fetchall()
        return render_template('Doctor_Change_specialty.html', headings=headings, data=result,
                               message=_get__message_____())


def __error____():
    global message_____
    message_____ = 'Invalid'


def reset___message_____():
    global message_____
    message_____ = ''


def _get__message_____():
    global message_____
    return message_____


if __name__ == '__main__':
    app.debug = True
    app.run()