import flask
from flask import render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField

app = flask.Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
form_values = []

class LoginForm(FlaskForm):
    sername = StringField('Фамилия')
    name = StringField('Имя')
    educate = StringField('Образование')
    prof = StringField('Профессия')
    motiv = StringField('Мотивация')
    ready = BooleanField('Готовы остаться на Марсе?')
    submit = SubmitField('Отправить')

@app.route('/auto_answer', methods=['GET', 'POST'])
def login():
    global form_values
    form = LoginForm()
    if form.validate_on_submit():
        form_values = request.form.items()
    return render_template('auto_answer.html', title='Авторизация', form=form)

@app.route('/answer', methods=['GET', 'POST'])
def viviod():
    global form_values
    form_values = list(form_values)[:-1]
    if form_values[-1][1] == 'y':
        form_values[-1] = (form_values[-1][0], 'True')
    else:
        form_values[-1] = (form_values[-1][0], 'False')
    return render_template('answer.html', title='Анкета', form=form_values)

if __name__ == '__main__':
    app.run(port=8080, host="127.0.0.1")