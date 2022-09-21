from flask import Flask, render_template, request, redirect, send_from_directory
import pyodbc as odbc
import os
import googlemaps

app = Flask(__name__,template_folder='templates')

@app.route('/')
def Paypal():
    return render_template('Paypal.html')

if __name__ == '__main__':
    app.debug = True
    app.env = "development"
    app.run(host="localhost")