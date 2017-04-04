from flask import Flask, render_template, send_from_directory, request
from settings import getDatabaseString
import os
import time
import psycopg2

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

def genFilename(s):
    arr_s = s.split('.')
    t = time.strftime("%d-%m-%Yh%Hm%Ms%S", time.localtime())
    return arr_s[0] + t + '.' + arr_s[1]

def createDBTable():
    try:
        conn = psycopg2.connect(getDatabaseString())
        cur = conn.cursor()
        sql_command = """
            CREATE TABLE picture (
                timestamp TIMESTAMP PRIMARY KEY DEFAULT CURRENT_TIMESTAMP,
                pic VARCHAR(150));"""
        cur.execute(sql_command)
        conn.commit()
        r = 'success'
    except:
        r = "error happens"
    return r

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        file = request.files['file']
        #Generate new filename
        file.filename = genFilename(file.filename)
        if file:
            #Save file to server
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
        file_url = request.url + 'uploads/' + file.filename
        #Insert file url into the database
        conn = psycopg2.connect(getDatabaseString())
        cur = conn.cursor()
        query = "INSERT INTO picture (pic) VALUES ('{}')"
        query = query.format(file.filename)
        print query
        cur.execute(query)
        conn.commit()
        #Render on the page
        return 'Your pic path is:  ' + file_url
    else:
        return 'Invalid'


if __name__ == "__main__":
    app.run(debug=True)
