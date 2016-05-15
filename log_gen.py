def isCube(s):
	for i in range(1,1 + int(len(s)/3)):
		if s[-i:] == s[-i*2:-i] == s[-i*3:-i*2]:
			return i
	return 0

def log_gen(gen_count, str_len, zero_len):
	if gen_count == 0:
		return [""]
	list = []
	for log in log_gen(gen_count - 1, str_len + 1, 0):
		list.append("1" + log)
	if str_len >= 3 * (zero_len + 1): 
		for log in log_gen(gen_count - 1, str_len - (zero_len + 1), zero_len + 1):
			list.append("0" + log)
	return list

def get_all_logs(gen_count):
	if gen_count == 0:
		return [""]
	list = []
	for log in get_all_logs(gen_count - 1):
		list.append("0" + log)
		list.append("1" + log)
	return list

def filtrate(logs, incorrect):
	clean_log = []
	for l in logs:
		if len(l) > 0 and l[0] == "0":
			l = "1" + l
		f = True
		for i in incorrect:
			if l.find(i) != -1:
				f = False
				break
		if f:
			clean_log.append(l)
	return clean_log

def get_logs(gen_count):
	return log_gen(gen_count, 0, 0)

def list_to_str(li):
	s = ""
	for l in li:
		s += chr(l+60)
	return s

def correct_check(log, add_valid_prefix):
	pref = ""
	if add_valid_prefix:
		for i in range(len(log)*3):
			pref += "1"
	log = pref + log
	debug = False
	list = []
	new = 0
	i = 0
	z_count = 0
	for op in log:
		if op == "1":
			if not add_valid_prefix and (z_count*2 > len(list)):
				return False
			if z_count > 0:
				for j in range(z_count):
					for k in range(len(list)):
						val = list[i-z_count+j]
						if list[k] == val:
							list[k] = list[i-2*z_count+j]
				z_count = 0
			list.append(new)
			new += 1
			i += 1
		else:
			if not add_valid_prefix and (len(list) < 1):
				return False
			list.pop()
			i -= 1
			z_count += 1
		if debug:
			print(i)
			print(z_count)
			print(list)
		if isCube(list_to_str(list)):
			return False
	if z_count > 0:
		if not add_valid_prefix and (z_count*2 > len(list)):
			return False
		for j in range(z_count):
			for k in range(len(list)):
				val = list[i-z_count+j]
				if list[k] == val:
					list[k] = list[i-2*z_count+j]
	if debug:
		print(i)
		print(z_count)
		print(list)
	if isCube(list_to_str(list)):
			return False
	return True


#print correct_check("1111110010", True)
#print(get_logs(7))
#print(get_all_logs(7))
incorrect = ["10101"]
for length in range(23):
	# print(str(length) + "	" + str(len(get_all_logs(length))))
	for log in filtrate(get_all_logs(length), incorrect):
		if not correct_check(log, True):
			incorrect.append(log)
	for i in incorrect:
		print(i)
	# for log in get_all_logs(length):
	# 	if not correct_check(log, True):
	# 		if log[0] == "0":
	# 			print("1" + log)
	# 		else:
	# 			print(log)
	

