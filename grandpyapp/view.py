from random import randint
import json
import requests
import googlemaps

from flask import Flask, render_template, request, config
import config

app = Flask(__name__)

app.config.from_object('config')

gmaps = googlemaps.Client(key=config.GOOGLE_API_KEY)

@app.route('/')
@app.route('/index/')
def index():
    grandPy_hello = getGrandPyGreating()
    return render_template('base.html', grandPy_hello=grandPy_hello)

@app.route('/api', methods=['POST'])
def api():
    # call parser
    # call APIs (google, wikipedia)

    # Get user question from the post request
    user_question = request.form['question']
    # print('question envoyé par l\'utilisateur : {question}'.format(question=user_question))

    adress_coordinate = getAdressCoordinnate(user_question)

    if (adress_coordinate):

        # geosearch request to get revisions content
        # https://fr.wikipedia.org/w/api.php?action=query&prop=extracts&exintro=true&explaintext=true&generator=geosearch&ggsradius=500&ggslimit=1&ggscoord=48.856614%7C2.3522219&format=json
        
        params = {
            'action': 'query',
            'prop': 'extracts',
            'exintro': 'true',
            'explaintext': 'true',
            'generator': 'geosearch',
            'ggsradius': 500,
            'ggslimit': 1,
            'ggscoord': adress_coordinate['latitude'] + '|' + adress_coordinate['longitude'],
            'format': 'json'
        }

        res = requests.get(url=config.WIKIPEDIA_API_ENDPOINT, params=params)
        
        try:
            wikimedia_result = res.json()['query']['pages']
        except:
            return ('Je n\'ai rien trouvé dans un rayon de ' + str(params['ggsradius']) + ' mètres.')

        page_id = list(wikimedia_result)[0]

        return (wikimedia_result[page_id]['extract'])

        # return ('Coordonnées géographique de ' + user_question + ' : Latitude : ' + str(adress_coordinate['latitude']) + ', longitude : ' + str(adress_coordinate['longitude']))
    else:
        return ('Je n\'ai pas saisie la question...')


def getGrandPyGreating():
    greating_index = randint(0, len(config.grandPy_greatings) - 1)
    return config.grandPy_greatings[greating_index]


def getAdressCoordinnate(adress):
    # Geocode request to get coordinate (Google Maps API)
    geocode_result = gmaps.geocode(adress)

    if (len(geocode_result) > 0):        
        return {
            'latitude': str(geocode_result[0]['geometry']['location']['lat']),
            'longitude': str(geocode_result[0]['geometry']['location']['lng'])
        }
    else:
        return None

if __name__ == "__main__":
    app.run()