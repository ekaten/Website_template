from flask import Flask, render_template, redirect, url_for, request
import datetime as dt


# DECLARATIONS
now = dt.datetime.now()
year = now.year


# APP CONFIGURATION
app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'sdjflksjdlkgjslkdjflksjdflksdm lxkcnvksdjfsd'


# ROUTES

@app.route('/', methods=["GET"])
def index():
    return render_template('index.html', year=year)


@app.route('/template', methods=["GET", "POST"])
def template():
    return render_template('template.html', year=year)


# RUN APP
if __name__ == '__main__':
    app.run(port=7000)