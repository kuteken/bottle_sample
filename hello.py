from bottle import route, run, template, static_file, error, abort, redirect

@route('/')
@route('/hello/<name>')
def greet(name='Stranger'):
  return template('Hello {{name}}', name=name)

@route('/user/<id:int>')
@route('/user/<id:re:[a-c]+>')
def userPage(id):
  return template('This is user: {{id}} page.', id=id)

@route('/static/<filepath>')
def static(filepath):
  return static_file(filepath, root='static/')

@error(404)
def error404(error):
  print error
  return 'Sorry, Nothing here'

@route('/denied')
def restricted():
  abort(401, 'Sorry, access denied')

@route('/redirect')
def redirecter():
  redirect("http://example.com/")

run(host='localhost', port=8000, debug=True, reloader=True)
