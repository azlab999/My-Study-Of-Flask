from flask import Flask, render_template

app = Flask(__name__)                           # Generate a Flask instance

@app.route('/')                                 # Indicate the URL for index()

def index() :                                   # Rend app1.html
    return render_template('app1.html')

if __name__ == '__main__' :
    app.run()