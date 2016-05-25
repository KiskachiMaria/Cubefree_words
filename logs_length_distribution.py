def isCube(s):
	for i in range(1,1 + int(len(s)/3)):
		if s[-i:] == s[-i*2:-i] == s[-i*3:-i*2]:
			return i
	return 0

def build_log(str, log, ch):
	s = str + ch
	log += '1'
	cube = isCube(s)
	if cube > 0:
		log += '0' * cube
		s = s[:-cube]
	return s, log
dic = {}

def log_gen(gen_count, str, log):
	if gen_count == 0:
		if len(log) not in dic:
			dic[len(log)] = 0
		dic[len(log)] += 1
		return
	s0, log0 = build_log(str, log, '0')
	s1, log1 = build_log(str, log, '1')
	log_gen(gen_count - 1, s0, log0)
	log_gen(gen_count - 1, s1, log1)

log_gen(31, "", "")
print(dic)
#for j in range(28, 29):
	#dic = {}
	#for i in log_gen(j, "", ""):
		# print(i)
	#	if len(i) not in dic:
	#		dic[len(i)] = 0
	#	dic[len(i)] += 1
	#for k in sorted(dic.keys()):
	#	print(j, k, dic[k])# sep="\t")