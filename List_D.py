import pypyodbc as odbc
from flask import Flask, render_template, request, redirect, send_from_directory

message_______ = ''

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



def get__first_():
    conn = odbc.connect(connection_string)
    cursor = conn.cursor()
    first = "SELECT first_name FROM Login WHERE email=?"
    result = cursor.execute(first, ('tot@gmail.com',)).fetchone()
    return result[0]


def get__last_():
    conn = odbc.connect(connection_string)
    cursor = conn.cursor()
    last = "SELECT last_name FROM Login WHERE email=?"
    result = cursor.execute(last, ('tot@gmail.com',)).fetchone()
    return result[0]


@app.route('/', methods=['POST', 'GET'])
def Order_Doc():
    if request.method == 'POST':

        if request.form.get("Done"):
            first_name = request.form["first_name"]
            last_name = request.form["last_name"]
            email = request.form["email"]
            # doctor = get_d_p_a_()
            # status = 'Available'
            status_ = 'Done'
            if first_name == '' or last_name == '' or email == '':
                ___error____()
            else:
                reset____message_____()
                conn = odbc.connect(connection_string)
                cursor = conn.cursor()

                # update = "UPDATE Login SET status = ? WHERE first_name =? AND last_name =? AND email =? AND D_P_A =?"
                # cursor.execute(update, (status, get__first_(), get__last_(), get_email(), doctor,))
                # conn.commit()

                update_ = "UPDATE Order_Doc SET status = ? WHERE first_name =? AND last_name =? AND email_p =?"
                cursor.execute(update_, (status_, first_name, last_name, email,))
                conn.commit()

                update__ = "UPDATE history SET status = ? WHERE first_name =? AND last_name =? AND email_p =? AND email_d=?"
                cursor.execute(update__, (status_, get__first_(), get__last_(), email, 'tot@gmail.com',))
                conn.commit()
            return redirect('/')

        elif request.form.get("Back"):
            reset____message_____()
            return Doctor()

    else:
        headings = ("First_Name", "Last_Name", "Email", "Status")
        conn = odbc.connect(connection_string)
        cursor = conn.cursor()
        order = "SELECT first_name,last_name,email_p,status FROM Order_Doc"
        result = cursor.execute(order, ).fetchall()
        return render_template('Order_Doc.html', headings=headings, data=result, message=__get__message_____())


def ___error____():
    global message_______
    message_______ = 'Invalid'


def reset____message_____():
    global message_______
    message_______ = ''


def __get__message_____():
    global message_______
    return message_______


if __name__ == '__main__':
    app.debug = True
    app.run()