from flask import Flask, render_template, request, redirect, send_from_directory
import sqlite3
import os

app = Flask(__name__,template_folder='template')

currentdirectory = os.path.dirname(os.path.abspath(__file__))
# conn = sqlite3.connect('database.db')
# conn.execute('CREATE TABLE items (name TEXT, price INT)')
APP_ROOT = os.path.dirname(os.path.abspath(__file__))


@app.route('/', methods=['POST','GET'])
def add_note():
    if request.method == 'POST':
        if request.form.get("add_note"):
            notes=request.form.get("note")
            print(notes)
            print("button works")
            email="ward@gmail.com" #email of patient
            conn = sqlite3.connect('database.db')
            cursor = conn.cursor()
            update = "UPDATE Login SET notes = ? WHERE email =?"
            cursor.execute(update, (notes, email,))
            conn.commit()

            return redirect('/')

    else:
        return render_template('Patient_note_P.html')


#@app.route('/')
#def Main():
    #return render_template('Main.html')


if __name__ == '__main__':
    app.debug = True
    app.run()
