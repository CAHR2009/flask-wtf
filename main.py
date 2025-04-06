import flask
from flask import render_template, url_for


app = flask.Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route("/<title>")
def mars(title):
    return render_template('base.html', title=title)

@app.route("/training/<prof>")
def profession(prof):
    link_eng = url_for("static", filename="img/eng.jpg")
    link_sient = url_for("static", filename="img/sient.jpg")
    return render_template('profession.html', prof=prof, link_eng=link_eng, link_sient=link_sient)


if __name__ == '__main__':
    app.run(port=8080, host="127.0.0.1")