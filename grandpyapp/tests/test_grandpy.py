#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ..classes.parser import Parser
from ..classes.apis import GoogleApi, WikiApi


def test_parser():
    assert (
        Parser().parseUserQuestion('Test1 abord test2;s etre test3  quatre ,:/"')
        == "test1 test2 test3"
    )


def test_google_api_return(monkeypatch):
    results = {
        "adress": "7 Cité Paradis, 75010 Paris, France",
        "latitude": "48.8748465",
        "longitude": "2.3504873",
    }

    def mockreturn(*param):
        return results

    monkeypatch.setattr(
        "grandpyapp.classes.apis.GoogleApi.getPlaceCoordinnate", mockreturn
    )

    assert GoogleApi().getPlaceCoordinnate("openclassrooms") == results


def test_wiki_api(monkeypatch):
    results = "Savais-tu que Le jardin du Port-de-l'Arsenal est un espace vert situé dans le 12e arrondissement de Paris, dans le quartier des Quinze-Vingts."

    def mockreturn(*param):
        return results

    monkeypatch.setattr("grandpyapp.classes.apis.WikiApi.getDataFromPlace", mockreturn)

    assert WikiApi().getDataFromPlace("48.8493088", "2.3685024") == results
