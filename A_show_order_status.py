from flask import Flask, render_template, request, redirect, send_from_directory
import sqlite3
import os

app = Flask(__name__,template_folder='template')

currentdirectory = os.path.dirname(os.path.abspath(__file__))
# conn = sqlite3.connect('database.db')
# conn.execute('CREATE TABLE items (name TEXT, price INT)')
APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route('/', methods=['POST','GET'])
def order_status():
    if request.method == 'POST':
        if request.form.get("order_status"):

            headings=['Patinet\'s name', 'Email','Order_status']
            print("button works")
            result = ret_result()
            print(result)
            return render_template('show_order_status_A.html', headings=headings, data=result)

    else:
        return render_template('show_order_status_A.html')


def ret_result():
    doctor = "Doctor"
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    result = "SELECT first_name,email,Order_completed FROM Login WHERE D_P_A = ?"
    result = cursor.execute(result, (doctor,)).fetchall()
    conn.commit()
    return result
#@app.route('/')
#def Main():
    #return render_template('Main.html')


if __name__ == '__main__':
    app.debug = True
    app.run()
