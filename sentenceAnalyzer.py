import nltk

class CrimeSentenceAnalyzer: 

    def __init__(self):
        self._victim_grammar_file = '635/victime.fcfg'
        self._location_grammar_file = '635/emplacement.fcfg'
        self._crime_hour_grammar_file = '635/heure_crime.fcfg'

    def who_is_the_victime(self, sentence):
        nltk.interpret_sents(sentence, self._victim_grammar_file)

    def where_am_i(self, sentence):
        nltk.interpret_sents(sentence, self._location_grammar_file)

    def what_is_the_crime_hour(self, sentence):
        nltk.interpret_sents(sentence, self._crime_hour_grammar_file)