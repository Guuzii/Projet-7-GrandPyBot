import json
import requests

import googlemaps

import config


class GoogleApi:

    def __init__(self):
        self.gmaps = googlemaps.Client(key=config.GOOGLE_API_KEY)

    def getPlaceCoordinnate(self, place):
        # Places request to get coordinate
        places_result = self.gmaps.places(place)

        if (len(places_result['results']) > 0):      
            return {
                'latitude': str(places_result['results'][0]['geometry']['location']['lat']),
                'longitude': str(places_result['results'][0]['geometry']['location']['lng'])
            }
        else:
            return None


class WikiApi:

    def __init__(self):        
        pass

    def getDataFromPlace(self, lat, lng):
        params = {
            'action': 'query',
            'prop': 'extracts',
            'exintro': 'true',
            'explaintext': 'true',
            'generator': 'geosearch',
            'ggsradius': 500,
            'ggslimit': 1,
            'ggscoord': lat + '|' + lng,
            'format': 'json'
        }

        res = requests.get(url=config.WIKIPEDIA_API_ENDPOINT, params=params)
        
        try:
            wikimedia_result = res.json()['query']['pages']
        except:
            return ('Je n\'ai rien trouvé dans un rayon de ' + str(params['ggsradius']) + ' mètres.')

        page_id = list(wikimedia_result)[0]

        return ('Savais-tu que ' + wikimedia_result[page_id]['extract'])