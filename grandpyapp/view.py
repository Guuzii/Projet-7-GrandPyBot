from random import randint
# import json
# import requests
# import googlemaps

from flask import Flask, render_template, request, config
import config

from .apis import GoogleApi, WikiApi
from .parser import Parser

app = Flask(__name__)
app.config.from_object('config')

@app.route('/')
@app.route('/index/')
def index():
    grandPy_hello = getGrandPyGreating()
    return render_template('base.html', grandPy_hello=grandPy_hello)


@app.route('/api', methods=['POST'])
def api():
    # Get user question from the post request
    user_question = request.form['question']

    parsed_question = Parser(user_question).parseUserQuestion()
    googleApi = GoogleApi(parsed_question)

    adress_coordinate = googleApi.getPlaceCoordinnate()

    if (adress_coordinate):
        wikiApi = WikiApi(adress_coordinate['latitude'], adress_coordinate['longitude'])

        return {
            'texte': wikiApi.getDataFromPlace(),
            'map_query': parsed_question
        }        
    else:
        return ('Je n\'ai pas saisie la question...')


def getGrandPyGreating():
    greating_index = randint(0, len(config.GRANDPY_GREATINGS) - 1)
    return config.GRANDPY_GREATINGS[greating_index]

# gmaps = googlemaps.Client(key=config.GOOGLE_API_KEY)

# @app.route('/api', methods=['POST'])
# def api():
#     # Get user question from the post request
#     user_question = request.form['question']

#     adress_coordinate = getPlaceCoordinnate(user_question)

#     if (adress_coordinate):
#         params = {
#             'action': 'query',
#             'prop': 'extracts',
#             'exintro': 'true',
#             'explaintext': 'true',
#             'generator': 'geosearch',
#             'ggsradius': 500,
#             'ggslimit': 1,
#             'ggscoord': adress_coordinate['latitude'] + '|' + adress_coordinate['longitude'],
#             'format': 'json'
#         }

#         res = requests.get(url=config.WIKIPEDIA_API_ENDPOINT, params=params)
        
#         try:
#             wikimedia_result = res.json()['query']['pages']
#         except:
#             return ('Je n\'ai rien trouvé dans un rayon de ' + str(params['ggsradius']) + ' mètres.')

#         page_id = list(wikimedia_result)[0]

#         return ('Savais-tu que ' + wikimedia_result[page_id]['extract'])
#     else:
#         return ('Je n\'ai pas saisie la question...')

# def getPlaceCoordinnate(place):
#     # Places request to get coordinate (Google Maps API)
#     places_result = gmaps.places(place)

#     if (len(places_result['results']) > 0):        
#         return {
#             'latitude': str(places_result['results'][0]['geometry']['location']['lat']),
#             'longitude': str(places_result['results'][0]['geometry']['location']['lng'])
#         }
#     else:
#         return None

if __name__ == "__main__":
    app.run()