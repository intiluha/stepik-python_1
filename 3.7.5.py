heights = [[] for i in range(12)]
with open('dataset_3380_5.txt') as f:
    for line in f.readlines():
        clas, name, heig = line.split('\t')
        heights[int(clas)].append(int(heig))
with open('ans_3.7.5.txt', 'w') as f:
    for i in range(1, 12):
        f.write(str(i) + ' ')
        if heights[i] == []:
            f.write('-\n')
        else:
            f.write(str(sum(heights[i]) / len(heights[i])) + '\n')