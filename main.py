from flask import Flask
import random

app = Flask(__name__)

facts = ['Несобранность, чувство повышенной тревожности, беспомощность и иные негативные переживания – все это происходит с нами во время использования гаджетов', 'Сильнее всего такого рода переживаниям подвержены дети и подростки', 'подобная зависимость может стать губительной для психического здоровья']
@app.route("/")
def hello_world():
    return '<a href="/random_fact">Посмотреть случайный факт!</a>'

@app.route("/random_fact")
def random_fact():
    return f'<p>{random.choice(facts)}</p>'

@app.route("hide_web")
def hide_d():
    return '<a href="/random_fact">Скрытая страничка!!</a>'

app.run(debug=True)
