import nltk

class CrimeSentenceAnalyzer: 

    def __init__(self):
        self._victim_grammar_file = '635/victime.fcfg'
        self._location_grammar_file = '635/emplacement.fcfg'
        self._crime_hour_grammar_file = '635/heure_crime.fcfg'
        self._location_hour_grammar_file = '635/emplacement_heure.fcfg'

    def who_is_the_victime(self, sentence):
        return str(nltk.interpret_sents(sentence, self._victim_grammar_file)[0][0][1])

    def where_am_i(self, sentence):
        return str(nltk.interpret_sents(sentence, self._location_grammar_file)[0][0][1])

    def what_is_the_crime_hour(self, sentence):
        return str(nltk.interpret_sents(sentence, self._crime_hour_grammar_file)[0][0][1])

    def where_in_room_in_hour(self, sentence):
        result = str(nltk.interpret_sents(sentence, self._location_hour_grammar_file)[0][0][1])
        return self.parse_result(result)

    def parse_result(self, result):
        response = {}
        response['name'] = result.split(',')[0].split('(')[1]
        response['room'] = result.split(',')[1]
        response['hour'] = result.split(',')[2].split(')')[0]
        return response