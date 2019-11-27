## This has example to add keyword to NLTK tokenizer for splitting better sentences.

from nltk.tokenize.punkt import PunktSentenceTokenizer, PunktParameters
punkt_param = PunktParameters()
abbreviation = ['Sr', 'sr','e.g','i.e']
punkt_param.abbrev_types = set(abbreviation)
#tokenizer._params.abbrev_types.add('dr')
tokenizer = PunktSentenceTokenizer(punkt_param)
tokenizer.tokenize('Entry level knowledge of Cloud solutions i.e.: Amazon, Google, Microsoft Azure \
Ability to proactively solve complex problems both individually and as part of a team')
