from flask import Flask, render_template, request, redirect, send_from_directory
import pypyodbc as odbc
import os

app = Flask(__name__,template_folder='templates')

currentdirectory = os.path.dirname(os.path.abspath(__file__))
# conn = sqlite3.connect('database.db')
# conn.execute('CREATE TABLE items (name TEXT, price INT)')
APP_ROOT = os.path.dirname(os.path.abspath(__file__))


DRIVER_NAME = 'SQL SERVER'
SERVER_NAME = 'WARD'
DATABASE_NAME = 'project'

connection_string = f"""
    DRIVER={{{DRIVER_NAME}}};
    SERVER={SERVER_NAME};
    DATABASE={DATABASE_NAME};
    Trust_connection=yes;
"""


@app.route('/', methods=['POST','GET'])
def Change_status():
    if request.method == 'POST':
        if request.form.get("Change_status"):
            print("hi")
            email="tot@gmail.com"
            conn = odbc.connect(connection_string)
            cursor = conn.cursor()
            get_avaiable = "SELECT status FROM login WHERE email=?"
            result = cursor.execute(get_avaiable, (email,)).fetchall()[0][0]
            print(result)
            Not_available = "Unavailable"
            Available = "Available"
            if result == "Available":
               update = "UPDATE Login SET status = ? WHERE email =?"
               cursor.execute(update, (Not_available, email,))
               conn.commit()
            else:
                update = "UPDATE Login SET status = ? WHERE email =?"
                cursor.execute(update, (Available, email,))
                conn.commit()

            return redirect('/')

    else:
        return render_template('Change_status_D.html')



if __name__ == '__main__':
    app.debug = True
    app.run()
