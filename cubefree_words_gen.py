from random import choice
import time

def isCube(s):
	for i in range(1,1 + int(len(s)/3)):
		if s[-i:] == s[-i*2:-i] == s[-i*3:-i*2]:
			return i
	return 0

def genSequens(alpha, length, optimize):
	freq = {}
	str_k = ""
	counter = 0
	s = choice(alpha)
	rand_s = s
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
			ch = choice(alpha)
			s += ch
			rand_s += ch
		k = isCube(s)
		if k > 0 :
			#if k != 1:
			#	print(str(k) + '	' + s[-k:])
			#if not k in freq:
			#	freq[k] = 0
			#freq[k] += 1
			#str_k += str(k) + "\t"
			s = s[:-k]#(k+int(k/2))]
		#if counter > length*10 :
		#	break
	return counter, rand_s
	
def genSequens2(alpha, length, optimize):
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
		s = cutCube(1, s)
	return len(s)

def cutCube(k_count, s):
	k = isCube(s)
	if k > 0 :
		s = s[:-k_count*k]
	return s

def genSequens2KOptimize(alpha, length):
	counter = 1
	s = choice(alpha)
	while len(s) < length :
		if s[-2:] == "00":
			while s[-1:] != "1":
				s += choice(alpha)
				s = cutCube(2, s)
		elif s[-2:] == "11":
			while s[-1:] != "0":
				s += choice(alpha)
				s = cutCube(2, s)
		else:
			s += choice(alpha)
			counter += 1
		s = cutCube(2, s)
	return counter

def randomCountDiffCubeFreeWords(alpha, fromLen, toLen):
	for k in range(fromLen,toLen):
		dic = {}
		f = open('test' + str(k), 'w')
		for i in range(5000000):
			(count, s) = genSequens(alpha, k, False)
			if s not in dic:
				dic[s] = 0
			dic[s] += 1
		print(k, len(dic.keys()))
		for key in sorted(dic.keys()):
			f.write(str(key) + "\t" + str(dic[key]) + "\n")
		f.close()

alphabet = "01"
start = time.time()

randomCountDiffCubeFreeWords(alphabet, 4, 11)
# for i in range(1000):
# 	count = genSequens2(alphabet, 10000, False)
# 	print(count)
finish = time.time()
# print(s)
# print(str(len(s)) + '	' + str(counter) + '	' + str(freq))
# print(finish - start)
# print(str(len(s)) + '	' + str(counter));
