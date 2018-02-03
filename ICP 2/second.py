file = open('words.txt', 'r')
result = open('result.txt', 'w')
line = file.readline().lower()
while line != "":
    i = (len(line)-1)
    print(line, i)
    result.write('{:0d}\n'.format(i))
    line = file.readline().lower()