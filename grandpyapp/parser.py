import re
import config

class Parser:

    def __init__(self, string):
        self.user_question: str = string

    def parseUserQuestion(self):
        to_split = re.sub(r'[^\w\s]', ' ', self.user_question)
        splited_string = to_split.split(' ')
        parsed_string = ''

        for string in splited_string:

            if string.lower() not in config.STOP_WORDS:
                parsed_string += string + ' '       

        parsed_string.strip()

        return parsed_string