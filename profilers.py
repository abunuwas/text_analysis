import timeit
from random import randint
import re

def time_func(func):
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