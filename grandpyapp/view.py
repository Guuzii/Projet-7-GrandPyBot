from random import randint

from flask import Flask, render_template, request, config
import config

from .classes.apis import GoogleApi, WikiApi
from .classes.parser import Parser

app = Flask(__name__)
app.config.from_object('config')

@app.route('/')
@app.route('/index/')
def index():
    grandPy_hello = getGrandPyGreating()
    return render_template('base.html', grandPy_hello=grandPy_hello)


@app.route('/api', methods=['POST'])
def api():
    user_question = request.form['question']

    parsed_question = Parser(user_question).parseUserQuestion()
    googleApi = GoogleApi()

    adress_coordinate = googleApi.getPlaceCoordinnate(parsed_question)

    if (adress_coordinate):
        wikiApi = WikiApi()

        return {
            'texte': wikiApi.getDataFromPlace(adress_coordinate['latitude'], adress_coordinate['longitude']),
            'map_query': parsed_question
        }        
    else:
        return ('Je n\'ai pas saisie la question...')


def getGrandPyGreating():
    greating_index = randint(0, len(config.GRANDPY_GREATINGS) - 1)
    return config.GRANDPY_GREATINGS[greating_index]

if __name__ == "__main__":
    app.run()