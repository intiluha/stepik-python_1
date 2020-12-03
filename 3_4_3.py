with open('3_4_3_input.txt', encoding='utf-8') as infile:
	with open('3_4_3_output.txt', 'w') as outfile:
		n, math, phys, russ = 0, 0, 0, 0
		for line in infile:
			n += 1
			m, p, r = (int(i) for i in line.strip().split(';')[1:])
			math += m
			phys += p
			russ += r
			outfile.write(str((m + p + r) / 3) + '\n')
		outfile.write(str(math / n) + ' ' + str(phys / n) + ' ' + str(russ / n))