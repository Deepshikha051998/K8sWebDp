from flask import Flask  #importing flask framework
from flask import render_template
import socket
import mysql.connector
import os

app = Flask(__name__)

DB_Host = os.environ.get('MYSQL_SERVICE_HOST') or "localhost" # get environment variables 
DB_Database = os.environ.get('DB_Database') or "mysql" 
DB_User = os.environ.get('DB_User') or "root"
DB_Password = os.environ.get('DB_Password') or "paswrd"
GROUP = os.environ.get('GROUP')
IMAGE_URL_PATH = os.environ.get('IMAGE_URL_PATH')
IMAGE_URL_S3 = os.environ.get('IMAGE_URL_S3')

@app.route("/")
def main():
    db_connect_result = False
    err_message = ""
    try:
        mysql.connector.connect(host=DB_Host, database=DB_Database, user=DB_User, password=DB_Password) # sets up a connection
        color = '#39b54b'
        db_connect_result = True
    except Exception as e:
        color = '#ff3f3f'
        err_message = str(e)

    return render_template('hello.html', debug="Environment Variables: DB_Host=" + (os.environ.get('DB_Host') or "Not Set") + "; DB_Database=" + (os.environ.get('DB_Database')  or "Not Set") + "; DB_User=" + (os.environ.get('DB_User')  or "Not Set") + "; DB_Password=" + (os.environ.get('DB_Password')  or "Not Set") + "; " + err_message, db_connect_result=db_connect_result, name=socket.gethostname(), color=color)

@app.route("/debug")
def debug():
    color = '#2196f3'
    return render_template('hello.html', debug="Environment Variables: DB_Host=" + (os.environ.get('DB_Host') or "Not Set") + "; DB_Database=" + (os.environ.get('DB_Database')  or "Not Set") + "; DB_User=" + (os.environ.get('DB_User')  or "Not Set") + "; DB_Password=" + (os.environ.get('DB_Password')  or "Not Set"), color=color)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=81)



















