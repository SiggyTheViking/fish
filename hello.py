#!/usr/bin/python3

from bottle import route, run, default_app
import sys
import os
import psycopg2 as pg

conn = pg.connect('dbname=pvr user=darin password=fjrk99cl')

@route('/api/hello')
def hello():
    return sys.version#"Hello World!"

@route('/api/time')
def time():
    cur = conn.cursor()
    cur.execute('select current_timestamp')
    dict = {'now':cur.fetchone()[0].strftime('%m/%d/%y %H:%M:%S')}
    cur.close()
    return dict
 
@route('/api/pond')
def pond():
    return {'foo':'bar'}

if __name__ == "__main__":
    # Interactive mode
    run(host='localhost', port=8080)
else:
    # Mod WSGI launch
    os.chdir(os.path.dirname(__file__))
    application = default_app()
