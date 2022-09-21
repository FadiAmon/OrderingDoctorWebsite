from lib2to3.pgen2 import driver

from flask import Flask, render_template, request, redirect, send_from_directory
import sqlite3
import os

app = Flask(__name__,template_folder='template')

currentdirectory = os.path.dirname(os.path.abspath(__file__))
# conn = sqlite3.connect('database.db')
# conn.execute('CREATE TABLE items (name TEXT, price INT)')
APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route('/', methods=['POST','GET'])
def show_table():
    # if request.method == 'POST':
    #
    #     if request.form.get("Back"):
    #         return Patient_()
    #
    # else:
        email="yytt@gmail.com"
        Admin="Admin"
        Patient="Patient"
        headings = ("Doctor", "Email", "Specialty")
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()

        address_of_patient="SELECT address FROM login WHERE email =?"
        addresses_of_doctors = "SELECT first_name,email,Specialty FROM login WHERE D_P_A !=? AND D_P_A !=?"
        result = cursor.execute(addresses_of_doctors, (Admin,Patient,)).fetchall()



        return render_template('Filter_Specialty_D.html', headings=headings, data=result)

@app.route('/Filter_Specialty', methods=['POST','GET'])
def Filter_Specialty():
    selected_item = request.form["Specialty"]



    if request.method == 'POST':
        if request.form.get("Filter_Specialty"):

            return redirect('/')

    else:
        return render_template('Filter_Specialty_D.html')



#@app.route('/')
#def Main():
    #return render_template('Main.html')


if __name__ == '__main__':
    app.debug = True
    app.run()

