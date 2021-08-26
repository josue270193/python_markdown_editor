test_file = open("test_file.txt", encoding="utf-16")
for line in test_file:
    print(line)
    break
test_file.close()
