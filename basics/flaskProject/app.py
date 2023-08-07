from flask import Flask, render_template, redirect, url_for, request, session

app = Flask(__name__)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/')
def home():  # put application's code here
    if 'username' in session:
        username = session['username']
        return f'<p>Bienvenido {username}</p>'
    return '<p>El usuario no esta loggeado</p>'


@app.route('/hello/<username>')
def hello(username):
    return 'Hello, World ' + username


@app.route('/edad/<int:edad>')
def mostrar_edad(edad):
    return 'Tu edad es ' + str(edad)


@app.route('/mostrar/<nombre>', methods=['GET', 'POST'])
def mostrar_nombre(nombre):
    return render_template('mostrar.html', nombre_parametro=nombre)


@app.errorhandler(404)
def pagina_error(error):
    return render_template('404.html', error=error), 404


@app.route('/api/devuelve/<name>')
def response_data(name):
    data = {'name': name, 'metodo': request.method}
    return data

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        session['username'] = username
        return redirect(url_for('home'))

    return render_template('login.html')

@app.route('/salir')
def salir():
    if 'username' in session:
        session.pop('username')
        return redirect(url_for('login'))
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run()
