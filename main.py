from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/edit')
def edit():
    return render_template('edit.html')

@app.route('/error')
def error():
    return render_template('error.html')

@app.route('/home')
def dummy():
    return render_template('dummy.html')

@app.route('/laptopdescription')
def laptopdescription():
    return render_template('laptopdescription.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/smartwatch')
def smartwatch():
    return render_template('smartwatch.html')

@app.route('/sneakers')
def sneakers():
    return render_template('sneakers.html')

@app.route('/payment')
def payment():
    return render_template('payment.html')

@app.route('/brush')
def brush():
    return render_template('brush.html')

@app.route('/kettle')
def kettle():
    return render_template('kettle.html')

@app.route('/hairdyer')
def hairdyer():
    return render_template('hairdyer.html')

@app.route('/bottle')
def bottle():
    return render_template('bottle.html')

@app.route('/layout')
def layout():
    return render_template('layout.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/logout')
def logout():
    return render_template('logout.html')

if __name__ == '__main__':
    app.run(debug=True, port=8080)



