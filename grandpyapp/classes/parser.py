import re
import config

"""
    Module containing the classe in charge of parsing the user question.
"""


class Parser:
    """
        Class that handle user's question parsing
    """

    def __init__(self):
        pass

    def parseUserQuestion(self, user_question: str):
        """
        Method that parse user's question

        Use a regex to take out all punctuation then split the string 
        to check for every words if they are contained in the stopword list.

        Parameters:
            - user_question (str): the user question to parse
        
        Returns:
            - (str): the parsed string 
    """
        splited_string = re.sub(r"[^\w\s]", " ", user_question)
        splited_string = splited_string.split(" ")
        parsed_string = ""

        for string in splited_string:

            if string.lower() not in config.STOP_WORDS:
                parsed_string += string + " "

        parsed_string = parsed_string.lower()
        parsed_string = parsed_string.strip()

        return parsed_string
