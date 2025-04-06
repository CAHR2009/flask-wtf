import flask
from flask import render_template, url_for


app = flask.Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route("/list_prof/<list_type>")
def profession(list_type):
    return render_template('profession.html', list_type=list_type)


if __name__ == '__main__':
    app.run(port=8080, host="127.0.0.1")