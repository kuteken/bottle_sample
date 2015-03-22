from bottle import route, run

@route('/')
@route('/hello')
def hello():
  return "Hello World"

run(host='localhost', port=8000, debug=True)
