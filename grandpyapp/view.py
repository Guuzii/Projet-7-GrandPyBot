from random import randint
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
    # appel parser
    # appel APIs (google, wikipedia)

    # Get user question from the post request
    user_question = request.form['question']
    # print('question envoyé par l\'utilisateur : {question}'.format(question=user_question))

    # Geocode request to get coordinate (Google Maps API)
    adress_coordinate = getAdressCoordinnate(user_question)

    if (adress_coordinate):
        return ('Coordonnées géographique de ' + user_question + ' : Latitude : ' + str(adress_coordinate['latitude']) + ', longitude : ' + str(adress_coordinate['longitude']))
    else:
        return ('Je n\'ai pas saisie la question')

def getGrandPyGreating():
    greating_index = randint(0, len(config.grandPy_greatings) - 1)
    return config.grandPy_greatings[greating_index]

def getAdressCoordinnate(adress):
    geocode_result = gmaps.geocode(adress)

    if (len(geocode_result) > 0):        
        return {
            'latitude': geocode_result[0]['geometry']['location']['lat'],
            'longitude': geocode_result[0]['geometry']['location']['lng']
        }
    else:
        return None

if __name__ == "__main__":
    app.run()