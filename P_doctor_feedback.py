from flask import Flask, render_template, request, redirect, send_from_directory
import sqlite3
import os

app = Flask(__name__,template_folder='template')

currentdirectory = os.path.dirname(os.path.abspath(__file__))
# conn = sqlite3.connect('database.db')
# conn.execute('CREATE TABLE items (name TEXT, price INT)')
APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route('/', methods=['POST','GET'])
def P_doctor_feedback():
    if request.method == 'POST':
        if request.form.get("P_doctor_feedback"):

            headings=['Patinet\'s name', 'Email','doctor feedback']
            print("button works")
            patient="Patient"
            conn = sqlite3.connect('database.db')
            cursor = conn.cursor()
            result = "SELECT first_name,email,doctor_feedback FROM Login WHERE D_P_A = ?"
            result = cursor.execute(result, (patient,)).fetchall()
            print(result)
            conn.commit()

            return render_template('doctor_feedback_P.html', headings=headings, data=result)

    else:
        return render_template('doctor_feedback_P.html')


#@app.route('/')
#def Main():
    #return render_template('Main.html')


if __name__ == '__main__':
    app.debug = True
    app.run()
