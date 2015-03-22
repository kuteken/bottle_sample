from bottle import route, run, template

@route('/')
@route('/hello/<name>')
def greet(name='Stranger'):
  return template('Hello {{name}}', name=name)

@route('/user/<id:int>')
def userPage(id):
  return template('This is user: {{id}} page.', id=id)

run(host='localhost', port=8000, debug=True, reloader=True)
