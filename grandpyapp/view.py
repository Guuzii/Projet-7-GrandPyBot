#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Module that handle the routing of the app.
"""

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
    """
        Get the question from the request, try to parse it and request the APIs.

        Returns:
            - (dict): a dictionary tha contains datas depending from the question of the user
    """
    user_question = request.form['question']

    if (user_question.strip()):
        parsed_question = Parser().parseUserQuestion(user_question)

        if (parsed_question.strip()):
            adress = GoogleApi().getPlaceCoordinnate(parsed_question)

            if (adress):
                # Uncomment for debug
                # return {
                #     'texte': 'parsed_question = ' +  parsed_question + '  ||  request response = ' + str(adress)
                # }

                return {
                    'adress': adress['adress'],
                    'texte': WikiApi().getDataFromPlace(adress['latitude'], adress['longitude']),
                    'map_query': parsed_question
                }        
            else:
                return {
                    'texte': 'Je n\'ai rien trouvé par rapport à votre question'
                }
        else:
            return {
                'texte': 'Je n\'ai pas saisie la question...'
            }
    else:
        return {
                'texte': 'Je n\'ai pas saisie la question...'
            }


def getGrandPyGreating():
    """
        Get a random message from GRANDPY_GREATINGS in config and return it.

        Returns:
            - (str): the rand message picked
    """
    greating_index = randint(0, len(config.GRANDPY_GREATINGS) - 1)
    return config.GRANDPY_GREATINGS[greating_index]

if __name__ == "__main__":
    app.run()