from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<center><h1 style="background-color: silver">Hello World!</h1></center>'

@app.route('/home')
def Display():
    return render_template("home.html")

@app.route('/login')
def display():
    return render_template("login.html")

@app.route('/signup')
def sign_up():
    return render_template("signup.html")

@app.route('/footer')
def footer():
    return render_template("footer.html")

if __name__ == '__main__':
    app.run(debug=True)
