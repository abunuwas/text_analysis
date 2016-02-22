import timeit
from random import randint
import re

from ngrams import get_grams, get_grams2


def time_func(func, chars='abcdefghijklmnopqrstuvwxyz', n=20, compute_times=1000):
	chars_list = re.findall('.', chars)
	global string 
	string = 'a'
	results = []
	for i in range(n):
		string += chars_list[randint(0, len(chars_list)-1)]
		time = timeit.timeit('{}(string)'.format(func.__name__), 
								setup='from __main__ import {}, string'.format(func.__name__), 
								number=compute_times)
		profile = {'n': len(string),
					'time': time,
					'time/n': time / n
					}
		results.append(profile)
	return results

def calculate_rate(prev_value, next_value, percentage='no'):
	rate = (next_value-prev_value)/prev_value
	if percentage == 'no':
		return rate
	if percentage == 'yes':
		return rate * 100

def add_rate(results, field_from_dict, new_field_name, percentage='no'):
	for index, result in enumerate(results):
		if index >= 1:
			prev = results[index-1]
			diff_time = calculate_rate(prev[field_from_dict], result[field_from_dict])
		else:
			diff_time, diff_time_per_n = 0, 0
		result[new_field_name] = diff_time
	return results

def print_results(results):
	for index, i in enumerate(results):
		if index >= 1:
			diff = ((i['time']-results[index-1]['time'])/results[index-1]['time'])*100
		else:
			diff = 0
		print('''
n: {} --- time: {:.4f} --- time/n: {:.4f} --- increase: {:.2f}%
			'''.format(i['n'], i['time'], i['time/n'], diff))

def plot_it(*data):
	import matplotlib.pyplot as plt

	data = data[0]

	graph1, graph2 = data['graph1'], data['graph2']

	plt.figure(1)
	plt.subplot(211)
	plt.plot(graph1['n'], graph1['rates'], 'r-')
	plt.ylabel(graph1['func'])
	plt.xlabel('n')

	plt.subplot(212)
	plt.plot(graph2['n'], graph2['rates'], 'g--')
	plt.ylabel(graph2['func'])
	plt.xlabel('n')

	plt.show()

def calculate_average():
	average = 0
	total = 0
	def averager(value):
		nonlocal average
		nonlocal total
		total += 1
		average = (average+value) / total
		return average
	return averager

'''
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

if __name__ == '__main__':
	time_get_grams2 = time_func(get_grams2, n=200)
	time_get_grams = time_func(get_grams, n=200)

	profile_get_grams2 = add_rate(time_get_grams2, 'time/n', 'diff_rate', percentage='yes')
	profile_get_grams = add_rate(time_get_grams, 'time/n', 'diff_rate', percentage='yes')

	rates_grams2 = [i['diff_rate'] for i in profile_get_grams2]
	rates_grams = [i['diff_rate'] for i in profile_get_grams]

	times_per_n_grams2 = [i['time/n'] for i in profile_get_grams2]
	times_per_n_grams = [i['time/n'] for i in profile_get_grams]

	n = [i['n'] for i in profile_get_grams]

	average = 0
	for index, i in enumerate(times_per_n_grams2):
		diff = ((times_per_n_grams[index]-i)/times_per_n_grams[index])*100
		averager = calculate_average()
		average = averager(diff)
		print('N = {} ==> grams: {:.4f} ---- grams2: {:.4f} || diff = {:.2f}%'.format(
																						n[index], 
																						times_per_n_grams[index], 
																						i,
																						diff
																						)
				)
	print('Aveage diff: {:.2f}%'.format(average))

	data = {
			'graph1': {'func': 'get_grams', 'n': n, 'rates': times_per_n_grams}, 
			'graph2': {'func': 'get_grams2', 'n': n, 'rates': times_per_n_grams2}
			}

	plot_it(data)




