import re
import config

class Parser:

    def __init__(self):
        pass

    def parseUserQuestion(self, user_question):
        splited_string = re.sub(r'[^\w\s]', ' ', user_question)
        splited_string = splited_string.split(' ')
        parsed_string = ''

        for string in splited_string:

            if string.lower() not in config.STOP_WORDS:
                parsed_string += string + ' '
                
        parsed_string = parsed_string.lower()
        parsed_string = parsed_string.strip()
        
        return parsed_string