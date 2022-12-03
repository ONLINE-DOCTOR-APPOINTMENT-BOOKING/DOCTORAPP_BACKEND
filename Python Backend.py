from flask import Flask, request, jsonify,render_template
import mysql.connector as con

mydb = con.connect(host="localhost", user='root', passwd='pc-1430')

app=Flask(__name__,
            static_url_path='',
            static_folder='web/static',
            template_folder='web/templates')

@app.route('/pyc/patientdata/', methods = ['GET','POST'])
def insert():
    print('In Controller')
    content = request.json
    print(content)
    Name=request.json['name']
    Number=request.json['number']
    EmailID=request.json['email']
    AppointmentDate=request.json['date']
    print(Name)
    print(Number)
    print(EmailID)
    print(AppointmentDate)

    cursor = mydb.cursor()
    query = "insert into patients.patientdata values('"+Name+"',"+Number+",'"+EmailID+"','"+AppointmentDate+"')";
    print(query)
    cursor.execute(query)
    mydb.commit()

    return jsonify(str("succesfully inserted your data"))

if __name__ == '__main__':
        print('Running Flask Server/Online...')
        app.run(port=5001)