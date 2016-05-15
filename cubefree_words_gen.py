from random import choice
import time

def isCube(s):
	for i in range(1,1 + int(len(s)/3)):
		if s[-i:] == s[-i*2:-i] == s[-i*3:-i*2]:
			return i
	return 0

def genSequens(alpha, length, optimize):#Строим по случайной бесконечной последовательности слово конкретной длины
	freq = {}
	str_k = ""
	counter = 0
	s = choice(alpha)
	while len(s) < length :
		# print(alpha, length, optimize, s)
		counter += 1
		if optimize:
			isWork = False
			if s[-2:] == "00":
				s += "1"
				isWork = True
			if s[-2:] == "11":
				s += "0"
				isWork = True
			# if s[-5:] == "01010":
			# 	s += "0"
			# 	isWork = True
			# if s[-5:] == "10101":
			# 	s += "1"
			# 	isWork = True
			if isWork:
				counter -= 1
		if not optimize or not isWork:
			s += choice(alpha)
		k = isCube(s)
		if k > 0 :
			#if k != 1:
			#	print(str(k) + '	' + s[-k:])
			#if not k in freq:
			#	freq[k] = 0
			#freq[k] += 1
			#str_k += str(k) + "\t"
			s = s[:-2*k]#(k+int(k/2))]
		#if counter > length*10 :
		#	break
	return counter
	
def genSequens2(alpha, length, optimize):#Строим по случайной последовательности фиксированной длинны бескубное слово.
	s = ""
	i = 0
	count = 0
	while i < length:
		if optimize:
			isWork = False
			if s[-2:] == "00":
				s += "1"
				count += 1
				isWork = True
			if s[-2:] == "11":
				s += "0"
				count += 1
				isWork = True
		if not optimize or not isWork:
			s += choice(alpha)
			i += 1
		k = isCube(s)
		if k > 0 :
			s = s[:-2*k]
	print("Count", count)
	return len(s)

def genSequens3(alpha, length, optimize):#Удлаялем из случайной последовательности повторяющиеся символы


alphabet = "01"
start = time.time()
for i in range(1000):
	count = genSequens2(alphabet, 1000, False)
	print(count)
finish = time.time()
# print(s)
# print(str(len(s)) + '	' + str(counter) + '	' + str(freq))
# print(finish - start)
# print(str(len(s)) + '	' + str(counter));
