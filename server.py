from flask import Flask

server_port = 8000
app = Flask(__name__)

@app.route('/login')
def login():
    return 'Hello!'

@app.route('/login/<user>')
def loginuser(user):
    return 'Hello, ' + user + '!'

@app.route('/process/<n>')
def process(n):
    factorial = 1
    for i in range(1, int(n)+1):
        factorial *= i
    return 'Factorial of ' + n + " = " + str(factorial)

@app.route('/logout')
def logout():
  return 'Bye!'

@app.route('/')
def index():
  return 'Index'

@app.route('/test')
def test():
  return 'Test'

if __name__ == "__main__":
    app.run('0.0.0.0',port=server_port)