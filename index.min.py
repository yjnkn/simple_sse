from bottle import run, route, response, view
import time
import os

@route('/')
@view("index.min.html")
def index():
    return dict()

@route('/sse')
def sse():
    count = 0
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Content_Type']  = 'text/event-stream'
    while (True):
        yield 'data:"hello SSE"\n\n'
        time.sleep(1)

# run(host="localhost", port=8080, debug=True, reloader=True)
myport = os.getenv("PORT", 8080)
myaddr = os.getenv("IP", "localhost")
run(host=myaddr, port=myport, debug=True, reloader=True)
