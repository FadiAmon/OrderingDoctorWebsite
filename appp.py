from flask import Flask, render_template, request, redirect, send_from_directory
import googlemaps
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
def distance():
        email="yey@gmail.com"
        Admin="Admin"
        Patient="Patient"
        headings = ("Doctor", "Email", "Distance from you")
        conn = odbc.connect(connection_string)
        cursor = conn.cursor()

        address_of_patient="SELECT address FROM login WHERE email =?"
        result_patient_address = cursor.execute(address_of_patient, (email,)).fetchall()[0][0]
        addresses_of_doctors = "SELECT first_name,email,address FROM login WHERE D_P_A !=? AND D_P_A !=?"
        result = cursor.execute(addresses_of_doctors, (Admin,Patient,)).fetchall()

        present_date = []
        for doctor in result: #calculate distance of each doctor to patient
            distance = calc_distance_of_two_points(result_patient_address, doctor[2])
            present_date.append((doctor[0],doctor[1],distance))
        return render_template('distance_P.html', headings=headings, data=present_date)

# #find distance
def calc_distance_of_two_points(origin, destination):
    API_KEY = 'AIzaSyAnvbtvxM2Yq6xATgorTR1_ukymn3Ana1k'
    gmaps = googlemaps.Client(key=API_KEY)
    distance =gmaps.distance_matrix(origin, destination)['rows'][0]['elements'][0]
    return [distance['distance']['text'], distance['duration']['text']]

if __name__ == '__main__':
    app.debug = True
    app.run()
