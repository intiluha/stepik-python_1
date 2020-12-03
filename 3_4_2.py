with open('3_4_2_input.txt') as inf:
	D = {}
	for line in inf:
		S = line.lower().split()
		for w in S:
		    if w in D:
		        D[w] += 1
		    else:
		        D[w] = 1
max_key, max_value = 0, 0
for k in D:
	if D[k] > max_value or D[k] == max_value and k < max_key:
		max_key, max_value = k, D[k]
print(max_key, max_value)