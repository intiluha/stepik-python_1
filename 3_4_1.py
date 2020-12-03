with open('3_4_1_input.txt') as inf:
	zipped = inf.readline().strip()
	unzipped = ''
	i = 0
	N = len(zipped)
	while i < N:
		c = zipped[i]
		i += 1
		n = ''
		while i < N and '0' <= zipped[i] <= '9':
			n += zipped[i]
			i += 1
		unzipped += int(n)*c
with open('3_4_1_output.txt', 'w') as outf:
	outf.write(unzipped)