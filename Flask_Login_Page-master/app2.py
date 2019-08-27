from flask import Flask, jsonify, request, render_template, send_from_directory, redirect
import mysql.connector

db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Khakim@17',
    database='school'
)
app = Flask(__name__)

@app.route('/file/<path:path>')
def aksesFile(path):
    return send_from_directory ('file', path)

@app.route('/', methods = ['GET'])
def landing_page():
    return render_template ('app_form2.html')

@app.route('/signup', methods=['POST'])
def srudents():
    body = request.form
    used = db.cursor()
    used.execute('select * from user_data')
    data = used.fetchall()
    email_temp = []
    for item in data:
        email_temp.append(item[0])
    for item in data:
        if body['email'] not in email_temp:
            used = db.cursor()
            qry = 'insert into user_data (email,pass) values (%s, %s)'
            val = (body['email'], body['pass'])
            used.execute(qry, val)
            db.commit()
            return render_template ('message.html', data = 'sign up success!')
        else:
            return render_template ('message.html', data = 'email already exist!')

@app.route('/signin', methods=['POST'])
def srudentss():
    body = request.form
    used = db.cursor()
    used.execute('select * from user_data')
    data = used.fetchall()
    email_temp = []
    for item in data:
        email_temp.append(item[0])
    for item in data:
        if body['email'] not in email_temp:
            return render_template ('message.html', data = 'email are not recognize!')
        else:
            if item[0] == body['email']:
                if item[1] == body['pass']:
                    return render_template ('message.html', data = 'Sign in success') 
                else:
                    return render_template ('message.html', data = 'Wrong password!') 

#get selected data ===============================================
@app.route('/students/<string:nis>')
def studdent(nis):
    if nis.isdigit() and int(nis) > 0:
        used = db.cursor()
        used.execute('describe students')
        hasil = used.fetchall()
        namaKolom = []
        for i in hasil:
            namaKolom.append(i[0])
        qry = 'select * from students where nis = %s'
        nis = (nis,)
        used.execute(qry, nis)
        hasil = used.fetchall()
        data=[]
        for i in hasil:
            x = {
                namaKolom[0]: i[0],
                namaKolom[1]: i[1],
                namaKolom[2]: i[2]
            }
            data.append(x)
        return jsonify (data)
    else:
        return jsonify()    

if __name__ == '__main__':
    app.run(
        debug=True
    )