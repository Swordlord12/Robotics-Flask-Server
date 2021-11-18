from flask import Flask, render_template
from flask import Flask, flash, request, redirect, url_for, abort

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/journal')
def journal():
    return render_template("journal.html")

@app.route('/pictures')
def pictures():
    return render_template("pictures.html")

if __name__ == '__main__':
    app.run(debug=True)