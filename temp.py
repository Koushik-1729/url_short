from flask import*
app= Flask(__name__)
import sqlite3
import random
from datetime import datetime

# Generate a unique seed combining the current time and a counter
current_time = datetime.now()
counter = 0
seed = int(current_time.strftime('%Y%m%d%H%M%S')) * 100000 + counter

# Set the random seed
random.seed(seed)

# Generate a 6-digit random number
random_number = random.randint(100000, 999999)

conn = sqlite3.connect('urlshort.db',check_same_thread=False)

def do_basic_ops():
    cur = conn.cursor()
    sql = '''
    CREATE TABLE IF NOT EXISTS urlshort(
    urlkey text,
    returnurl text
    )
    '''
    cur.execute(sql)
    conn.commit()

@app.route('/')
def index():
    return {'I am':'alive'}

@app.route('/insert',methods=['POST','GET'])
def insert():
    returnpath = request.args.get('url')
    cur = conn.cursor()
    sql =f''' 
    INSERT INTO urlshort(urlkey,returnurl) values('{random_number}', '{returnpath}')
    '''
    cur.execute(sql)
    conn.commit()
    return {'message':f'Successfully inserted key {random_number}'}
    
    
@app.route('/<path>')
def return_path(path):
    cur = conn.cursor()
    cur.execute(f"select * from urlshort where urlkey = '{path}' ")
    returnurl = cur.fetchone()[1]
    
    return redirect(returnurl)
    



if __name__ == '__main__':
    do_basic_ops()
    app.run(debug=True)