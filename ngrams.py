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

def get_grams(string):
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


def time_func(func):
	import timeit
	from random import randint
	import re

	letters = re.findall('.', 'abcdefghijklmnopqrstuvwxyz')
	global string 
	string = 'a'
	result = []
	for i in range(25):
		string += letters[randint(0, len(letters)-1)]
		time = timeit.timeit('{}(string)'.format(func.__name__), 
								setup='from __main__ import {}, string'.format(func.__name__), 
								number=1000)
		profile = {'n': len(string),
					'time': time,
					'time/n': time/len(string) 
					}
		result.append(profile)
	return result

results = time_func(get_grams2)

def print_results(results):
	for index, i in enumerate(results):
		if index >= 1:
			diff = ((i['time']-results[index-1]['time'])/results[index-1]['time'])*100
		else:
			diff = 0
		print('''
n: {} --- time: {:.4f} --- time/n: {:.4f} --- increase: {:.2f}%
			'''.format(i['n'], i['time'], i['time/n'], diff))

print_results(results)

n = [i['n'] for i in results]
times = [i['time'] for i in results]
diffs = []
for index, i in enumerate(results):
	if index >= 1:
		diff = ((i['time']-results[index-1]['time'])/results[index-1]['time'])*100
	else:
		diff = 0
	diffs.append(diff)
import matplotlib.pyplot as plt
plt.figure(1)
plt.subplot(211)
plt.plot(n, times, 'r-')
#xaxis = [min(n)-1, max(n)+1]
#yaxis = [min(times)-1, max(times)+1]
#plt.axis(xaxis + yaxis)
plt.ylabel('time to compute n')
plt.subplot(212)
plt.plot(n[1:], diffs[1:], 'g--')
plt.ylabel('increases %')

plt.show()

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
