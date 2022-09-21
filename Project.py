from flask import Flask, render_template, request, redirect, send_from_directory
import pyodbc as odbc
import os
import googlemaps


app = Flask(__name__,template_folder='templates')


connection_string = (
    r'Driver=ODBC Driver 17 for SQL Server;'
    r'Server=tcp:wardp.database.windows.net,1433;'
    r'Database=project;'
    r'UID=ward;'
    r'PWD=Wa246810;'
    r'MARS_Connection=yes;'
    r'APP=yourapp'
    )

# connection_string=textwrap.dedent('''
#     Driver={{{driver}}};
#     Server={server};
#     Database={database};
#     Uid={username};
#     Pwd={password};
#     Encrypt=yes;
#     TrustServerCertificate=no;
#     Connection Timeout=30;
# '''.format(
#     driver=driver,
#     server=server,
#     database=database_name,
#     username=username,
#     password=password
# ))

# DRIVER_NAME = 'SQL SERVER'
# SERVER_NAME = 'WARD'
# DATABASE_NAME = 'project'
#
# connection_string = f"""
#     DRIVER={{{DRIVER_NAME}}};
#     SERVER={SERVER_NAME};
#     DATABASE={DATABASE_NAME};
#     Trust_connection=yes;
# """

currentdirectory = os.path.dirname(os.path.abspath(__file__))
# conn = sqlite3.connect('database.db')
# conn.execute('CREATE TABLE items (name TEXT, price INT)')
APP_ROOT = os.path.dirname(os.path.abspath(__file__))


@app.route('/')
def Main():
    return render_template('Main__.html')


@app.route('/Main')
def Main_():
    return render_template('Main__.html')


@app.route('/Paypal')
def Paypal():
    return render_template('Paypal.html')


@app.route('/About')
def About():
    return render_template('About.html')


########################################## Login/Sign_up #################
message_login = ''
message_signup = ''
email = ''
message_table = ''
message_vip = ''


def email__(email__):
    global email
    email = email__


@app.route('/Login', methods=['POST', 'GET'])
def Login():
    if request.method == 'POST':

        if request.form.get("login"):
            _reset_message_signup_()
            email = request.form["email"]
            conn = odbc.connect(connection_string)
            cursor = conn.cursor()
            email__(email)
            password = request.form["pswd"]
            # if check_login_email(email) == 0 or check_login(email, password) == 0:
            #     error_login()
            # else:
            #     _reset_message_login_()
            position = "SELECT D_P_A FROM Login WHERE email=? and pass=?"
            result = cursor.execute(position, (email, password,)).fetchone()
            if result[0] == 'Admin':
                return Admin()
            elif result[0] == 'Patient':
                return Patient_()
            else:
                return Doctor()
            return redirect('/Login')

        elif request.form.get("sign_up"):
            conn = odbc.connect(connection_string)
            first_name = request.form["first_name"]
            last_name = request.form["last_name"]
            email = request.form["email_"]
            password = request.form["pswd_"]
            D_P = request.form["d_p"]
            address = request.form["address_"]
            status = 'Available'
            # if check_login_email(email) == 1 or check_login(email, password) == 1:
            #     error_signup()
            # else:
            #     _Success_message_signup_()
            cursor = conn.cursor()
            if D_P == 'Doctor':
                x = '''INSERT INTO Login(first_name,last_name,email,pass,D_P_A,status,count_,address,count_o) VALUES(?,?,?,?,?,?,?,?)'''
                cursor.execute(x, (first_name, last_name, email, password, D_P, status, 0, address, 0,))
            if D_P == 'Patient':
                x = '''INSERT INTO Login(first_name,last_name,email,pass,D_P_A, address) VALUES(?,?,?,?,?,?)'''
                cursor.execute(x, (first_name, last_name, email, password, D_P, address,))
            conn.commit()
            return redirect('/Login')

    else:
        return render_template('Login_.html', message=get_message_login(), message_=get_message_signup())


def get_email():
    global email
    return email


def get_message_signup():
    global message_signup
    return message_signup


def error_signup():
    global message_signup
    message_signup = 'Invalid input'


def _Success_message_signup_():
    global message_signup
    message_signup = 'Success'


def _reset_message_signup_():
    global message_signup
    message_signup = ''


def get_message_login():
    global message_login
    return message_login


def error_login():
    global message_login
    message_login = 'Invalid input'


def _reset_message_login_():
    global message_login
    message_login = ''


# def check_login_email(email):
#     conn = odbc.connect(connection_string)
#     cursor = conn.cursor()
#     n_e = "('{0}', )".format(email)
#     print(n_e)
#     x = "SELECT email FROM Login"
#     x_ = cursor.execute(x)
#     for row in x_:
#         print(row)
#         if row == n_e:
#             return 1
#             break
#     return 0
#
#
# def check_login(email, pass_):
#     conn = odbc.connect(connection_string)
#     cursor = conn.cursor()
#     x = "SELECT pass FROM Login WHERE email = ?"
#     x_ = cursor.execute(x, (email,))
#     for row in x_:
#         if row == (pass_,):
#             return 1
#             break
#     return 0


@app.route('/upload00/<filename>')
def send_image(filename):
    return send_from_directory("Thumbnail", filename)


########################################## Admin #################
@app.route('/Admin')
def Admin():
    return render_template('Main_A.html')


########################################### Admin_orders #######################
@app.route('/View_orders')
def View_orders():
    headings = ("First Name-P", "Last Name-P", "Email-P", "Email-D", "Status")
    conn = odbc.connect(connection_string)
    cursor = conn.cursor()
    order = "SELECT first_name,last_name,email_p,email_d,status FROM Order_Doc"
    result = cursor.execute(order).fetchall()
    return render_template('Admin_View_Orders_.html', headings=headings, data=result)


########################################### Admin_Orders_Count #######################
@app.route('/Orders_Count')
def Orders_Count():
    conn = odbc.connect(connection_string)
    cursor = conn.cursor()

    emails_d = "SELECT email FROM Login WHERE D_P_A!=? AND D_P_A!=?"
    result_ = cursor.execute(emails_d, ('Admin', 'Patient',)).fetchall()

    emails_d_ = "SELECT email_d FROM Order_Doc"
    result__ = cursor.execute(emails_d_).fetchall()

    for x in result_:
        print(x[0][0])
        count = 0
        for y in result__:
            if x[0] == y[0]:
                count += 1
                # count_o_ = "SELECT count_o FROM Login WHERE email =?"
                # result___ = cursor.execute(count_o_, (x[0],)).fetchone()

                update = "UPDATE Login SET count_o = ? WHERE email =?"
                cursor.execute(update, (count, x[0],))
                conn.commit()

    headings = ("First Name-D", "Last Name-D", "Email-D", "Orders Count")
    order = "SELECT first_name,last_name,email,count_o FROM Login WHERE D_P_A!=? AND D_P_A!=?"
    result = cursor.execute(order, ('Admin', 'Patient',)).fetchall()
    return render_template('Admin_Orders_Count_.html', headings=headings, data=result)


############################################### A_New_Doctor ################################
message_ = ''


@app.route('/New_Doctor', methods=['POST', 'GET'])
def New_Doctor():
    if request.method == 'POST':

        if request.form.get("Add"):
            first_name = request.form["first_name"]
            last_name = request.form["last_name"]
            email = request.form["email"]
            password = request.form["pass"]
            address = request.form["address_"]
            Doctor = 'Doctor'
            status = 'Available'
            if first_name == '' or last_name == '' or email == '' or password == '':
                _error_()
            else:
                reset__message__()
                conn = odbc.connect(connection_string)
                cursor = conn.cursor()
                x = '''INSERT INTO Login(first_name,last_name,email,pass,D_P_A,status,count_,address,count_o) VALUES(?,?,?,?,?,?,?,?)'''
                cursor.execute(x, (first_name, last_name, email, password, Doctor, status, 0, address, 0,))
                conn.commit()
            return redirect('/New_Doctor')

        elif request.form.get("Delete"):
            first_name = request.form["first_name"]
            last_name = request.form["last_name"]
            email = request.form["email"]
            password = request.form["pass"]
            conn = odbc.connect(connection_string)
            cursor = conn.cursor()
            if first_name == '' or last_name == '' or email == '' or password == '':
                _error_()
            else:
                reset__message__()
                delete = "DELETE FROM Login WHERE first_name=? and last_name=? and email=? and pass=?"
                # get_message_delete__(name, price_s, price_m, price_l)
                cursor.execute(delete, (first_name, last_name, email, password,))
                conn.commit()

                delete_ = "DELETE FROM history WHERE first_name=? and last_name=? and email_d=?"
                # get_message_delete__(name, price_s, price_m, price_l)
                cursor.execute(delete_, (first_name, last_name, email,))
                conn.commit()

                delete__ = "DELETE FROM Order_Doc WHERE first_name=? and last_name=? and email_d=?"
                # get_message_delete__(name, price_s, price_m, price_l)
                cursor.execute(delete__, (first_name, last_name, email,))
                conn.commit()

            return redirect('/New_Doctor')

    else:
        admin = 'Admin'
        headings = ("First_Name", "Last_Name", "Email", "Password", "D/P", "Address")
        conn = odbc.connect(connection_string)
        cursor = conn.cursor()
        x = "SELECT first_name,last_name,email,pass,D_P_A,address FROM Login WHERE D_P_A!=?"
        result = cursor.execute(x, (admin,)).fetchall()
        return render_template('Admin_New_Doctor.html', headings=headings, data=result, message=_get_message_())


def _error_():
    global message_
    message_ = 'Invalid'


def reset__message__():
    global message_
    message_ = ''


def _get_message_():
    global message_
    return message_


########################################## Doctor #################
@app.route('/Doctor')
def Doctor():
    return render_template('Main_D.html')


########################################## Doctor_Profile #################
########################################## change pass doctor #################
message__ = ''


@app.route('/Doctor_P', methods=['POST', 'GET'])
def Doctor_P():
    if request.method == 'POST':

        if request.form.get("Change"):
            password = request.form["pass"]
            email_ = get_email()
            if password == '':
                _error__()
            else:
                reset__message___()
                conn = odbc.connect(connection_string)
                cursor = conn.cursor()
                update = "UPDATE Login SET pass = ? WHERE email =?"
                cursor.execute(update, (password, email_,))
                conn.commit()
            return redirect('/Doctor_P')

        # elif request.form.get("Back"):
        #     reset__message___()
        #     return Doctor()

    else:
        email_ = get_email()
        headings = ("First_Name", "Last_Name", "Email", "Password")
        conn = odbc.connect(connection_string)
        cursor = conn.cursor()
        profile = "SELECT first_name,last_name,email,pass FROM Login WHERE email=?"
        result = cursor.execute(profile, (email_,)).fetchall()
        return render_template('Doctor_P_.html', headings=headings, data=result, message=_get_message___())


def _error__():
    global message__
    message__ = 'Invalid'


def reset__message___():
    global message__
    message__ = ''


def _get_message___():
    global message__
    return message__


########################################## change f/l name doctor #################
message___ = ''


@app.route('/Doctor_F_L', methods=['POST', 'GET'])
def Doctor_F_L():
    if request.method == 'POST':

        if request.form.get("Change"):
            first_name = request.form["first_name"]
            last_name = request.form["last_name"]
            email_ = get_email()
            if first_name == '' or last_name == '':
                _error___()
            else:
                reset__message____()
                conn = odbc.connect(connection_string)
                cursor = conn.cursor()
                update = "UPDATE Login SET first_name = ?, last_name = ? WHERE email =?"
                cursor.execute(update, (first_name, last_name, email_,))
                conn.commit()
            return redirect('/Doctor_F_L')

        # elif request.form.get("Back"):
        #     reset__message____()
        #     return Doctor()

    else:
        email_ = get_email()
        headings = ("First_Name", "Last_Name", "Email", "Password")
        conn = odbc.connect(connection_string)
        cursor = conn.cursor()
        profile = "SELECT first_name,last_name,email,pass FROM Login WHERE email=?"
        result = cursor.execute(profile, (email_,)).fetchall()
        return render_template('Doctor_F_L_.html', headings=headings, data=result, message=_get_message____())


def _error___():
    global message___
    message___ = 'Invalid'


def reset__message____():
    global message___
    message___ = ''


def _get_message____():
    global message___
    return message___

#############################################################################
#############################################################################
#############################################################################
#############################################################################
#############################################################################
########################################## Change status doctor #################
@app.route('/Change_status', methods=['POST','GET'])
def Change_status():
    if request.method == 'POST':
        if request.form.get("Change"):
            conn = odbc.connect(connection_string)
            cursor = conn.cursor()
            get_avaiable = "SELECT status FROM login WHERE email=?"
            result = cursor.execute(get_avaiable, (get_email(),)).fetchall()[0][0]
            Not_available = "Unavailable"
            Available = "Available"
            if result == "Available":
               update = "UPDATE Login SET status = ? WHERE email =?"
               cursor.execute(update, (Not_available, get_email(),))
               conn.commit()

               update_ = "UPDATE Login SET count_ = ? WHERE email =?"
               cursor.execute(update_, (0, get_email(),))
               conn.commit()
            else:
                update = "UPDATE Login SET status = ? WHERE email =?"
                cursor.execute(update, (Available, email,))
                conn.commit()

                update_ = "UPDATE Login SET count_ = ? WHERE email =?"
                cursor.execute(update_, (0, get_email(),))
                conn.commit()
            return redirect('/Change_status')

        # elif request.form.get("Back"):
        #     return Doctor()

    else:
        email_ = get_email()
        headings = ("First_Name", "Last_Name", "Email", "Status")
        conn = odbc.connect(connection_string)
        cursor = conn.cursor()
        x = "SELECT first_name,last_name,email,status FROM Login WHERE email=?"
        result = cursor.execute(x, (email_,)).fetchall()
        return render_template('Doctor_Change_Status_.html', headings=headings, data=result)



########################################## change email doctor #################
message____ = ''
first = ''
last = ''
password = ''


def get_first():
    conn = odbc.connect(connection_string)
    cursor = conn.cursor()
    first = "SELECT first_name FROM Login WHERE email=?"
    result = cursor.execute(first, (get_email(),)).fetchone()
    return result[0]


def get_last():
    conn = odbc.connect(connection_string)
    cursor = conn.cursor()
    last = "SELECT last_name FROM Login WHERE email=?"
    result = cursor.execute(last, (get_email(),)).fetchone()
    return result[0]


def get_pass():
    conn = odbc.connect(connection_string)
    cursor = conn.cursor()
    password = "SELECT pass FROM Login WHERE email=?"
    result = cursor.execute(password, (get_email(),)).fetchone()
    return result[0]


def get_d_p_a():
    conn = odbc.connect(connection_string)
    cursor = conn.cursor()
    _d_p_a_ = "SELECT D_P_A FROM Login WHERE email=?"
    result = cursor.execute(_d_p_a_, (get_email(),)).fetchone()
    return result[0]


#######################################################################
#######################################################################
#######################################################################
@app.route('/Doctor_E', methods=['POST', 'GET'])
def Doctor_E():
    if request.method == 'POST':

        if request.form.get("Change"):
            email = request.form["email"]
            old_email = get_email()
            first_name = get_first()
            last_name = get_last()
            password = get_pass()
            doctor = get_d_p_a()
            if email == '':
                _error____()
            else:
                reset__message_____()
                conn = odbc.connect(connection_string)
                cursor = conn.cursor()

                # update = "UPDATE Order_Doc SET email_d = ? WHERE email_d = ?"
                # cursor.execute(update, (email, old_email,))
                # conn.commit()

                update = "UPDATE history SET email_d = ? WHERE email_d = ?"
                cursor.execute(update, (email, old_email,))
                conn.commit()

                update_ = "UPDATE Login SET email = ? WHERE first_name =? AND last_name =? AND pass = ? AND D_P_A = ?"
                cursor.execute(update_, (email, first_name, last_name, password, doctor,))
                email__(email)
                conn.commit()
            return redirect('/Doctor_E')

        # elif request.form.get("Back"):
        #     reset__message_____()
        #     return Doctor()

    else:
        email_ = get_email()
        headings = ("First_Name", "Last_Name", "Email", "Password")
        conn = odbc.connect(connection_string)
        cursor = conn.cursor()
        profile = "SELECT first_name,last_name,email,pass FROM Login WHERE email=?"
        result = cursor.execute(profile, (email_,)).fetchall()
        return render_template('Doctor_E_.html', headings=headings, data=result, message=_get_message_____())


def _error____():
    global message____
    message____ = 'Invalid'


def reset__message_____():
    global message____
    message____ = ''


def _get_message_____():
    global message____
    return message____


# # ########################################## Doctor specialty #################
_m_essage_____ = ''


def __get__first():
    conn = odbc.connect(connection_string)
    cursor = conn.cursor()
    first = "SELECT first_name FROM Login WHERE email=?"
    result = cursor.execute(first, (get_email(),)).fetchone()
    return result[0]


def __get__last():
    conn = odbc.connect(connection_string)
    cursor = conn.cursor()
    last = "SELECT last_name FROM Login WHERE email=?"
    result = cursor.execute(last, (get_email(),)).fetchone()
    return result[0]


@app.route('/Change_Specialty', methods=['POST', 'GET'])
def Change_Specialty():
    if request.method == 'POST':
        if request.form.get("Change"):
            specialty = request.form["specialty"]
            if specialty == '':
                _____error____()
            else:
                ___reset___message_____()
                conn = odbc.connect(connection_string)
                cursor = conn.cursor()

                update = "UPDATE Login SET D_P_A = ? WHERE first_name =? AND last_name =? AND email =?"
                cursor.execute(update, (specialty, get_first(), get_last(), get_email(),))
                conn.commit()
            return redirect('/Change_Specialty')

        elif request.form.get("Back"):
            ___reset___message_____()
            return Doctor()
    else:
        headings = ("First_Name", "Last_Name", "Email", "Specialty")
        conn = odbc.connect(connection_string)
        cursor = conn.cursor()
        specialty_ = "SELECT first_name,last_name,email,D_P_A FROM Login WHERE email = ?"
        result = cursor.execute(specialty_, (get_email(),)).fetchall()
        return render_template('Doctor_Change_Specialty_.html', headings=headings, data=result,
                               message=___get__message_____())


def _____error____():
    global _m_essage_____
    _m_essage_____ = 'Invalid'


def ___reset___message_____():
    global _m_essage_____
    _m_essage_____ = ''


def ___get__message_____():
    global _m_essage_____
    return _m_essage_____


########################################## Oredr #################
message_______ = ''


def get__first_():
    conn = odbc.connect(connection_string)
    cursor = conn.cursor()
    first = "SELECT first_name FROM Login WHERE email=?"
    result = cursor.execute(first, (get_email(),)).fetchone()
    return result[0]


def get__last_():
    conn = odbc.connect(connection_string)
    cursor = conn.cursor()
    last = "SELECT last_name FROM Login WHERE email=?"
    result = cursor.execute(last, (get_email(),)).fetchone()
    return result[0]


# def get_d_p_a_():
#     conn = odbc.connect(connection_string)
#     cursor = conn.cursor()
#     _d_p_a_ = "SELECT D_P_A FROM Login WHERE email=?"
#     result = cursor.execute(_d_p_a_, (get_email(),)).fetchone()
#     return result[0]


@app.route('/Order_Doc', methods=['POST', 'GET'])
def Order_Doc():
    if request.method == 'POST':

        if request.form.get("Done"):
            first_name = request.form["first_name"]
            last_name = request.form["last_name"]
            email = request.form["email"]
            notes = request.form["note"]
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

                update__ = "UPDATE history SET status = ?, notes=? WHERE first_name =? AND last_name =? AND email_p =? AND email_d=? AND notes IS NULL"
                cursor.execute(update__, (status_, notes, get__first_(), get__last_(), email, get_email(),))
                conn.commit()

                select_ = "SELECT medical_history FROM Login WHERE email=?"
                x = cursor.execute(select_, (email,)).fetchone()[0]
                if x == None:
                    update___ = "UPDATE Login SET medical_history=? WHERE email=?"
                    cursor.execute(update___, (notes, email,))
                    conn.commit()
                else:
                    y = '{0},{1}'.format(x, notes)
                    update___ = "UPDATE Login SET medical_history=? WHERE email=?"
                    cursor.execute(update___, (y, email,))
                    conn.commit()
            return redirect('/Order_Doc')

        elif request.form.get("Approval"):
            conn = odbc.connect(connection_string)
            cursor = conn.cursor()
            first_name = request.form["first_name"]
            last_name = request.form["last_name"]
            email = request.form["email"]
            status_ = 'Approve'

            update_ = "UPDATE Order_Doc SET status = ? WHERE first_name =? AND last_name =? AND email_p =? AND status!=?"
            cursor.execute(update_, (status_, first_name, last_name, email, 'Done',))
            conn.commit()

            update__ = "UPDATE history SET status = ? WHERE first_name =? AND last_name =? AND email_p =? AND email_d=? AND notes IS NULL"
            cursor.execute(update__, (status_, get__first_(), get__last_(), email, get_email(),))
            conn.commit()

            return redirect('/Order_Doc')

        elif request.form.get("DisApproval"):
            conn = odbc.connect(connection_string)
            cursor = conn.cursor()
            first_name = request.form["first_name"]
            last_name = request.form["last_name"]
            email = request.form["email"]
            status_ = 'DisApprove'

            update_ = "UPDATE Order_Doc SET status = ? WHERE first_name =? AND last_name =? AND email_p =? AND status!=?"
            cursor.execute(update_, (status_, first_name, last_name, email, "Done",))
            conn.commit()

            update__ = "UPDATE history SET status = ? WHERE first_name =? AND last_name =? AND email_p =? AND email_d=? AND notes IS NULL"
            cursor.execute(update__, (status_, get__first_(), get__last_(), email, get_email(),))
            conn.commit()

            return redirect('/Order_Doc')

    else:
        headings = ("First_Name", "Last_Name", "Email", "Status", "Notes_P", "Medical_history")
        conn = odbc.connect(connection_string)
        cursor = conn.cursor()
        order = "SELECT first_name,last_name,email_p,status,notes FROM Order_Doc WHERE email_d = ?"
        result = cursor.execute(order, (get_email(),)).fetchall()
        present_date = []
        for r in result:
            select_ = "SELECT medical_history FROM Login WHERE email=?"
            x = cursor.execute(select_, (r[2],)).fetchone()[0]
            present_date.append((r[0],r[1],r[2],r[3],r[4],x))
        return render_template('Order_Doc_D.html', headings=headings, data=present_date, message=__get__message_____())


def ___error____():
    global message_______
    message_______ = 'Invalid'


def reset____message_____():
    global message_______
    message_______ = ''


def __get__message_____():
    global message_______
    return message_______


########################################## Patient #################
@app.route('/Patient')
def Patient_():
    return render_template('Main_P.html')


########################################## Patient_Profile #################
########################################## change pass Patient #################
__message__ = ''


@app.route('/Patient_P', methods=['POST', 'GET'])
def Patient_P():
    if request.method == 'POST':

        if request.form.get("Change"):
            password = request.form["pass"]
            email_ = get_email()
            if password == '':
                __error__()
            else:
                _reset__message___()
                conn = odbc.connect(connection_string)
                cursor = conn.cursor()
                update = "UPDATE Login SET pass = ? WHERE email =?"
                cursor.execute(update, (password, email_,))
                conn.commit()
            return redirect('/Patient_P')

        # elif request.form.get("Back"):
        #     _reset__message___()
        #     return Patient_()

    else:
        email_ = get_email()
        headings = ("First_Name", "Last_Name", "Email", "Password")
        conn = odbc.connect(connection_string)
        cursor = conn.cursor()
        profile = "SELECT first_name,last_name,email,pass FROM Login WHERE email=?"
        result = cursor.execute(profile, (email_,)).fetchall()
        return render_template('Patient_P_.html', headings=headings, data=result, message=__get_message___())


def __error__():
    global __message__
    __message__ = 'Invalid'


def _reset__message___():
    global __message__
    __message__ = ''


def __get_message___():
    global __message__
    return __message__


########################################## change f/l name Patient #################
___message___ = ''


@app.route('/Patient_F_L', methods=['POST', 'GET'])
def Patient_F_L():
    if request.method == 'POST':

        if request.form.get("Change"):
            first_name = request.form["first_name"]
            last_name = request.form["last_name"]
            email_ = get_email()
            Patient = 'Patient'
            if first_name == '' or last_name == '':
                _error___()
            else:
                reset__message____()
                conn = odbc.connect(connection_string)
                cursor = conn.cursor()
                update = "UPDATE Login SET first_name = ?, last_name = ? WHERE email =? AND D_P_A =?"
                cursor.execute(update, (first_name, last_name, email_, Patient,))
                conn.commit()

                update = "UPDATE Order_Doc SET first_name = ?, last_name = ? WHERE email_p =?"
                cursor.execute(update, (first_name, last_name, email_,))
                conn.commit()

            return redirect('/Patient_F_L')

        # elif request.form.get("Back"):
        #     reset__message____()
        #     return Patient_()

    else:
        email_ = get_email()
        headings = ("First_Name", "Last_Name", "Email", "Password")
        conn = odbc.connect(connection_string)
        cursor = conn.cursor()
        profile = "SELECT first_name,last_name,email,pass FROM Login WHERE email=?"
        result = cursor.execute(profile, (email_,)).fetchall()
        return render_template('Patient_F_L_.html', headings=headings, data=result, message=_get_message____())


def _error___():
    global ___message___
    ___message___ = 'Invalid'


def reset__message____():
    global message___
    message___ = ''


def _get_message____():
    global message___
    return message___


########################################## change email Patient #################
_____message____ = ''


def _get__first_():
    conn = odbc.connect(connection_string)
    cursor = conn.cursor()
    first = "SELECT first_name FROM Login WHERE email=?"
    result = cursor.execute(first, (get_email(),)).fetchone()
    return result[0]


def _get__last_():
    conn = odbc.connect(connection_string)
    cursor = conn.cursor()
    last = "SELECT last_name FROM Login WHERE email=?"
    result = cursor.execute(last, (get_email(),)).fetchone()
    return result[0]


def _get__pass_():
    conn = odbc.connect(connection_string)
    cursor = conn.cursor()
    password = "SELECT pass FROM Login WHERE email=?"
    result = cursor.execute(password, (get_email(),)).fetchone()
    return result[0]


@app.route('/Patient_E', methods=['POST', 'GET'])
def Patient_E():
    if request.method == 'POST':

        if request.form.get("Change"):
            email = request.form["email"]
            old_email = get_email()
            first_name = _get__first_()
            last_name = _get__last_()
            password = _get__pass_()
            Patient = 'Patient'
            if email == '':
                ____error____()
            else:
                ____reset__message_____()
                conn = odbc.connect(connection_string)
                cursor = conn.cursor()

                update = "UPDATE Order_Doc SET email_p = ? WHERE email_p = ?"
                cursor.execute(update, (email, old_email,))
                conn.commit()

                update = "UPDATE history SET email_p = ? WHERE email_p = ?"
                cursor.execute(update, (email, old_email,))
                conn.commit()

                update_ = "UPDATE Login SET email = ? WHERE first_name =? AND last_name =? AND pass = ? AND D_P_A = ?"
                cursor.execute(update_, (email, first_name, last_name, password, Patient,))
                email__(email)
                conn.commit()
            return redirect('/Patient_E')

        # elif request.form.get("Back"):
        #     ____reset__message_____()
        #     return Patient_()

    else:
        email_ = get_email()
        headings = ("First_Name", "Last_Name", "Email", "Password")
        conn = odbc.connect(connection_string)
        cursor = conn.cursor()
        profile = "SELECT first_name,last_name,email,pass FROM Login WHERE email=?"
        result = cursor.execute(profile, (email_,)).fetchall()
        return render_template('Patient_E_.html', headings=headings, data=result, message=_____get_message_____())


def ____error____():
    global _____message____
    _____message____ = 'Invalid'


def ____reset__message_____():
    global _____message____
    _____message____ = ''


def _____get_message_____():
    global _____message____
    return _____message____


########################################## Order_Doctor #################
message_____ = ''


def get_first_():
    conn = odbc.connect(connection_string)
    cursor = conn.cursor()
    first = "SELECT first_name FROM Login WHERE email=?"
    result = cursor.execute(first, (get_email(),)).fetchone()
    return result[0]


def get_last_():
    conn = odbc.connect(connection_string)
    cursor = conn.cursor()
    last = "SELECT last_name FROM Login WHERE email=?"
    result = cursor.execute(last, (get_email(),)).fetchone()
    return result[0]


def get_d_p_a__(first, last, email):
    conn = odbc.connect(connection_string)
    cursor = conn.cursor()
    _d_p_a_ = "SELECT D_P_A FROM Login WHERE first_name =? AND last_name =? AND email =?"
    result = cursor.execute(_d_p_a_, (first, last, email,)).fetchone()
    return result[0]


##################################################################################
##################################################################################
# ##################################################################################
@app.route('/Order_Doctor', methods=['POST', 'GET'])
def Order_Doctor():
    if request.method == 'POST':

        if request.form.get("Order"):
            first_name = request.form["first_name"]
            last_name = request.form["last_name"]
            email = request.form["email"]
            notes = request.form["note"]
            doctor = get_d_p_a__(first_name, last_name, email)
            status = 'Unavailable'
            _status_ = 'Available'
            status_ = 'Waiting to approve'
            if first_name == '' or last_name == '' or email == '':
                __error____()
            else:
                reset___message_____()
                conn = odbc.connect(connection_string)
                cursor = conn.cursor()

                if check_count_(first_name, last_name, email) < 11:
                    update = "UPDATE Login SET status = ?, count_ = ? WHERE first_name =? AND last_name =? AND email =? AND D_P_A =?"
                    cursor.execute(update, (_status_, check_count_(first_name, last_name, email)+1, first_name, last_name, email, doctor,))
                    conn.commit()
                else:
                    update = "UPDATE Login SET status = ?, count_ = ? WHERE first_name =? AND last_name =? AND email =? AND D_P_A =?"
                    cursor.execute(update, (status, 0, first_name, last_name, email, doctor,))
                    conn.commit()

                x = '''INSERT INTO Order_Doc(first_name,last_name,email_p,status,email_d,notes) VALUES(?,?,?,?,?,?)'''
                cursor.execute(x, (get_first_(), get_last_(), get_email(), status_, email, notes,))
                conn.commit()

                y = '''INSERT INTO history(first_name,last_name,email_p,status,email_d) VALUES(?,?,?,?,?)'''
                cursor.execute(y, (first_name, last_name, get_email(), status_, email,))
                conn.commit()
            return redirect('/Order_Doctor')

        # elif request.form.get("Back"):
        #     reset__message_____()
        #     return Patient_()

    else:
        Admin = "Admin"
        Patient = "Patient"
        status = 'Available'
        headings = ("First_Name", "Last_Name", "Email", "Doctor", "Distance from you")
        conn = odbc.connect(connection_string)
        cursor = conn.cursor()

        address_of_patient="SELECT address FROM Login WHERE email =?"
        result_patient_address = cursor.execute(address_of_patient, (get_email(),)).fetchall()[0][0]
        addresses_of_doctors = "SELECT first_name,last_name,email,D_P_A,address FROM Login WHERE D_P_A !=? AND D_P_A !=? AND status =?"
        result = cursor.execute(addresses_of_doctors, (Admin,Patient,status,)).fetchall()

        # # find distance
        API_KEY = 'your API'
        gmaps = googlemaps.Client(key=API_KEY)
        # map_clinet = googlemaps.Client(API_KEY)
        def calc_distance_of_two_points(origin, destination):
            distance =gmaps.distance_matrix(origin, destination)['rows'][0]['elements'][0]
            return [distance['distance']['text'], distance['duration']['text']]
        present_date = []
        for doctor in result: #calculate distance of each doctor to patient
            distance = calc_distance_of_two_points(result_patient_address, doctor[4])
            present_date.append((doctor[0],doctor[1],doctor[2],doctor[3],distance))

        # order = "SELECT first_name,last_name,email,D_P_A FROM Login WHERE status=?"
        # result_ = cursor.execute(order, (status,)).fetchall()
        return render_template('Patient_Order_Doctor.html', headings=headings, data=present_date, message=_get__message_____())


def __error____():
    global message_____
    message_____ = 'Invalid'


def reset___message_____():
    global message_____
    message_____ = ''


def _get__message_____():
    global message_____
    return message_____


def check_count_(first_name, last_name, email):
    conn = odbc.connect(connection_string)
    cursor = conn.cursor()
    count_ = "SELECT count_ FROM Login WHERE first_name =? AND last_name =? AND email =?"
    result = cursor.execute(count_, (first_name, last_name, email,)).fetchone()
    return result[0]


########################################## Oredrs_History #################
@app.route('/Orders_History')
def Orders_History():
    headings = ("First_Name", "Last_Name", "status", "Doctor Note")
    conn = odbc.connect(connection_string)
    cursor = conn.cursor()
    order = "SELECT first_name,last_name,status,notes FROM history WHERE email_p =?"
    result = cursor.execute(order, (get_email(),)).fetchall()
    return render_template('Patient_Orders_History.html', headings=headings, data=result)


########################################## Cancel_Order #################
@app.route('/Cancel_Order', methods=['POST', 'GET'])
def Cancel_Order():
    if request.method == 'POST':

        if request.form.get("Delete"):
            first_name = request.form["first_name"]
            last_name = request.form["last_name"]
            email = request.form["email"]
            conn = odbc.connect(connection_string)
            cursor = conn.cursor()

            delete = "DELETE FROM history WHERE first_name=? AND last_name=? AND email_d=? AND status=? AND email_p=?"
            cursor.execute(delete, (first_name, last_name, email, 'Waiting to approve', get_email(),))
            conn.commit()

            delete_ = "DELETE FROM Order_Doc WHERE first_name=? AND last_name=? AND email_p=? AND email_d=? AND status=?"
            cursor.execute(delete_, (get_first_(), get_last(), get_email(), email, 'Waiting to approve',))
            conn.commit()

            update = "UPDATE Login SET count_ = ? WHERE first_name =? AND last_name =? AND email =?"
            cursor.execute(update, (check_count_(first_name, last_name, email)-1, first_name, last_name, email,))
            conn.commit()

            return redirect('/Cancel_Order')

    else:
        headings = ("First Name", "Last Name", "Email-D", "Status")
        conn = odbc.connect(connection_string)
        cursor = conn.cursor()
        order = "SELECT first_name,last_name,email_d,status FROM history WHERE email_p =? AND status=?"
        result = cursor.execute(order, (get_email(), 'Waiting to approve',)).fetchall()
        return render_template('Patient_Cancel_Order.html', headings=headings, data=result)


if __name__ == '__main__':
    app.debug = True
    app.env = "development"
    app.run(host="localhost", port=5000)
