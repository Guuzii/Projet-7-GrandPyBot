# Projet-7-GrandPyBot

Web app made with Flask that uses Google Maps and Media Wiki API to answer questions from the user about a location and giving information about that place with the data from wikipedia.
This programm has been developped for a python course.

## Requirements

    - Python 3.7
    - Pip
    - Pipenv
    - A valid google api key

## Installation

    - Clone the project,
    - Create a file named apiKey.py at the root of the directory
    - Add in the created file apiKey.py a variable named GOOGLE_API_KEY containing your api key
    - setup virtual env : pipenv --python 3.7
    - get into your virtual env : pipenv shell
    - install requirements : pipenv install
    - run locally : python main.py

The app need either an environment variable called 'GOOGLE_API_KEY' containing your api key or file apiKey.py containing this variable.

## Usage

Get to the url where your app is deploy.
The bot welcome you with a sentence.
Enter your question in the text input and click "envoyer" or press enter.
The bot give you an answer appropriate for your question followed by a map of the location if he found one.