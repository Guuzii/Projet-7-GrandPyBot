#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Module containing APIs classes. Use it to request different APIs.

    APIs available:
        - GoogleMaps API
        - Wikimedia API
"""

import json
import requests

import googlemaps

import config


class GoogleApi:
    """
        Class that represent GoogleMaps API.

        Initialize a googlemaps client to request the API.

        Attributes:
            - gmaps: the client identified with an API key used to request the API
    """
    def __init__(self):
        self.gmaps = googlemaps.Client(key=config.GOOGLE_API_KEY)


    def getPlaceCoordinnate(self, place: str):
        """
            Request the Places API from GoogleMaps to get adress and coordinate depending on a string passed in argument.

            Parameters:
                - place (str): parsed string containing keyword for the places research
            
            Returns:
                - (dict): a dictionary containing the adress, the latitude and the longitude present in the response for the request
        """
        
        places_result = self.gmaps.places(place)

        if (places_result['status'] == 'OK'):      
            return {
                'adress': places_result['results'][0]['formatted_address'],
                'latitude': str(places_result['results'][0]['geometry']['location']['lat']),
                'longitude': str(places_result['results'][0]['geometry']['location']['lng'])
            }
        else:
            return None


class WikiApi:
    """
        Class that represent Wikimedia API.

        Use Wikimedia API to get information depending on coordinate.
    """
    def __init__(self):        
        pass

    def getDataFromPlace(self, lat: str, lng: str):
        """
            Query the Wikimedia API using the geocode module to get data depending on coordinate.

            Parameters:
                - lat (str): the latitude to use in params for the request
                - lng (str): the longitude to use in params for the request
            
            Returns:
                - (str): a text extract from the page found with the specified coordinate 
        """
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
            return 'Je n\'ai rien trouvé dans un rayon de ' + str(params['ggsradius']) + ' mètres.'

        page_id = list(wikimedia_result)[0]

        return 'Savais-tu que ' + wikimedia_result[page_id]['extract']