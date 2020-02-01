import re
import config

class Parser:

    def __init__(self, string):
        self.user_question = string

    def parseUserQuestion(self):
        splited_string = re.sub(r'[^\w\s]', ' ', self.user_question)
        splited_string = splited_string.split(' ')
        parsed_string = ''

        for string in splited_string:

            if string.lower() not in config.STOP_WORDS:
                parsed_string += string + ' '
                
        parsed_string = parsed_string.lower()
        parsed_string = parsed_string.strip()       

        print (parsed_string)
        return parsed_string