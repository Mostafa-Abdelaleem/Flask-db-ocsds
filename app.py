import os
import ibm_db
from flask import Flask
app = Flask(__name__)


conn=ibm_db.connect( os.environ['dbcred'], "", "")


@app.route("/")
def main():
    return "Flask app is online!"


@app.route('/db2')
def access_db():
    
    sql = ' select * from NAMES '
    stmt = ibm_db.exec_immediate(conn,sql)
    dictionary = ibm_db.fetch_both(stmt)
    return dictionary['NAME']


@app.route('/abdelaleem')
def abd_db():

    sql = ''' UPDATE Names SET  name = 'abdelaleem' WHERE id='1'; '''
    ibm_db.exec_immediate(conn,sql)
    return "name is now abdelelaeem"

@app.route('/mostafa')
def mos_db():

    sql = ''' UPDATE Names SET  name = 'mostafa' WHERE id='1'; '''
    ibm_db.exec_immediate(conn,sql)
    return "name is now mostafa"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
