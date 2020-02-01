from ..parser import Parser 
from ..apis import GoogleApi, WikiApi

def test_parser():
    parser_to_test = Parser('Test1 abord test2;s etre test3  quatre ,:/"')
    assert parser_to_test.parseUserQuestion() == 'test1 test2 test3'

def test_google_api():
    api_to_test = GoogleApi('openclassrooms')
    assert api_to_test.getPlaceCoordinnate() == { 'latitude': '48.8748465', 'longitude': '2.3504873'}

def test_wiki_api():
    api_to_test = WikiApi('48.8493088', '2.3685024')
    assert api_to_test.getDataFromPlace() == "Savais-tu que Le jardin du Port-de-l'Arsenal est un espace vert situé dans le 12e arrondissement de Paris, dans le quartier des Quinze-Vingts."
    


