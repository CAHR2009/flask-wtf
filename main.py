import flask
from flask import render_template


app = flask.Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route("/<title>")
def mars(title):
    return render_template('base.html', title=title)


if __name__ == '__main__':
    app.run(port=8080, host="127.0.0.1")