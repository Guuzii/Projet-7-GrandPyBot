from random import randint

from flask import Flask, render_template, request, config
from flask_cors import CORS
import config

from .classes.apis import GoogleApi, WikiApi
from .classes.parser import Parser

app = Flask(__name__)
app.config.from_object('config')

CORS(app)

@app.route('/')
@app.route('/index/')
def index():
    grandPy_hello = getGrandPyGreating()
    return render_template('base.html', grandPy_hello=grandPy_hello)


@app.route('/api', methods=['POST'])
def api():
    user_question = request.form['question']

    if (user_question.strip()):
        parsed_question = Parser().parseUserQuestion(user_question)

        if (parsed_question.strip()):
            adress = GoogleApi().getPlaceCoordinnate(parsed_question)

            print(adress)

            if (adress):
                return {
                    'texte': 'parsed_question = ' +  parsed_question + 'request response = ' + str(adress)
                }
                # return {
                #     'adress': adress['adress'],
                #     'texte': WikiApi().getDataFromPlace(adress['latitude'], adress['longitude']),
                #     'map_query': parsed_question
                # }        
            else:
                return {
                    'texte': 'GoogleApi response == null'
                }
        else:
            return {
                'texte': 'Parsed question is empty'
            }
    else:
        return {
                'texte': 'Je n\'ai pas saisie la question...'
            }


def getGrandPyGreating():
    greating_index = randint(0, len(config.GRANDPY_GREATINGS) - 1)
    return config.GRANDPY_GREATINGS[greating_index]

if __name__ == "__main__":
    app.run()