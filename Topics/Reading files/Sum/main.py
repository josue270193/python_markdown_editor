sums_file = open("sums.txt")
for line in sums_file:
    number_1, number_2 = line.split()
    print(int(number_1) + int(number_2))

sums_file.close()
