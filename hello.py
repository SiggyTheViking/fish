#!/usr/bin/python

from bottle import route, request, run, default_app
import sys
import os
#import psycopg2 as pg
import pond as p

#conn = pg.connect('dbname=pvr user=darin password=fjrk99cl')
#!/usr/bin/python3

#touch
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
def gen_pond():
    w = int(request.query.width)
    h = int(request.query.height)
    d = int(request.query.depth)
    set_depth_func = p.set_depth_factory(w,h,d)
    pnd = p.make_a_pond(w,h,set_depth_func)
    return {'pond':pnd,'width':w,'height':h,'depth':d}

def pond():
    return {'foo':'bar'}

if __name__ == "__main__":
    # Interactive mode
    run(host='localhost', port=8080)
else:
    # Mod WSGI launch
    os.chdir(os.path.dirname(__file__))
    application = default_app()
