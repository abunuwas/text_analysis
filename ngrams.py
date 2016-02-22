import os

'''
current_dir = os.getcwd()
texts_dir = os.path.join('texts')
texts = [text for text in os.listdir(texts_dir) if text.endswith('.txt')]
text = os.path.join(texts_dir, texts[0])
text = open(text, 'r', encoding='utf-8').read()
len_text = len(text)
text_test = text[:int(len_text*.1)]
print(len(text_test))
'''

def get_grams(string, start=None, skip=None, end=None):
	grams = {}

	for index, char in enumerate(string):
		try:
			gram = string[index:index+2]
			chain = string[index:index+2]
		except IndexError:
			pass 
		values = grams.get(gram, {'count': 0, 'chains': set()})
		values['count'] += 1
		values['chains'].add(chain)
		grams[gram] = values
	return grams

def get_grams2(string):
	grams = {}

	for index, char in enumerate(string):
		try:
			gram = string[index:index+2]
			chain = string[index:index+2]
		except IndexError:
			pass 
		if gram in grams:
			grams[gram]['count'] += 1
			grams[gram]['chains'].add(chain)
		else:
			grams[gram] = {'count': 1, 'chains': {chain}}
	return grams




'''
counter_bigram = set()
for key, value in four_len_bigrams.items():
	counter_key = value['count']
	counter_bigram.add((counter_key, key))

counter_bigram = sorted(four_len_bigrams.items(), key=lambda value: value[1]['count'], reverse=True)
print(len(counter_bigram))
print(counter_bigram[200][0], counter_bigram[0][1]['count'])

from collections import OrderedDict
counter_bigram3 = OrderedDict(sorted(four_len_bigrams.items(), key=lambda keyvalue: keyvalue[1]['count']))
'''
